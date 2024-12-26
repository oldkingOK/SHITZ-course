import configparser
import requests
import os
from playwright.sync_api import sync_playwright
from getcookie import get_cookie

URL = "https://ids.hit.edu.cn/authserver/login?service=http%3A%2F%2Fjw.hitsz.edu.cn%2FcasLogin"

def get_ticket_url():
    """通过手动登录获取 ticket URL"""

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('config.ini')
    username = config.get('credentials', 'username')
    password = config.get('credentials', 'password')

    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch(headless=False)
        # load storage state if it exists
        if os.path.exists("state.json"):
            print("加载存储状态...")
            context = browser.new_context(storage_state="state.json")
        else:
            print("未找到存储状态，新建上下文...")
            context = browser.new_context()
        
        page = context.new_page()

        # 打开指定网页
        # 尝试使用 context 的 Cookie 并使用 requests 请求 url，打印出 Response
        cookies = {cookie['name']: cookie['value'] for cookie in context.cookies()}
        response = requests.get(URL, cookies=cookies, allow_redirects=False)
        if response.status_code == 302:
            return response.headers['Location']

        page.goto(URL)

        # 等待并点击名称为"Shenzhen"或"深圳校区"的元素
        try:
            # 等待元素出现并点击
            page.wait_for_selector('a:has-text("Shenzhen"), a:has-text("深圳校区")', timeout=60000)  # 等待60秒
            page.click('a:has-text("Shenzhen"), a:has-text("深圳校区")')
        except Exception as e:
            print("元素未找到：", e)
            return

        # 如果有 .oauth__btn2 按钮，填充用户名和密码
        if page.query_selector('.oauth__btn2'):
            # 填充用户名和密码
            try:
                page.fill('input.oauth_inputuser', username)  # 从配置文件读取用户名
                page.fill('input.oauth_inputpassword', password)  # 从配置文件读取密码
            except Exception as e:
                print("无法填充用户名或密码：", e)
                return

            # 点击 .oauth__btn2 按钮
            try:
                page.wait_for_selector('.oauth__btn2', timeout=10000)  # 等待按钮出现
                page.click('.oauth__btn2')
            except Exception as e:
                print("无法点击按钮 .oauth__btn2：", e)
                return

        # 如果有 #btn_part1 按钮，点击
        if page.query_selector('#btn_part1'):
            try:
                page.wait_for_selector('#btn_part1', timeout=10000)  # 等待按钮出现
                page.click('#btn_part1')
            except Exception as e:
                print("无法点击按钮 #btn_part1：", e)
                return

        # 保存浏览器上下文的存储状态
        context.storage_state(path="state.json")
        browser.close()

    # 拿到 Cookie 后，重新获取 ticket URL
    return get_ticket_url()

if __name__ == "__main__":
    url = get_ticket_url()
    if url:
        print("获取到 ticket URL：", url)
        print("获取到的 Cookie：", get_cookie(url))
    input("按任意键退出...")