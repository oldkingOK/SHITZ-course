import requests

def get_cookie(ticket_url):
    response = requests.get(ticket_url, allow_redirects=False)

    set_cookie_header = response.headers.get("Set-Cookie", None)
    if set_cookie_header:
        return set_cookie_header
    else:
        return None

if __name__ == "__main__":
    get_cookie("http://jw.hitsz.edu.cn/casLogin?ticket=TICKET")