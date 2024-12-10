import argparse
import url
import author
import webbrowser
import scan_file
from colorama import Fore,Style,init
import pyfiglet


init()

parser = argparse.ArgumentParser()

parser.add_argument("-u","--url",help="Enter Url to Check")
parser.add_argument("-f","--file",help="Enter to url file   Foramt = eg..(file.txt)")
parser.add_argument("-a","--author",action='store_true',help="About Author")


args = parser.parse_args()

def main():
    name = pyfiglet.figlet_format("MYSQL Injector")
    skull_ascii = r"""
     ______
  .-        -.
 /            \\
|,  .-.  .-.  ,|
| )(_o/  \o_)( |
 |/     /\     \|
 (_     ^^     _)
  \__|IIIIII|__/
   | \\IIIIII/ |
   \          /
    `--------`
"""

    
    print(Fore.RED + Style.BRIGHT+name)
    print(Fore.RED + Style.BRIGHT+f"                 {skull_ascii}")
   
    print(Fore.RED + Style.BRIGHT+"                 AUTHOR : @balajih4kr 💀   insta : @balajik4kr 📭   github: @balajih4kr 💻" )
    print("\n")
    print(Fore.RED + Style.BRIGHT+"NOTE : U Want Good Internet Connection *(blind-sql)")
    if args.url:
        url.url_vulnerable(args.url)
        print(Fore.RED + Style.BRIGHT+"Task completed successfully! 📂")
        print("\n")
        print(Fore.RED + Style.BRIGHT+"Happy Hacking 💀")
    if args.author:
        webbrowser.open_new_tab(author.data.blog)
    if args.file:
        scan_file.file_name(args.file)
        print(Fore.RED + Style.BRIGHT+"Task completed successfully! 📂")
        print("\n")
        print(Fore.RED + Style.BRIGHT+"Happy Hacking 💀")


if __name__ == "__main__":
    main()
else:
    print(Fore.RED +Style.BRIGHT+"[!] Check your internet connection ")


