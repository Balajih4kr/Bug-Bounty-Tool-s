#!/bin/bash

# Check if figlet is installed
if ! command -v figlet &> /dev/null; then
    echo "[!] Figlet is not installed. Install it using: sudo apt install figlet"
    exit 1
fi

# Colors for figlet and output
GREEN="\033[1;32m"
CYAN="\033[1;36m"
NC="\033[0m" # No Color

# Display tool name in ASCII art with color
echo -e "${CYAN}"
figlet -c "BALAJIH4KR"
echo -e "${GREEN}Recon Tool${NC}"

# Colors for script output
BLUE="\033[0;34m"
RED="\033[0;31m"

# Check if required tools are installed
check_tool() {
    if ! command -v "$1" &> /dev/null; then
        echo -e "${RED}[!] $1 is not installed. Please install it before running this script.${NC}"
        exit 1
    fi
}

# Check if ParamSpider is installed
check_paramspider() {
    if [ ! -d "$HOME/tools/ParamSpider" ]; then
        echo -e "${RED}[!] ParamSpider is not installed. Please install it using:${NC}"
        echo -e "    git clone https://github.com/devanshbatham/ParamSpider.git"
        echo -e "    cd ParamSpider && pip install -r requirements.txt"
        exit 1
    fi
}

# Ensure required tools are installed
TOOLS=("amass" "sublist3r" "assetfinder" "findomain" "curl" "waybackurls" "gau" "httprobe" "whatweb" "nmap" "jq")
for tool in "${TOOLS[@]}"; do
    check_tool "$tool"
done
check_paramspider

# Usage
usage() {
    echo -e "${GREEN}Usage: $0 -d <domain>${NC}"
    exit 1
}

# Parse command-line options
while getopts "d:" opt; do
    case "$opt" in
        d) DOMAIN=$OPTARG ;;
        *) usage ;;
    esac
done

if [ -z "$DOMAIN" ]; then
    usage
fi

# Create output directory
OUTPUT_DIR="recon-$DOMAIN"
mkdir -p "$OUTPUT_DIR"
echo -e "${BLUE}[+] Output will be saved to $OUTPUT_DIR${NC}"

# Reconnaissance steps

# 1. Amass
echo -e "${GREEN}[+] Running Amass...${NC}"
amass enum -passive -d "$DOMAIN" > "$OUTPUT_DIR/amass.txt"


# 3. Assetfinder
echo -e "${GREEN}[+] Running Assetfinder...${NC}"
assetfinder --subs-only "$DOMAIN" > "$OUTPUT_DIR/assetfinder.txt"

# 4. Findomain
echo -e "${GREEN}[+] Running Findomain...${NC}"
findomain -t "$DOMAIN" -u "$OUTPUT_DIR/findomain.txt"

# 5. crt.sh
echo -e "${GREEN}[+] Querying crt.sh...${NC}"
curl -s "https://crt.sh/?q=%.$DOMAIN&output=json" | jq -r '.[].name_value' | sort -u > "$OUTPUT_DIR/crtsh.txt"

# 6. Wayback URLs
echo -e "${GREEN}[+] Fetching Wayback URLs...${NC}"
echo "$DOMAIN" | waybackurls > "$OUTPUT_DIR/waybackurls.txt"

# 7. gau (Get All URLs)
echo -e "${GREEN}[+] Running gau...${NC}"
echo "$DOMAIN" | gau > "$OUTPUT_DIR/gau.txt"

# 8. Tools by BALAJIh4kr
echo -e "${GREEN}[+] Running BALAJIh4kr...${NC}"
cd "$HOME/tools/"
python3 param_crawl.py "$DOMAIN" -o "$HOME/tools/$OUTPUT_DIR/raw_url.txt"

# 8.1 =>

echo -e "${GREEN}[+] Running BALAJIh4kr (sqli.txt)...${NC}"
cd "$HOME/tools/"
python3 value_rem.py "$HOME/tools/$OUTPUT_DIR/raw_url.txt" "$HOME/tools/$OUTPUT_DIR/sqli.txt"
sort -u "$HOME/tools/$OUTPUT_DIR/sqli.txt" > "$HOME/tools/$OUTPUT_DIR/sql_injection.txt"
# 9. httprobe
echo -e "${GREEN}[+] Probing for live domains...${NC}"
cat "$HOME/tools/$OUTPUT_DIR/amass.txt" "$HOME/tools/$OUTPUT_DIR/assetfinder.txt" "$HOME/tools/$OUTPUT_DIR/findomain.txt" | sort -u | httprobe > "$HOME/tools/$OUTPUT_DIR/live_domains.txt"

# 10. WhatWeb
echo -e "${GREEN}[+] Running WhatWeb...${NC}"
while read -r domain; do
    whatweb "$domain" >> "$HOME/tools/$OUTPUT_DIR/whatweb.txt"
done < "$HOME/tools/$OUTPUT_DIR/live_domains.txt"

# Done
echo -e "${CYAN}[+] Recon complete! Results saved in $OUTPUT_DIR${NC}"
