
import argparse
import url_scan
import file_scan
from colorama import Fore,init,Style
import pyfiglet

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", help="Add a single url ")
parser.add_argument("-f", "--file", help="Add set of url in .txt file format")
parser.add_argument("-a", "--author", action="store_true", help="Author Info")



args = parser.parse_args()

def main():

    name = pyfiglet.figlet_format("XSS Injector")
    cat_ascii = r"""
      /\     /\
     {  `---'  }
     {  O   O  }
     ~~>  V  <~~
      \  \|/  /
       `-----'____
       /     \    \_
      {       }\  )_\_   _
      |  \_/  |/ /  \_\_/ )
       \__/  /(_/     \__/
         (__/

        """

    print(Fore.RED + Style.BRIGHT+name)
    print(Fore.RED + Style.BRIGHT+f"                 {cat_ascii}")

    print(Fore.RED + Style.BRIGHT+"                 AUTHOR : @balajih4kr 💀   insta : @balajik4kr 📭   github: @balajih4kr 💻" )
    print("\n")

    if args.url:

        url_scan.url_scanner(args.url)
        print(Fore.RED + Style.BRIGHT+"Happy Hacking 💀")


    if args.file:

        file_scan.file_scanner(args.file)
        print(Fore.RED + Style.BRIGHT+"Happy Hacking 💀")
    
if __name__ == "__main__":
    main()
