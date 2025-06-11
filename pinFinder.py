import random
import requests
import os
import time
from datetime import datetime
from colorama import Back, Fore, Style, deinit, init

def kpin(pin):
    if requests.get("https://kahoot.it/reserve/session/" + pin, verify=True, timeout=5).status_code == 200:
        return True
    else:
        return False

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
wind = True    
while wind == True:
    clear()
    print("1 : Kahoot pin finder")
    print("X : Leave")
    mode = input("Pick a mode: ")
    if mode == "X" or "x":
        wind = False
        
    if mode == "1":
        c = 0
        clear()
        pin = ""
        while True:
            for i in range(random.randint(5,7)):
                if i == 0:
                    pin = str(random.randint(1,9))
                else:
                    pin += str(random.randint(0,9))
            if kpin(pin) == True:
                r = requests.get("https://kahoot.it/reserve/session/" + pin, verify=True, timeout=5).json()
                try:
                    startTime = r["startTime"]
                    if startTime > int(time.time_ns() / 1000000)-180000:
                        print(Fore.BLUE + Style.NORMAL + "https://kahoot.it/?pin=" + pin, datetime.fromtimestamp(startTime//1000).strftime('%Y-%m-%d %H:%M:%S'))
                    elif startTime > int(time.time_ns() / 1000000)-300000:
                        print(Fore.GREEN + Style.NORMAL + "https://kahoot.it/?pin="  + pin, datetime.fromtimestamp(startTime//1000).strftime('%Y-%m-%d %H:%M:%S'))
                    elif startTime > int(time.time_ns() / 1000000)-600000:
                        print(Fore.YELLOW + Style.NORMAL + "https://kahoot.it/?pin=" + pin, datetime.fromtimestamp(startTime//1000).strftime('%Y-%m-%d %H:%M:%S'))
                    elif startTime > int(time.time_ns() / 1000000)-1800000:
                        print(Fore.ORANGE + Style.NORMAL + "https://kahoot.it/?pin=" + pin, datetime.fromtimestamp(startTime//1000).strftime('%Y-%m-%d %H:%M:%S'))
                    else:
                        print(Fore.RED + Style.NORMAL + "https://kahoot.it/?pin="+ pin, datetime.fromtimestamp(startTime//1000).strftime('%Y-%m-%d %H:%M:%S'))
                        #print("#"+str(c), "aux")
                except Exception:
                    print("Error, skipping pin")
                
            
        
