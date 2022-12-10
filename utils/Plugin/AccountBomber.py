import os
import random
from colorama import Fore
import threading

def NUKER(token, Server, Content):
    if threading.active_count() < 50:
        thread = threading.Thread(target="", args=(token, ))