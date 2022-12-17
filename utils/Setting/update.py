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

    os.system("pause")