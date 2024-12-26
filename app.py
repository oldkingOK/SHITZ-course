import configparser
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
        context = browser.new_context()  # 创建上下文以便管理Cookie
        page = context.new_page()

        # 打开指定网页
        url = "https://ids.hit.edu.cn/authserver/login?service=http%3A%2F%2Fjw.hitsz.edu.cn%2FcasLogin"
        page.goto(url)

        # 等待并点击名称为"Shenzhen"或"深圳校区"的元素
        try:
            # 等待元素出现并点击
            page.wait_for_selector('a:has-text("Shenzhen"), a:has-text("深圳校区")', timeout=60000)  # 等待60秒
            page.click('a:has-text("Shenzhen"), a:has-text("深圳校区")')
        except Exception as e:
            print("元素未找到：", e)
            browser.close()
            return

        # 填充用户名和密码
        try:
            page.fill('input.oauth_inputuser', username)  # 从配置文件读取用户名
            page.fill('input.oauth_inputpassword', password)  # 从配置文件读取密码
        except Exception as e:
            print("无法填充用户名或密码：", e)
            browser.close()
            return

        # 提交登录表单
        # page.press('input.oauth_inputpassword', 'Enter')

        # 点击 .oauth__btn2 按钮
        try:
            page.wait_for_selector('.oauth__btn2', timeout=10000)  # 等待按钮出现
            page.click('.oauth__btn2')
        except Exception as e:
            print("无法点击按钮 .oauth__btn2：", e)
            browser.close()
            return

        # 等待页面跳转
        page.wait_for_load_state('load')

        # 获取并打印当前页面的Cookie
        cookies = context.cookies()
        print("当前Cookie：", cookies)

        # 关闭浏览器
        input("按任意键关闭浏览器...")
        browser.close()

if __name__ == "__main__":
    main()
