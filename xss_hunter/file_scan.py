
import requests
import requests
from colorama import Fore, Style, init
import traceback


init(autoreset=True)

def file_scanner(f_name):
    with open(f_name,"r") as url_file:
        urls = [line.strip() for line in url_file]

    with open("xss_payload.txt","r") as payload_file:
        payloads = [line.strip() for line in payload_file]
    
    for url in urls:
        for payload in payloads:
            full_url = url+payload

            try:
                response = requests.get(full_url)
                print(Fore.GREEN + f"Testing the Payload ==> {payload}")
                
                if payload in response.text:
                    print(Fore.RED + Style.BRIGHT +f"XSS Vulnerability Found ==> {full_url}")
                else:
                    print(Fore.YELLOW+ Style.BRIGHT+f"[*] NO VULNERABILITY FOUND IN THE URL ==> {full_url}")

            except Exception as error:
                
                print(Fore.BLUE + Style.BRIGHT+f"[-] Error testing payload: {payload} - {error}")
                print(traceback.format_exc())
