DATA = "cxsfmt=0&p_pylx=1&mxpylx=1&p_sfgldjr=0&p_sfredis=0&p_sfsyxkgwc=0&p_xktjz=rwtjzyx&p_chaxunxh=&p_gjz=&p_skjs=&p_xn=2024-2025&p_xq=2&p_xnxq=2024-20252&p_dqxn=2024-2025&p_dqxq=1&p_dqxnxq=2024-20251&p_xkfsdm=bx-b-b&p_xiaoqu=&p_kkyx=&p_kclb=&p_xkxs=&p_dyc=&p_kkxnxq=&p_id={}&p_sfhlctkc=0&p_sfhllrlkc=0&p_kxsj_xqj=&p_kxsj_ksjc=&p_kxsj_jsjc=&p_kcdm_js=&p_kcdm_cxrw=&p_kc_gjz=&p_xzcxtjz_nj=&p_xzcxtjz_yx=&p_xzcxtjz_zy=&p_xzcxtjz_zyfx=&p_xzcxtjz_bj=&p_sfxsgwckb=1&p_skyy=&p_chaxunxkfsdm=&pageNum=1&pageSize=21"
URL = "http://jw.hitsz.edu.cn/Xsxk/addGouwuche"
COOKIE = "JSESSIONID=452098A4335A003914041BD920F39EBE; Path=/; HttpOnly, route=2f5ea2943ce43bccdc54bd1e6f73f716; Path=/"
ID = "2A2CD36B53159179E0630B18F80A81BE"

import requests

def grab_class(id, cookie):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://jw.hitsz.edu.cn",
        "Referer": "http://jw.hitsz.edu.cn/Xsxk/query"
    }

    cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie.split(", ")}
    response = requests.post(URL, 
                            data=DATA.format(id), 
                            cookies=cookies,
                            headers=headers)
    print(response.text)

if __name__ == "__main__":
    grab_class(ID, COOKIE)