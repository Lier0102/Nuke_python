import os # <-- 시스템 명령어를 쓸 일이 많음
from colorama import Fore # <-- 디자인(배경 X 글씨 O)
import requests # <-- 웹페이지에 요청을 보낼 때 헤더가 필요한데 얘가 좀 도움이 됨

from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

###### 버전 지정 ######

CUR_VERSION = 0.1

###### 버전 지정 ######

###### 색 지정 ######

w = Fore.WHITE
b = Fore.BLACK
lg = Fore.LIGHTGREEN_EX
ly = Fore.LIGHTYELLOW_EX
lm = Fore.LIGHTMAGENTA_EX
lc = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX

###### 색 지정 ######

tokencnt = len(open('token.txt').readlines()) # 토큰 갯수 카운팅

if os.name != "nt": # 맥은 내가 프로그램 만들 줄 몰라서 못하고 리눅스는 굳이..? 해서 윈도우로 필터링함.
    print("Sorry, Your OS cannot run this program.") # <-- 한국어 인코딩이 깨져서 영어로 집어넣음.
    exit(-1)

os.system("title PRESS ENTER TO START THIS PROGRAM") # 타이틀에 명령하기

def OKAYLIST(): # 우리 프로그램은 메인 화면에서 메뉴가 띄워진 다음에 
    os.system("cls")
    global responseList
    responseList = ['yes', 'y', 'yeah', 'yep', 'ok', 'okay', 'yee', 'ye', 'sure', 'good']

# 크롬 드라이버를 이용하여 다양한 기능 : ex) 오토로그인, Qr그래빙
# 에 쓸 것임.