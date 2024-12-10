import requests

from colorama import Fore,Style,init



init()

def url_vulnerable(url):
    with open("SQL_payload.txt","r") as file:
        result = file.readlines()

    for payloads in result:
        response = requests.get(url + payloads)

        print(Fore.GREEN + f" 🕵️ [+] Testing the Payload ==> {payloads}")
    

        try:
            if "SQL syntax" in response.text or "mysql" in response.text.lower() or "MYSQL" in response.text or "error" in response.text.lower():
                
                print(Fore.RED+ Style.BRIGHT+ f"[!] 👾 Possible of SQL Injection vulnerability Found ==> {url+payloads}")

                
                print(Fore.YELLOW+Style.BRIGHT + f"[+] payload => {payloads}")

            elif response.elapsed.total_seconds() > 5:

                print(Fore.RED + Style.BRIGHT+f"[!] 👾 Possible of TIME-BASEED SQL Injection vulnerability Found ==> {url+payloads}")
                

                print(Fore.YELLOW+Style.BRIGHT + f"[+] payload => {payloads}")

            elif "UNION SELECT" in response.text or "union select" in response.text and("column" in response.text or "row" in response.text):

                print(Fore.RED + Style.BRIGHT +f"[!] 👾 Possible of UNION-BASEED SQL Injection vulnerability Found ==> {url+payloads}")
                

                print(Fore.YELLOW+Style.BRIGHT + f"[+] payload => {payloads}")

            else:
                print(Fore.RED + Style.BRIGHT+f" ❌ [*] NO VULNERABILITY FOUND IN THE URL ==> {url+payloads}")
            
        except Exception as error:
            print(Fore.BLUE + "[-] Error testing payload: {payload} - {e}")
        
    



                

