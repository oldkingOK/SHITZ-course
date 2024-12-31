from get_ticket import get_ticket_url
from get_cookie import get_cookie
from grab import grab_class, ClassType
from time import sleep
import os

ticket_url = ""
cookie = ""
TICKET_PATH = ".ticket"
COOKIE_PATH = ".cookies"

if (os.path.exists(TICKET_PATH)):
    with open(TICKET_PATH, "r") as f:
        ticket_url = f.read()
    print("Loaded Ticket URL:", ticket_url)

if (os.path.exists(COOKIE_PATH)):
    with open(COOKIE_PATH, "r") as f:
        cookie = f.read()
    print("Loaded Cookie:", cookie)

def u_ticket():
    global ticket_url
    ticket_url = get_ticket_url()
    if ticket_url:
        print("Ticket URL:", ticket_url)
        with open(TICKET_PATH, "w") as f:
            f.write(ticket_url)
    else:
        print("Failed to get ticket URL")

def u_cookie():
    global cookie
    while True:
        cookie = get_cookie(ticket_url)
        with open(COOKIE_PATH, "w") as f:
            f.write(cookie)
        if cookie:
            print("Cookie:", cookie)
            break

ids = [
    # ( "248E4D6B93A50548E0630C18F80AD971", ClassType.CROSS), # 污染控制微生物学
    ( "2580B3A200A64FA1E0630C18F80A1F9A", ClassType.COMPETITION)
]

def grab():
    global cookie, ids
    grabed = []
    while True:
        for i in range(len(ids)):
            id = ids[i][0]
            type = ids[i][1]
            if id in grabed:
                continue

            print("Grabbing class:", id)
            # u_cookie()
            msg = grab_class(id, cookie, type)
            if "操作成功" in msg['message']:
                print("Grabbed class:", id)
                grabed.append(id)

            if "该任务已选择" in msg['message']:
                print("Class already grabbed:", id)
                grabed.append(id)

            else:
                print(msg)

            sleep(2)

if __name__ == "__main__":
    # grab()
    # u_ticket()
    u_ticket()
    u_cookie()
    pass