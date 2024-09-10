import requests

import file

def vuln_check(v_url):
    file = open('s.txt','r')
    read_result = file.readlines()
    
    
    for payloads in read_result:
        response = v_url + payloads
        result = requests.get(response)
    try:    
        if result.status_code == 200 and "root:x" in result.text:
            print(f"[!] Vulnerable URL Found :====>{v_url}{payloads}")

        else:
            print(f"[-] No Vulnerable Found at: ==> {v_url}{payloads}")
    except requests.exceptions.RequestException as e:
                print(f"[!] Error accessing {v_url}{payloads}: {e}")        
    




