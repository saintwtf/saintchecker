import os
import sys
import subprocess
import platform
import whois
from shutil import get_terminal_size

def clear_terminal():
    if os.name == 'nt':  
        _ = os.system('cls')
    else:  
        _ = os.system('clear')

def check_domain_availability(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        if domain_info.status == None:
            return True, None  
        else:
            return False, domain_info.registrar
    except whois.parser.PywhoisError:
        return False, None  

def display_header():
    header = """
  .dBBBBP dBBBBBb     dBP dBBBBb dBBBBBBP
  BP           BB            dBP         
  `BBBBb   dBP BB   dBP dBP dBP   dBP    
     dBP  dBP  BB  dBP dBP dBP   dBP     
dBBBBP'  dBBBBBBB dBP dBP dBP   dBP      
"""
    print(header)
    print("Made by @saintlf")

def main():
    clear_terminal()
    display_header()

    while True:
        print("\nPlease enter a domain name:", end=' ')
        width = get_terminal_size().columns - 22
        domain_name = input()[:width]

        if domain_name:
            available, owner = check_domain_availability(domain_name)
            if available:
                print(f"The domain {domain_name} is available! You can purchase it from domain registrars like GoDaddy, Namecheap, or Google Domains.")
            else:
                print(f"Sorry, the domain {domain_name} is already taken. It is owned by {owner}.")
        else:
            print("Please enter a domain name.")

        print()
        choice = input("Do you want to check another domain? (yes/no): ")
        if choice.lower() != 'yes':
            print("Restarting...")
            python_executable = sys.executable
            subprocess.Popen([python_executable, __file__, "--new-terminal"])
            sys.exit()

if __name__ == "__main__":
    main()
