#!/bin/bash

DIR_NAME="$1"
DOMAIN="$2"
TOOL_DIR="$3"




if [ -d "$DIR_NAME" ]; then
  echo "[!] Directory $DIR_NAME already exists. Exiting."
  exit 1
else
  echo "[+] Creating new Directory for Recon ==> $DIR_NAME"
  mkdir "$DIR_NAME"
fi

# Amass for subdomain enumeration
echo "[+] Running Amass for subdomain enumeration"
amass enum -active -d "$DOMAIN" >> ~/"$DIR_NAME"/subdomain.txt
echo "[+] Amass completed and output saved to ${DIR_NAME}/subdomain.txt"



# Sublist3r for subdomain enumeration
echo "[+] Running Sublist3r..."
if [ -d "$TOOL_DIR/Sublist3r" ]; then
    cd "$TOOL_DIR/Sublist3r"
    python3 sublist3r.py -d "$DOMAIN" -t 30 -b -o ~/"$DIR_NAME"/subdomain.txt
    cd -
    echo "[+] Sublist3r completed."
else
    echo "[-] Sublist3r directory not found!"
fi

# Add Go binaries to PATH
echo "[+] Adding Go binaries to PATH"
export PATH=$PATH:$(go env GOPATH)/bin
source ~/.bashrc

# Assetfinder for subdomain enumeration
echo "[+] Running Assetfinder..."
assetfinder "$DOMAIN" >> ~/"$DIR_NAME"/subdomain.txt
echo "[+] Assetfinder completed."

# Findomain for subdomain enumeration
echo "[+] Running Findomain..."
if [ -d "$TOOL_DIR/findomain" ]; then
    cd "$TOOL_DIR/findomain"
    cargo build --release
    sudo mv target/release/findomain /usr/bin/
    findomain -t "$DOMAIN" >> ~/"$DIR_NAME"/subdomain.txt
    cd -
    echo "[+] Findomain completed."
else
    echo "[-] Findomain directory not found!"
fi

# Query crt.sh for certificates
echo "[+] Querying crt.sh for certificates..."
curl -s "https://crt.sh/?q=$DOMAIN&output=json" | jq -r '.[].name_value' >> ~/"$DIR_NAME"/subdomain.txt
echo "[+] crt.sh results saved."

# DNSenum for DNS enumeration
echo "[+] Running DNSenum..."
dnsenum --enum "$DOMAIN" -o ~/"$DIR_NAME"/dnsenum.xml
echo "[+] DNSenum completed."

# DNScan for DNS-based discovery
echo "[+] Running DNScan..."
if [ -d "$TOOL_DIR/dnscan" ]; then
    cd "$TOOL_DIR/dnscan"
    python3 dnscan.py -d "$DOMAIN" -o ~/"$DIR_NAME"/dnscan.txt
    cd -
    echo "[+] DNScan completed."
else
    echo "[-] DNScan directory not found!"
fi

# Nmap scan
echo "[+] Running Nmap scan..."
nmap "$DOMAIN" > ~/"$DIR_NAME"/nmap.txt
echo "[+] Nmap scan completed."

# Waybackurls for extracting archived URLs
echo "[+] Running Waybackurls..."
echo "$DOMAIN" | waybackurls > ~/"$DIR_NAME"/urls.txt
echo "[+] Waybackurls completed."

# Running Dirsearch for directory brute-forcing
echo "[+] Running Dirsearch..."
if [ -d "$TOOL_DIR/dirsearch" ]; then
    cd "$TOOL_DIR/dirsearch"
    python3 dirsearch.py -u "$DOMAIN" -e php,html,js -o ~/"$DIR_NAME"/dirsearch.txt
    cd -
    echo "[+] Dirsearch completed."
else
    echo "[-] Dirsearch directory not found!"
fi

# Running Gobuster for directory enumeration
echo "[+] Running Gobuster..."
gobuster dir -u "$DOMAIN" -w /usr/share/wordlists/dirb/common.txt -o ~/"$DIR_NAME"/gobuster.txt
echo "[+] Gobuster completed."

# Running EyeWitness for screenshots
echo "[+] Running EyeWitness..."
if [ -d "$TOOL_DIR/EyeWitness/Python" ]; then
    cd "$TOOL_DIR/EyeWitness/Python"
    ./setup/setup.sh
    python3 EyeWitness.py --web -f ~/"$DIR_NAME"/urls.txt -d ~/"$DIR_NAME"/scr/
    cd -
    echo "[+] EyeWitness completed."
else
    echo "[-] EyeWitness directory not found!"
fi

echo "[+] Recon automation completed."
