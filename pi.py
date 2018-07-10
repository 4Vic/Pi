from urllib3 import *
from platform import system
from urllib.request import urlopen
import sys
import os

def pi():
    print("""\033[1;36m
                PPPPPPPPPPPPPPPPP     iiii        333333333333333             1111111       444444444  
                P::::::::::::::::P   i::::i      3:::::::::::::::33          1::::::1      4::::::::4  
                P::::::PPPPPP:::::P   iiii       3::::::33333::::::3        1:::::::1     4:::::::::4  
                PP:::::P     P:::::P             3333333     3:::::3        111:::::1    4::::44::::4  
                  P::::P     P:::::Piiiiiii                  3:::::3           1::::1   4::::4 4::::4  
                  P::::P     P:::::Pi:::::i                  3:::::3           1::::1  4::::4  4::::4  
                  P::::PPPPPP:::::P  i::::i          33333333:::::3            1::::1 4::::4   4::::4  
                  P:::::::::::::PP   i::::i          3:::::::::::3             1::::l4::::444444::::444
                  P::::PPPPPPPPP     i::::i          33333333:::::3            1::::l4::::::::::::::::4
                  P::::P             i::::i                  3:::::3           1::::l4444444444:::::444
                  P::::P             i::::i                  3:::::3           1::::l          4::::4  
                  P::::P             i::::i                  3:::::3           1::::l          4::::4  
                PP::::::PP          i::::::i     3333333     3:::::3        111::::::111       4::::4  
                P::::::::P          i::::::i     3::::::33333::::::3 ...... 1::::::::::1     44::::::44
                P::::::::P          i::::::i     3:::::::::::::::33  .::::. 1::::::::::1     4::::::::4
                PPPPPPPPPP          iiiiiiii      333333333333333    ...... 111111111111     4444444444
""")
                                                               
pi()
def mainpage():

    print(""" 

                1) Honeypot Detector
                2) DNS Lookup
                3) Port Scanner
                4) E-Mail Collector
                5) Traceroute
                6) Whois Lookup
                7) IP Lookup
                8) Reverse IP Lookup
                9) Subdomain Finder
                10) Find Share DNS Servers
                11) HTTP Header
                12) Robots.txt
                13) Host Finder
                14) Zone Transfer
                15) Subnet Lookup
                16) Extract Links
                17) Test ping
                18) Reverse DNS Lookup
                19) Exit


""")

mainpage()
def list():
    while True:
        
        choose = input("\033[1;36m Select Number  :")
        if choose == "19":
            print("\n","\033[1;32m See you later (づ｡◕‿‿◕｡)づ✿ ","\n")
            break

        elif choose == "1":  
            ipaddress = input("Enter the IP address  :")
            sh="https://api.shodan.io/labs/honeyscore/" + ipaddress + "?key=oxchYb8VrHJoYvLVRtid2reJa0TRStW8"
            openn = urlopen(sh).read().decode()
            print("\n","Honey Score :",openn)
            mainpage()
       
        elif choose == "2":
            ipaddress = input("Enter the IP address or hostname :")
            ht ="http://api.hackertarget.com/dnslookup/?q=" + ipaddress
            openn = urlopen(ht).read().decode()
            print(openn)
            mainpage()
            
        elif choose == "3":
            ipaddress = input("Enter the IP address or hostname :")
            ht = "http://api.hackertarget.com/nmap/?q=" + ipaddress
            openn = urlopen(ht).read().decode()
            print(openn)
            mainpage()
            
        elif choose == "4":
            ipaddress = input("Enter the hostname  :")
            harvest = os.getcwd()
            os.system('cd ' +  harvest  + '/modules && python2 theHarvester.py -d %s -b all' % ipaddress)
            mainpage()
            
        elif choose == "5":
            ipaddress = input("Enter the IP address or hostname  :")
            tra = "https://api.hackertarget.com/mtr/?q=" + ipaddress
            openn = urlopen(tra).read().decode()
            print (openn)
            mainpage()
            
        elif choose == "6":
            ipaddress = input("Enter the IP address or hostname  :")
            who = "http://api.hackertarget.com/whois/?q=" + ipaddress
            openn = urlopen(who).read().decode()
            print(openn)
            mainpage()
        
        elif choose == "7":
            ipaddress = input("Enter the IP address or hostname  :")
            ip = "http://ip-api.com/json/"  + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()
            
        elif choose == "8":
            ipaddress = input("Enter the IP address or hostname   :")
            ip = "http://api.hackertarget.com/reverseiplookup/?q=" + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()
               
        elif choose == "9":
            ipaddress = input("Enter the hostname  :")
            subdom = os.getcwd()
            os.system('cd ' +  subdom + '/modules && python2 sub.py -t %s -l fr ' % ipaddress)
            mainpage()
            
        elif choose == "10":
            ipaddress = input("Enter the IP address or hostname :")
            ip = "https://api.hackertarget.com/findshareddns/?q=ns1." + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()
        elif choose == "11":
            ipaddress = input("Enter the IP address or hostname :")
            ip = "http://api.hackertarget.com/httpheaders/?q=" + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()
            
        elif choose == "12":
            ipaddress = input("Enter the IP address or hostname :")
            robot = os.getcwd()
            os.system('cd ' +  robot  + '/modules && python2 goofile.py -d %s -f txt' % ipaddress)
            mainpage()
            
        elif choose == "13":
            ipaddress = input("Enter the IP address or hostname :")
            ip = "http://api.hackertarget.com/hostsearch/?q=" + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()
            
        elif choose == "14":
            ipaddress = input("Enter the IP address or hostname :")            
            ip = "http://api.hackertarget.com/zonetransfer/?q=" + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()
            
        elif choose == "15":
            ipaddress = input("Enter the IP address or hostname :")
            ip = "http://api.hackertarget.com/subnetcalc/?q=" + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()
        
        elif choose == "16":
            ipaddress = input("Enter the IP address or hostname :")
            ip = "https://api.hackertarget.com/pagelinks/?q=" + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()
            
        elif choose == "17":
            ipaddress = input("Enter the IP address or hostname :")
            ip = "https://api.hackertarget.com/nping/?q=" + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()

        elif choose == "18":
            ipaddress = input("Enter the IP address or hostname :")
            ip = "https://api.hackertarget.com/reversedns/?q=" + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()

        else:
            print("Invalid operation")
            mainpage()
list()






