# 필요한 모듈 인클루드 및 다운로드

import os

from selenium import webdriver
from PIL import Image
import base64
import json
import colorama
import random
import asyncio
import time
import aiohttp
import threading

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
os.system("mode 120,30")

url = "https://discord.com/api/v10/channels/messages"

tokens: list[str] = []
with open("token.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        # 주석 처리된 문장 무시
        if line.startswith("#"):
            continue
        tokens.append(line)


def Rstr(length: int):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ""
    for _ in range(0, length):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text


def mainHeader(token: str):
    return {
        "authorization": token,
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={Rstr(43)}; __dcfduid={Rstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 "
                      "Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": ("eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX"
                               "2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmV"
                               "yc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNr"
                               "IiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"),
    }


def secondHeader(token: str):
    return {
        ":authority": "discord.com",
        ":method": "PATCH",
        ":path": "/api/v9/users/@me",
        ":scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US",
        "authorization": token,
        "content-length": "124",
        "content-type": "application/json",
        "Cookie": f"__cfuid={Rstr(43)}; __dcfduid={Rstr(32)}; locale=en-US",
        "origin": "https://canary.discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.616 "
                      "Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": ("eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQ"
                               "iLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2l"
                               "vbiI6IjEuMC42MTYiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjQ1OCIsIm9z"
                               "X2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfY"
                               "nVpbGRfbnVtYmVyIjo5ODgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="),
    }
