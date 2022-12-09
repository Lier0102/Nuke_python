import requests

def remove_friend(token: str):
    base_url = "https://discord.com/api/v10/users/@me/relationships"
    
    headers = {
        'Authorization': token
    }
    
    response: list[dict] = requests.get(url=base_url, headers=headers).json() # type: ignore
    friend_ids: list[str] = [friend["id"] for friend in response] # type: ignore
    for friend_id in friend_ids:
        requests.delete(f"{base_url}/{friend_id}", headers=headers)
    


def accounts_bomber():
    with open("token.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            # 주석 처리된 문장 무시
            if line.startswith("#"):
                continue
            remove_friend(line)
            
remove_friend(token="MTA0ODg0OTQyNzE2MDM4NzY2NA.Gdkemr.D9zBGj8-bz5SQaGtIiDlo1BoFhDXBcgp1nXnEk")
