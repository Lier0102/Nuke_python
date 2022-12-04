import requests


def get_servers(token: str):
    base_url = "https://discord.com/api/v9"
    headers = {
        'Authorization': token
    }
    servers = requests.get(f"{base_url}/users/@me/guilds", headers=headers).json()

    server_infos = []
    params = {
        "with_counts": True
    }
    for server in servers:
        server_info = requests.get(f"{base_url}/guilds/{server['id']}", headers=headers, params=params).json()
        server_infos.append(server_info)

    return server_infos
