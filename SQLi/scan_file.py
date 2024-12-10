import requests
from colorama import Fore, Style, init
from file import file_open  
import traceback




init(autoreset=True)

def file_name(f_name):



    with open(f_name, 'r') as url_file:
        urls = [line.strip() for line in url_file]

    with open("SQL_payload.txt", "r") as payload_file:
        result = [line.strip() for line in payload_file]

    for url in urls:
        for payloads in result:
            full_url = url + payloads
            try:
               
                response = requests.get(full_url)
                print(Fore.GREEN + f"Testing the Payload ==> {payloads}")

                
                if "SQL syntax" in response.text or "mysql" in response.text.lower() or "MYSQL" in response.text or "error" in response.text.lower():
                    print(Fore.RED +Style.BRIGHT+ f"[!] Possible SQL Injection vulnerability found ==> {full_url}")
                    print("\n")
                    print(Fore.YELLOW+ Style.BRIGHT+f"[+] Payload => {payloads}")

                elif response.elapsed.total_seconds() > 5:
                    print(Fore.RED + Style.BRIGHT+f"[!] Possible TIME-BASED SQL Injection vulnerability found ==> {full_url}")
                    print("\n")
                    print(Fore.YELLOW+ Style.BRIGHT+f"[+] Payload => {payloads}")

                elif "UNION SELECT" in response.text or "union select" in response.text and ("column" in response.text or "row" in response.text):
                    print(Fore.RED + Style.BRIGHT+f"[!] Possible UNION-BASED SQL Injection vulnerability found ==> {full_url}")
                    print("\n")
                    print(Fore.RED + Style.BRIGHT+f"[+] Payload => {payloads}")

                else:
                    print(Fore.YELLOW+ Style.BRIGHT+f"[*] NO VULNERABILITY FOUND IN THE URL ==> {full_url}")

            except Exception as error:
                print(Fore.BLUE + Style.BRIGHT+f"[-] Error testing payload: {payloads} - {error}")
                print(traceback.format_exc())

