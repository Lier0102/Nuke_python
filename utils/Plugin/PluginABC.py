from abc import ABC, abstractmethod

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
    @abstractmethod
    async def main(cls):
        ...
    