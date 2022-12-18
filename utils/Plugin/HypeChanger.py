from utils.Plugin.PluginABC import PluginABC
from utils.Setting.setup_most import heads
from colorama import Fore

class HypeChanger(PluginABC):
    plugin_name = "하이퍼스쿼드 변경"

    print(f'''\n[\x1b[95m1\x1b[95m\x1B[37m] {Fore.MAGENTA}용맹(Bravery){Fore.RESET}
[\x1b[95m2\x1b[95m\x1B[37m] {Fore.LIGHTRED_EX}찬란함(Brilliance){Fore.RESET}
[\x1b[95m3\x1b[95m\x1B[37m] {Fore.LIGHTCYAN_EX}균형(Balance){Fore.RESET}
[\x1b[95m4\x1b[95m\x1B[37m] 하이퍼스쿼드 나가기''')