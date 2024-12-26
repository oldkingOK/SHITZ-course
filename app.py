from get_ticket import get_ticket_url
from get_cookie import get_cookie
from grab import grab_class

ticket_url = ""
cookie = ""

def ticket():
    global ticket_url
    ticket_url = get_ticket_url()
    if ticket_url:
        print("Ticket URL:", ticket_url)
    else:
        print("Failed to get ticket URL")

def cookie():
    global cookie
    while True:
        cookie = get_cookie(ticket_url)
        if cookie:
            print("Cookie:", cookie)
            break

ids = [
    "2922FE7D81D6929AE0630B18F80A71EA"
]

def grab():
    global cookie
    for id in ids:
        print("Grabbing class:", id)
        grab_class(id, cookie)