from abc import ABC, abstractmethod
from colorama import Fore

class PluginABC(ABC):
    plugin_name: str
    
    @classmethod
    def get_option(cls):
        print("\n")
        print(f"[\x1b[95m1\x1b[95m\x1B[37m] {cls.plugin_name}")
        print("[\x1b[95m2\x1b[95m\x1B[37m] 나가기")
        
        option = int(input(f"[\x1b[95m>\x1b[95m\x1B[37m] 옵션: "))
        return option
    
    @classmethod
    def getHype_option():
        print(f'''\n[\x1b[95m1\x1b[95m\x1B[37m] {Fore.MAGENTA}용맹(Bravery){Fore.RESET}
[\x1b[95m2\x1b[95m\x1B[37m] {Fore.LIGHTRED_EX}찬란함(Brilliance){Fore.RESET}
[\x1b[95m3\x1b[95m\x1B[37m] {Fore.LIGHTCYAN_EX}균형(Balance){Fore.RESET}
[\x1b[95m4\x1b[95m\x1B[37m] 하이퍼스쿼드 나가기''')
        
    
    @classmethod
    @abstractmethod
    async def main(cls):
        ...
    