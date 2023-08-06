import requests


def request(url):
    try:
        return requests.get("http://" + url, timeout=1.0)
    except:
        pass


target_url = "google.com"

with open("./suddom_list.txt", 'r') as subdom_list:
    for line in subdom_list:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain --> http://" + test_url)
