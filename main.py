import os
import sys
import subprocess
import whois
import colorama
from colorama import Fore, Style

colorama.init()

def clear_terminal():
    if os.name == 'nt':  
        _ = os.system('cls')
    else:  
        _ = os.system('clear')

def check_domain_availability(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        if domain_info.status == None:
            return True  
        else:
            return False  
    except whois.parser.PywhoisError:
        return False  

def display_header():
    header = """
  .dBBBBP dBBBBBb     dBP dBBBBb dBBBBBBP
  BP           BB            dBP         
  `BBBBb   dBP BB   dBP dBP dBP   dBP    
     dBP  dBP  BB  dBP dBP dBP   dBP     
dBBBBP'  dBBBBBBB dBP dBP dBP   dBP      
"""
    print(Fore.RED + header + Style.RESET_ALL)
    print(Fore.RED + "Made by @saintlf" + Style.RESET_ALL)

def main():
    clear_terminal()
    display_header()

    if len(sys.argv) > 1 and sys.argv[1] == "--new-terminal":
        while True:
            domain_name = input("Enter a domain name to check its availability: ")

            if domain_name:
                if check_domain_availability(domain_name):
                    print(Fore.RED + f"The domain {domain_name} is available!" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"Sorry, the domain {domain_name} is already taken or invalid." + Style.RESET_ALL)
            else:
                print(Fore.RED + "Please enter a domain name." + Style.RESET_ALL)

            choice = input("Do you want to check another domain? (yes/no): ")
            if choice.lower() != 'yes':
                break
    else:
        subprocess.Popen([sys.executable, os.path.abspath(__file__), "--new-terminal"])
        sys.exit()

if __name__ == "__main__":
    main()
