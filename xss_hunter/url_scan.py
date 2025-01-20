from colorama import Fore,init,Style
import requests
import traceback

def url_scanner(url):

    with open("xss_payload.txt","r") as file:
        result = file.readlines()

        for payloads in result:
            full_url = url+payloads

            try:
                response = requests.get(full_url)
                print(Fore.GREEN + f"Testing the Payload ==> {payloads}")
                
                if payloads in response.text:
                    print(Fore.RED + Style.BRIGHT +f"XSS Vulnerability Found ==> {full_url}")
                else:
                    print(Fore.YELLOW+ Style.BRIGHT+f"[*] NO VULNERABILITY FOUND IN THE URL ==> {full_url}")

            except Exception as error:
                
                print(Fore.BLUE + Style.BRIGHT+f"[-] Error testing payload: {payloads} - {error}")
                print(traceback.format_exc())

