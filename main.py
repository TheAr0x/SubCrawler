import time

import requests
from banner_printer import print_banner


def request(url):
    try:
        return requests.get("http://" + url, timeout=1.0)
    except:
        pass


print_banner()
print("Made with love by Ar0x\n")
target_url = input("Enter an URL (format : site.com) : ")

with open("./suddom_list.txt", 'r') as subdom_list:
    for line in subdom_list:
        word = line.strip()
        test_url = word + "." + target_url
        begin = time.time()
        response = request(test_url)
        stop = time.time()
        request_time = stop - begin
        if response:
            print("[+] Discovered subdomain --> http://" + test_url + " in " + str(round(request_time, 2)) + " seconds")
