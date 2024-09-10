import requests
def net(d_name):
    try:
        response =  requests.get(d_name,timeout=5)
        print("[+] Connection Done !!!\n\n")
        return True
    except(requests.ConnectionError,requests.Timeout):
        return False

