import webbrowser
import file
import argparse
import about
import check_net
import scan
from check_net import net
import scan_f

parse = argparse.ArgumentParser()
parse.add_argument("-u","--url",help="Enter url")
parse.add_argument("-l","--list",help="list the file")
parse.add_argument("-a","--author",action='store_true',help="About Author")
parse.add_argument("-d","--domain",help="Enter the domain you want to check ?")
parse.add_argument("-f","--file",help="Enter file name")

args = parse.parse_args()

def main():
    if args.url:
        scan.vuln_check(args.url)
    if args.list:
        file.reader_file(args.list)
    if args.author:
        webbrowser.open_new_tab(about.data.blog)
    if args.file:
        scan_f.vuln_file(args.file)
    



if __name__ == "__main__":
    if check_net.net(args.domain):
        main()
    else:
        print("[!] Check your Internet ")


