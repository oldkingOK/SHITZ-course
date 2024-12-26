import configparser
import requests
import os
from playwright.sync_api import sync_playwright

def main():
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
        url = "https://ids.hit.edu.cn/authserver/login?service=http%3A%2F%2Fjw.hitsz.edu.cn%2FcasLogin"
        page.goto(url)
        input("请手动登录，登录成功后按任意键继续...")

        # 等待并点击名称为"Shenzhen"或"深圳校区"的元素
        try:
            # 等待元素出现并点击
            page.wait_for_selector('a:has-text("Shenzhen"), a:has-text("深圳校区")', timeout=60000)  # 等待60秒
            page.click('a:has-text("Shenzhen"), a:has-text("深圳校区")')
        except Exception as e:
            print("元素未找到：", e)
            return

        # 填充用户名和密码
        try:
            page.fill('input.oauth_inputuser', username)  # 从配置文件读取用户名
            page.fill('input.oauth_inputpassword', password)  # 从配置文件读取密码
        except Exception as e:
            print("无法填充用户名或密码：", e)
            return

        # 提交登录表单
        page.press('input.oauth_inputpassword', 'Enter')

        # 点击 .oauth__btn2 按钮
        try:
            page.wait_for_selector('.oauth__btn2', timeout=10000)  # 等待按钮出现
            page.click('.oauth__btn2')
        except Exception as e:
            print("无法点击按钮 .oauth__btn2：", e)
            return

        # 手动请求 http://jw.hitsz.edu.cn/casLogin
        # def handle_request(route, request):
        #     print("拦截到请求：", request.url)
        #     if "http://jw.hitsz.edu.cn/casLogin" in request.url:
        #         print("拦截到请求，开始手动发送...")
        #         response = requests.get(request.url, headers=request.headers)
        #         if response.status_code == 200:
        #             set_cookie_header = response.headers.get("Set-Cookie", None)
        #             if set_cookie_header:
        #                 print("Set-Cookie 中的 Cookie：", set_cookie_header)
        #         route.continue_()

        # context.route("http://jw.hitsz.edu.cn/casLogin", handle_request)

        # 保存浏览器上下文的存储状态
        context.storage_state(path="state.json")

if __name__ == "__main__":
    main()
    input("按任意键退出...")