import requests
import subprocess
def net(d_name):
    #subprocess.call(['sudo','apt','install','figlet'])
    subprocess.call(['figlet','etc / passwd'])
    print("\n")
    print("                                                     => BALAJI A    \n")
    print("checking Connection [!]......")

    try:
        response =  requests.get(d_name,timeout=5)

        print("\n")

        print("\n")
        print("[+] Connection Done !!!\n\n")
        return True
    except(requests.ConnectionError,requests.Timeout):
        return False



