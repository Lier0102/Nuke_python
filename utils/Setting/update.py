import os
import re
import sys
import shutil
import requests
from time import sleep
from colorama import Fore
from zipfile import ZipFile
from bs4 import BeautifulSoup

from utils.Setting.setup_most import *

w = Fore.WHITE
b = Fore.BLACK
lg = Fore.LIGHTGREEN_EX
ly = Fore.LIGHTYELLOW_EX
lm = Fore.LIGHTMAGENTA_EX
lc = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX

def update():
    clear()

    setTitle("")

    r = requests.get("https://github.com/Lier0102/Nuke_python/releases/latest")

    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]

    if CUR_VERSION not in result_string:
        Write.Print("\n\n\n           █    ██  ██▓███  ▓█████▄  ▄▄▄     ▄▄▄█████▓▓█████  ▐██▌ \n", Colors.red_to_white, interval=0.000)
        Write.Print("          ██   ▓██▒▓██░  ██▒▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒▓█   ▀  ▐██▌ \n", Colors.red_to_white, interval=0.000)
        Write.Print("          ▓██  ▒██░▓██░ ██▓▒░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░▒███    ▐██▌  \n", Colors.red_to_white, interval=0.000)
        Write.Print("          ▓▓█  ░██░▒██▄█▓▒ ▒░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄  ▓██▒  \n", Colors.red_to_white, interval=0.000)
        Write.Print("          ▒▒█████▓ ▒██▒ ░  ░░▒████▓  ▓█   ▓██▒ ▒██▒ ░ ░▒████▒ ▒▄▄   \n", Colors.red_to_white, interval=0.000)
        Write.Print("          ░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░ ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░ ░▀▀▒  \n", Colors.red_to_white, interval=0.000)
        Write.Print("          ░░▒░ ░ ░ ░▒ ░      ░ ▒  ▒   ▒   ▒▒ ░   ░     ░ ░  ░ ░  ░  \n", Colors.red_to_white, interval=0.000)
        Write.Print("           ░░░ ░ ░ ░░        ░ ░  ░   ░   ▒    ░         ░       ░  \n", Colors.red_to_white, interval=0.000)
        Write.Print("             ░                 ░          ░  ░           ░  ░ ░      \n", Colors.red_to_white, interval=0.000)
        Write.Print("                              ░                                       \n", Colors.red_to_white, interval=0.000)
        print(f'''\n\n                               [{lr}!{w}] [{lm}현재 소유하고 계신 버전{w}]이 구버전입니다! 업데이트 할까요?''')
        soup = BeautifulSoup(requests.get("https://github.com/Lier0102/Nuke_Python/releases").text, 'html.parser')
        for link in soup.find_all('a'):
            if "releases/download" in str(link):
                update_url = f"https://github.com/{link.get('href')}"
        
        choice = input(f'                               [\x1b[95m#\x1b[95m\x1B[37m] (ㅇㅇ/ㄴㄴ)?: ')

        if choice.lower() == 'y' or choice == 'ㅇㅇ' or choice.lower() in responseList:
            print(f"\n                               [{lg}#{w}] Hydron_Nuker를 업뎃 중..")

            if os.path.basename(sys.argv[0]).endswith("exe"):
                with open("Hydron_Nuker.zip", 'wb')as zipfile:
                    zipfile.write(requests.get(update_url).content)
                with ZipFile("Hydron_Nuker.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("Hydron_Nuker.zip")
                cwd = os.getcwd()+'\\Hydron_Nuker\\'
                shutil.copyfile(cwd+'README.md', 'README.md')                   
                shutil.rmtree('Hydron-Nuker')
                input(f"                               [{lg}#{w}] 업뎃이 성공적으로 끝났습니다!", end="")
                os.startfile("main_start.bat")
                os._exit(0)

            else:
                new_version_source = requests.get("https://github.com/Lier0102/Nuke_Python/archive/refs/heads/main.zip")
                with open("Nuke_Python-main.zip", 'wb')as zipfile:
                    zipfile.write(new_version_source.content)
                with ZipFile("Nuke_Python-main.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("Nuke_Python-main.zip")
                cwd = os.getcwd()+'\\Nuke_Python-main'
                shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
                shutil.rmtree(cwd)
                input(f"                               [{lg}!{w}] 업뎃이 성공적으로 끝났습니다!")
                print(f'                               [{lg}#{w}] 엔터 키를 눌러서 업데이트를 확인하세요!')
                if os.path.exists(os.getcwd()+'check_env.bat'):
                    os.startfile("check_env.bat")
                elif os.path.exists(os.getcwd()+'main_start.bat'):
                    os.startfile("main_start.bat")
                os._exit(0)