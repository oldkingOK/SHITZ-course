DATA = "cxsfmt=0&p_pylx=1&mxpylx=1&p_sfgldjr=0&p_sfredis=0&p_sfsyxkgwc=0&p_xktjz=rwtjzyx&p_chaxunxh=&p_gjz=&p_skjs=&p_xn=2024-2025&p_xq=2&p_xnxq=2024-20252&p_dqxn=2024-2025&p_dqxq=1&p_dqxnxq=2024-20251&p_xkfsdm={}&p_xiaoqu=&p_kkyx=&p_kclb=&p_xkxs=&p_dyc=&p_kkxnxq=&p_id={}&p_sfhlctkc=0&p_sfhllrlkc=0&p_kxsj_xqj=&p_kxsj_ksjc=&p_kxsj_jsjc=&p_kcdm_js=&p_kcdm_cxrw=&p_kc_gjz=&p_xzcxtjz_nj=&p_xzcxtjz_yx=&p_xzcxtjz_zy=&p_xzcxtjz_zyfx=&p_xzcxtjz_bj=&p_sfxsgwckb=1&p_skyy=&p_chaxunxkfsdm=&pageNum=1&pageSize=21"
URL = "http://jw.hitsz.edu.cn/Xsxk/addGouwuche"
COOKIE = "JSESSIONID=452098A4335A003914041BD920F39EBE; Path=/; HttpOnly, route=2f5ea2943ce43bccdc54bd1e6f73f716; Path=/"
ID = "2A2CD36B53159179E0630B18F80A81BE"

import requests

class ClassType:
    MUST = "bx-b-b" 
    """必修"""
    LIMIT = "xx-b-b" 
    """限选"""
    SPORTS = "ty-b-b"
    """体育"""
    WRITE = "xzygt-b-b"
    """写作与沟通"""
    CREATIVE = "cxcytx-b-b"
    """创新创业通选课"""
    PRACTICE = "shsj-b-b"
    """社会实践课"""
    COMPETITION = "jsrw-b-b"
    """竞赛指导课程体系"""
    CREATIVE_RESEARCH = "cxyx-b-b"
    """创新研究"""
    CREATIVE_EXPIREMENT = "cysy-b-b"
    """创新实验"""
    CROSS_IN_PLAN = "fankzy-b-b"
    """方案内跨专业"""
    CROSS = "sx-b-b" 
    """跨专业课程体系"""


def grab_class(id, cookie, type=ClassType.MUST):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://jw.hitsz.edu.cn",
        "Referer": "http://jw.hitsz.edu.cn/Xsxk/query/1",
        "Connection": "keep-alive",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    }

    cookies = {
        "JSESSIONID": cookie.split(";")[0].split("=")[1],
        "route": cookie.split(";")[2].split("=")[1]
    }
    
    # cookies = {
    #     "JSESSIONID": "A879873B12E1D04CD2B0AAE8627A7DB5",
    #     "route": "1db2c5f6085b9278d9cf7aaa8af65cd2"
    # }

    print(cookies)
    response = requests.post(URL, 
                            data=DATA.format(type, id), 
                            cookies=cookies,
                            headers=headers,
                            allow_redirects=False)

    if response.status_code != 200:
        print("Failed to grab class")
        return None
    
    try:
        return response.json()
    except:
        print("Failed to parse response as JSON")
        # print(response.text)
        return response.text

if __name__ == "__main__":
    grab_class(ID, COOKIE)