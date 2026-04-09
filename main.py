import platform
pcname = platform.node()
from pystyle import Colors, Colorate
import os
os.system(f"title Made with ❤️ - {pcname}")
import itertools, sys
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore
from colorist import ColorHex as h
from datetime import datetime
from os.path import isfile, join
import base64
import requests
import json
import random
import string
import threading
import time
import tls_client
import uuid
import websocket
import logging
import sys
import time
import os
import ctypes

session = tls_client.Session(
            client_identifier="chrome_112",
            random_tls_extension_order=True
        )



def get_random_str(length):
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def Clear():
    os.system("cls")

def wrapper(func):
    def wrapper(*args, **kwargs):
        Clear()
        console.render_ascii()
        result = func(*args, **kwargs)
        return result
    return wrapper

def title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

C = {
    "green": h("#65fb07"),
    "red": h("#Fb0707"),
    "yellow": h("#FFCD00"),
    "magenta": h("#b207f5"),
    "blue": h("#00aaff"),
    "cyan": h("#aaffff"),
    "gray": h("#8a837e"),
    "white": h("#DCDCDC"),
    "pink": h("#c203fc"),
    "light_blue": h("#07f0ec"),
    "brown": h("#8B4513"),
    "black": h("#000000"),
    "aqua": h("#00CED1"),
    "purple": h("#800080"),
    "lime": h("#00FF00"),
    "orange": h("#FFA500"),
    "indigo": h("#4B0082"),
    "violet": h("#EE82EE"),
    "gold": h("#FFD700"),
    "silver": h("#C0C0C0"),
    "teal": h("#008080"),
    "navy": h("#000080"),
    "olive": h("#808000"),
    "maroon": h("#800000"),
    "coral": h("#FF7F50"),
    "salmon": h("#FA8072"),
    "khaki": h("#F0E68C"),
    "orchid": h("#DA70D6")
}

class Files:
    @staticmethod
    def write_config():
        try:
            if not os.path.exists("config.json"):
                data = {
                    "Proxies": False,
                    "Theme": "pink", 
                }
                with open("config.json", "w") as f:
                    json.dump(data, f, indent=4)
        except Exception as e:
            console.log("FAILED", C["red"], "Failed to Write Config", e)

    @staticmethod
    def write_folders():
        folders = ["data", "scraped"]
        for folder in folders:
            try:
                if not os.path.exists(folder):
                    os.mkdir(folder)
            except Exception as e:
                console.log("FAILED", C["red"], "Failed to Write Folders", e)

    @staticmethod
    def write_files():
        files = ["tokens.txt", "proxies.txt"]
        for file in files:
            try:
                if not os.path.exists(file):
                    with open(f"data/{file}", "a") as f:
                        f.close()
            except Exception as e:
                console.log("FAILED", C["red"], "Failed to Write Files", e)

    @staticmethod
    def run_tasks():
        tasks = [Files.write_config, Files.write_folders, Files.write_files]
        for task in tasks:
            task()

Files.run_tasks()

with open("data/proxies.txt") as f:
    proxies = f.read().splitlines()

with open("config.json") as f:
    Config = json.load(f)

with open("data/tokens.txt", "r") as f:
    tokens = f.read().splitlines()

proxy = Config["Proxies"]
color = Config["Theme"]

def change_proxy():
    while True:
        selected_proxy = random.choice(proxies)
        session.proxies = {
            "http": f"http://{selected_proxy}", 
            "https": f"http://{selected_proxy}"
        }
        time.sleep(5)

if proxy:
    proxy_thread = threading.Thread(target=change_proxy, daemon=True)
    proxy_thread.start()

class Render:
    def __init__(self):
        self.size = os.get_terminal_size().columns
        if not color:
            self.background = C['black']
        else:
            self.background = C[color]

    def render_ascii(self):

        os.system(f"title Made with ❤️ - {pcname}")
        Clear()
        edges = ["╗", "║", "╚", "╝", "═", "╔"]
        title = f"""     


"""
        for edge in edges:
            title = title.replace(edge, f"{self.background}{edge}{C['white']}")
        print(title)

    def raider_options(self):
        text = """
1. Joiner           11. Token Online
2. Leaver           12. Vc Spammer
3. Channel spam     13. Nick Name Change
4. Token Checker    14. Threads Spam
5. Reaction press   15. Friend Adder
6. Soundboard       16. Onboard Bypass
7. token formater   17. Inviter
8. Button bypass    18. All Spam
9. Rule Bypass      19. Random Vc
10. Bio Changer     20. Pronoun Changer 21.Poll Spam        22.Mass Report      23.Exit
              Dev: fir3t_blood """
        gradient_text = Colorate.Vertical(Colors.red_to_blue, text)
        print(gradient_text) 

    def run(self):
        options = [self.render_ascii(), self.raider_options()]
        ([option] for option in options)

    def log(self, text=None, color=None, token=None, log=None):
        response = f"{Fore.RESET}{datetime.now().strftime(f'{Fore.LIGHTBLACK_EX}%H:%M:%S{Fore.RESET}')} "
        if text:
            response += f"{color}{text}{C['white']} "
        if token:
            response += token
        if log:
            response += f" ~ {C['gray']}{log}{C['white']}"
        print(response)

    def prompt(self, text, ask=None):
        response = f"{C['white']}{text}{C['white']}"
        if ask:
            response += f" {C['gray']}(y/n){C['white']}  "
        else:
            response += f"  "
        return response

console = Render()

def fmt():
    with open("data/tokens.txt", "r") as f:
        tokens = f.read().splitlines()
    try:
        formatted = []
        for token in tokens:
            token = token.strip()
            if token:
                tokens_split = token.split(":")
                if len(tokens_split) >= 3:
                    formatted_token = tokens_split[2]
                    formatted.append(formatted_token)
                else:
                    formatted.append(token)
        console.log("SUCCESS", C["green"], f"Formatted {len(formatted)} tokens")
        with open("data/tokens.txt", "w") as f:
            for token in formatted:
                f.write(f"{token}\n")
        time.sleep(1.5)
        Clear()
        Files.run_tasks()

    except Exception as e:
        console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", e)

class Utils:
    @staticmethod
    def range_corrector(ranges):
        if [0, 99] not in ranges:
            ranges.insert(0, [0, 99])
        return ranges

    @staticmethod
    def get_ranges(index, multiplier, member_count):
        initial_num = int(index * multiplier)
        ranges = [[initial_num, initial_num + 99]]
        if member_count > initial_num + 99:
            ranges.append([initial_num + 100, initial_num + 199])
        return Utils.range_corrector(ranges)

    @staticmethod
    def parse_member_list_update(response):
        data = response["d"]
        member_data = {
            "online_count": data["online_count"],
            "member_count": data["member_count"],
            "id": data["id"],
            "guild_id": data["guild_id"],
            "hoisted_roles": data["groups"],
            "types": [op["op"] for op in data["ops"]],
            "locations": [],
            "updates": [],
        }

        for chunk in data["ops"]:
            op_type = chunk["op"]
            if op_type in {"SYNC", "INVALIDATE"}:
                member_data["locations"].append(chunk["range"])
                member_data["updates"].append(chunk["items"] if op_type == "SYNC" else [])
            elif op_type in {"INSERT", "UPDATE", "DELETE"}:
                member_data["locations"].append(chunk["index"])
                member_data["updates"].append(chunk["item"] if op_type != "DELETE" else [])

        return member_data


class DiscordSocket(websocket.WebSocketApp):
    def __init__(self, token, guild_id, channel_id):
        self.token = token
        self.guild_id = guild_id
        self.channel_id = channel_id
        self.blacklisted_ids = {"1100342265303547924", "1190052987477958806", "833007032000446505", "1287914810821836843", "1273658880039190581", "1308012310396407828"}

        headers = {
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        }

        super().__init__(
            "wss://gateway.discord.gg/?encoding=json&v=9",
            header=headers,
            on_open=self.on_open,
            on_message=self.on_message,
            on_close=self.on_close,
        )

        self.end_scraping = False
        self.guilds = {}
        self.members = {}
        self.ranges = [[0, 0]]
        self.last_range = 0
        self.packets_recv = 0

    def run(self):
        self.run_forever()
        return self.members

    def scrape_users(self):
        if not self.end_scraping:
            self.send(json.dumps({
                "op": 14,
                "d": {
                    "guild_id": self.guild_id,
                    "typing": True,
                    "activities": True,
                    "threads": True,
                    "channels": {self.channel_id: self.ranges}
                }
            }))

    def on_open(self, ws):
        self.send(json.dumps({
            "op": 2,
            "d": {
                "token": self.token,
                "capabilities": 125,
                "properties": {
                    "os": "Windows",
                    "browser": "Chrome",
                    "device": "",
                    "system_locale": "it-IT",
                    "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
                    "browser_version": "131.0.0.0",
                    "os_version": "10",
                    "referrer": "",
                    "referring_domain": "",
                    "referrer_current": "",
                    "referring_domain_current": "",
                    "release_channel": "stable",
                    "client_build_number": 355624,
                    "client_event_source": None
                },
                "presence": {
                    "status": "online",
                    "since": 0,
                    "activities": [],
                    "afk": False
                },
                "compress": False,
                "client_state": {
                    "guild_hashes": {},
                    "highest_last_message_id": "0",
                    "read_state_version": 0,
                    "user_guild_settings_version": -1,
                    "user_settings_version": -1
                }
            }
        }))

    def heartbeat_thread(self, interval):
        while not self.end_scraping:
            self.send(json.dumps({"op": 1, "d": self.packets_recv}))
            time.sleep(interval)

    def on_message(self, ws, message):
        decoded = json.loads(message)
        if not decoded:
            return

        if decoded["op"] != 11:
            self.packets_recv += 1

        if decoded["op"] == 10:
            threading.Thread(
                target=self.heartbeat_thread,
                args=(decoded["d"]["heartbeat_interval"] / 1000,),
                daemon=True,
            ).start()

        if decoded["t"] == "READY":
            self.guilds.update({guild["id"]: {"member_count": guild["member_count"]} for guild in decoded["d"]["guilds"]})

        if decoded["t"] == "READY_SUPPLEMENTAL":
            self.ranges = Utils.get_ranges(0, 100, self.guilds[self.guild_id]["member_count"])
            self.scrape_users()

        elif decoded["t"] == "GUILD_MEMBER_LIST_UPDATE":
            parsed = Utils.parse_member_list_update(decoded)
            if parsed["guild_id"] == self.guild_id:
                self.process_updates(parsed)

    def process_updates(self, parsed):
        if "SYNC" in parsed["types"] or "UPDATE" in parsed["types"]:
            for i, update_type in enumerate(parsed["types"]):
                if update_type == "SYNC":
                    if not parsed["updates"][i]:
                        self.end_scraping = True
                        break
                    self.process_members(parsed["updates"][i])
                elif update_type == "UPDATE":
                    self.process_members(parsed["updates"][i])

                self.last_range += 1
                self.ranges = Utils.get_ranges(self.last_range, 100, self.guilds[self.guild_id]["member_count"])
                time.sleep(0.65)
                self.scrape_users()

        if self.end_scraping:
            self.close()

    def process_members(self, updates):
        for item in updates:
            if "member" in item:
                member = item["member"]
                user_id = member["user"]["id"]
                if user_id not in self.blacklisted_ids and not member["user"].get("bot"):
                    user_info = {
                        "tag": f"{member['user']['username']}#{member['user']['discriminator']}",
                        "id": user_id,
                    }
                    self.members[user_id] = user_info

    def on_close(self, ws, close_code, close_msg):
        console.log("Success", C["green"], False, f"scraped {len(self.members)} members")


def scrape(token, guild_id, channel_id):
    sb = DiscordSocket(token, guild_id, channel_id)
    return sb.run()

class Raider:
    def __init__(self):
        self.cookies = self.get_cookies()
        self.props = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6Iml0LUlUIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWrbykgQ2hyb21lLzExMi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEyLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE5MzkwNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=="
        self.ws = websocket.WebSocket()

    def headers(self, token):
        return {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-GB',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6Iml0LUlUIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEyLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE5MzkwNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
        }

    def nonce(self):
        return str((int(time.mktime(datetime.now().timetuple())) * 1000 - 1704067200000) * 4194304)

    def soundboard_sounds(self, token):
        return session.get("https://discord.com/api/v9/soundboard-default-sounds", headers=self.headers(token)).json()

    def ran_str(self):
        return ''.join(random.sample(string.ascii_lowercase + string.digits, 16))

    def get_cookies(self):
        cookies = {}
        try:
          response = session.get('https://discord.com')
          for cookie in response.cookies:
            if cookie.name.startswith('__') and cookie.name.endswith('uid'):
                cookies[cookie.name] = cookie.value
          return cookies

        except Exception as e:
          print('Failed to obtain cookies ({})'.format(e))
          return cookies

    def joiner(self, token, invite):
        try:
            payload = {
                'session_id': self.ran_str()
            }

            response = session.post(
                url=f'https://discord.com/api/v9/invites/{invite}',
                headers=self.headers(token),
                json=payload,
                cookies=self.get_cookies(),
            )
            match response.status_code:
                case 200:
                    console.log(f"JOINED", C["green"], f"{Fore.RESET}{token[:25]}...", f"{response.json()['guild']['name']} - {response.json()['guild']['id']}")
                case 400:
                    console.log("CAPTCHA", C["yellow"], f"{Fore.RESET}{token[:25]}...", f"discord.gg/{invite}")
                case 429:
                    console.log("CLOUDFARE", C["magenta"], f"{Fore.RESET}{token[:25]}...", f"discord.gg/{invite}")
                case _:
                    console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}...", response.json().get("message"))
        except Exception as e:
            console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}...", e)

    def poll_spammer(self, token, channel):

        try:
            while True:
                payload = {
                  "mobile_network_type": "unknown",
                  "content": "",
                  "nonce": "",
                  "tts": False,
                  "flags": 0,
                  "poll": {
                    "question": {
                      "text": "India/India team on top"
                    },
                    "answers": [
                      {
                        "poll_media": {
                          "text": "discord.gg/India"
                        }
                      },
                      {
                        "poll_media": {
                          "text": "discord.gg/nigga"
                        }
                      },
                      {
                        "poll_media": {
                          "text": "discord.gg/India"
                        }
                      },
                      {
                        "poll_media": {
                          "text": "discord.gg/sikibidi"
                        }
                      }
                    ],
                    "allow_multiselect": False,
                    "duration": 24,
                    "layout_type": 1
                  }
                }
                response = session.post(
                    f"https://discord.com/api/v9/channels/{channel}/messages",
                    headers=self.headers(token),
                    json=payload,
                    cookies=self.get_cookies(),
                )
                #print(response.json())
                match response.status_code:
                    case 200:
                        console.log("Sent", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**")
                    case 429:
                        retry_after = response.json().get("retry_after")
                        console.log("RATELIMIT", Fore.LIGHTYELLOW_EX, f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", f"Ratelimit Exceeded - {retry_after}s",)
                        time.sleep(float(retry_after))
                    case _:
                        console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", response.json().get("message"))
                        return
        except Exception as e:
            console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", e)




    def leaver(self, token, guild):
        try:
            def get_guild_name(guild):
                in_guild = []
                for token in tokens:
                    response = session.get(
                        f"https://discord.com/api/v9/guilds/{guild}",
                        headers=self.headers(token)
                    )

                    match response.status_code:
                        case 200:
                            in_guild.append(token)
                            try:
                                return response.json().get("name")
                            except:
                                return guild
                if not in_guild:
                    return guild

            self.guild = get_guild_name(guild)

            payload = {
                "lurking": False,
            }

            while True:
                response = session.delete(
                    f"https://discord.com/api/v9/users/@me/guilds/{guild}",
                    json=payload,
                    headers=self.headers(token)
                )

                match response.status_code:
                    case 204:
                        console.log("LEFT", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", self.guild)
                        break
                    case 429:
                        retry_after = response.json().get("retry_after")
                        console.log("RATELIMIT", C["yellow"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", f"Ratelimit Exceeded - {retry_after}s",)
                        time.sleep(float(retry_after))
                    case _:
                        console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
                        break
        except Exception as e:
            console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

    def emojis():
        emos = list("😀😃😄😁😆😅😂🤣😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🤩🥳😏😒😞😔😟😕🙁☹️😣😖😫😩🥺😢😭😮‍💨😤😠😡🤬🤯😳🥵🥶😱😨😰😥😓🤗🤔🤭🤫🤥😶😶‍🌫️😐😑😬🙄😯😦😧😮😲🥱😴🤤😪😵😵‍💫🤐🥴🤢🤮🤧😷🤒🤕🤑🤠😈👿👹👺🤡💩👻💀☠️👽👾🤖🎃😺😸😹😻😼😽🙀😿😾😀😃😄😁😆😅😂🤣😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🤩🥳😏😒😞😔😟😕🙁☹️😣😖😫😩🥺😢😭😮‍💨😤😠😡🤬🤯😳🥵🥶😱😨😰😥😓🤗🤔🤭🤫🤥😶😶‍🌫️😐😑")
        random.shuffle(emos)
        emojis=""
        for emoji in emos:
            emojis+=emoji
        return emojis

    def bio_changer(self, token, bio):
        try:
            payload = {
                "bio": bio
            }

            while True:
                response = session.patch(
                    "https://discord.com/api/v9/users/@me/profile",
                    headers=self.headers(token),
                    json=payload
                )

                match response.status_code:
                    case 200:
                        console.log("Changed", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", bio)
                        break
                    case 429:
                        retry_after = response.json().get("retry_after")
                        console.log("RATELIMIT", C["yellow"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", f"Ratelimit Exceeded - {retry_after}s",)
                        time.sleep(float(retry_after))
                    case _:
                        console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
                        break
        except Exception as e:
            console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

    def prooun(self):
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        try:
            lists = ["he/him", "she/her", "they/them", "ze/zir", "xe/xem"]
            p = random.choice(lists)
            payload = {
                "pronouns": p
            }
            for token in tokens:
                while True:
                        response = session.patch(
                            "https://discord.com/api/v9/users/@me/profile",
                            headers=self.headers(token),
                            json=payload
                        )

                        match response.status_code:
                            case 200:
                                console.log("Changed", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", p)
                                break
                            case 429:
                                retry_after = response.json().get("retry_after")
                                console.log("RATELIMIT", C["yellow"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", f"Ratelimit Exceeded - {retry_after}s",)
                                time.sleep(float(retry_after))
                            case _:
                                console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
                                break
        except Exception as e:
            console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

    def vc_joiner(self, token, guild, channel, ws):
        try:
            for _ in range(1):
                ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
                ws.send(json.dumps({
                    "op": 2,
                    "d": {
                        "token": token,
                        "properties": {
                            "$os": "windows",
                            "$browser": "Discord",
                            "$device": "desktop"
                        }
                    }
                }))
                ws.send(json.dumps({
                    "op": 4,
                    "d": {
                        "guild_id": guild,
                        "channel_id": channel,
                        "self_mute": False,
                        "self_deaf": False
                    }
                }))
                print(f"{Fore.RESET}[{datetime.now().strftime(f'{Fore.LIGHTBLACK_EX}%H:%M:%S{Fore.RESET}')}] {Fore.RESET}[{Fore.LIGHTBLACK_EX}Joined{Fore.RESET}] {Fore.RESET}{token[:25]}.{Fore.LIGHTBLACK_EX}**")
        except Exception as e:
            console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTLIGHTWHITE_EX}**", e)

    def onliner(self, token, ws):
        try:
            ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
            ws.send(
                json.dumps(
                    {
                        "op": 2,
                        "d": {
                            "token": token,
                            "properties": {
                                "$os": "Windows",
                            },
                        },
                    }
                )
            )
        except Exception as e:
            console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", e)

    def member_scrape(self, guild_id, channel_id):
        try:
            in_guild = []

            if not os.path.exists(f"scraped/{guild_id}.txt"):
                for token in tokens:
                    response = session.get(
                        f"https://discord.com/api/v9/guilds/{guild_id}",
                        headers=self.headers(token),
                    )

                    match response.status_code:
                        case 200:
                            in_guild.append(token)
                            break

                if not in_guild:
                    console.log("Failed", C["red"], "Missing Access")
                token = random.choice(in_guild)
                members = scrape(token, guild_id, channel_id)
                with open(f"scraped/{guild_id}.txt", "a") as f:
                    f.write("\n".join(members))
        except Exception as e:
            console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

    def get_random_members(self, guild_id, count):
        try:
            with open(f"scraped/{guild_id}.txt") as f:
                members = f.read().splitlines()
            message = ""
            for _ in range(int(count)):
                message += f"<@{random.choice(members)}>"
            return message
        except Exception as e:
            console.log("FAILED", C["red"], "Failed to get Random Members", e)

    def spammer(self, token, channel, message=None, guild=None, massping=None, pings=None, random_str=None, emoiyspam=None):
        try:
            while True:
                if massping:
                    self.member_scrape(guild, channel)
                    msg = self.get_random_members(guild, int(pings))
                    payload = {
                        "content": f"{message} {msg}"
                    }
                elif emoiyspam:
                    payload = {
                        "content": Raider.emojis()
                    }
                elif random_str:
                    payload = {
                        "content":f"{message} " + f" > {get_random_str(10)}"
                    }

                else:
                    payload = {
                        "content": f"{message}"
                    }

                api = itertools.cycle(["v9", "v10"])
                response = session.post(
                    f"https://discord.com/api/{next(api)}/channels/{channel}/messages",
                    headers=self.headers(token),
                    json=payload
                )

                match response.status_code:
                    case 200:
                        console.log("Sent", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**")
                    case 429:
                        retry_after = response.json().get("retry_after")
                        console.log("RATELIMIT", C["yellow"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", f"Ratelimit Exceeded - {retry_after}s",)
                        time.sleep(retry_after)
                    case _:
                        console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
                        return
                        break
        except Exception as e:
            console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

    def dyno_massping(self, token, guild, channel, message, count):
        try:
            while True:
                headers = self.headers(token)

                tag = get_random_str(6)

                headers[
                    "content-type"
                ] = "multipart/form-data; boundary=----WebKitFormBoundary8cOu4YCjwIllrLVf"

                pings = self.get_random_members(guild, int(count))
                data = (
                    '------WebKitFormBoundary8cOu4YCjwIllrLVf\r\nContent-Disposition: form-data; name="payload_json"\r\n\r\n{"type":2,"application_id":"161660517914509312","guild_id":"%s","channel_id":"%s","session_id":"%s","data":{"version":"1116144106687692895","id":"824701594749763611","name":"tag","type":1,"options":[{"type":1,"name":"create","options":[{"type":3,"name":"name","value":"%s"},{"type":3,"name":"content","value":"a```%s```a"}]}],"application_command":{"id":"824701594749763611","application_id":"161660517914509312","version":"1116144106687692895","default_member_permissions":null,"type":1,"nsfw":false,"name":"tag","description":"Get or create a tag","dm_permission":false,"contexts":null,"integration_types":[0],"options":[{"type":1,"name":"raw","description":"Get the raw tag for use copying/editing.","options":[{"type":3,"name":"name","description":"Tag name","required":true,"autocomplete":true},{"type":3,"name":"category","description":"Tag category","autocomplete":true}]},{"type":1,"name":"get","description":"Get a tag","options":[{"type":3,"name":"name","description":"Tag name","required":true,"autocomplete":true},{"type":3,"name":"category","description":"Tag category","autocomplete":true}]},{"type":1,"name":"edit","description":"Edit a tag","options":[{"type":3,"name":"name","description":"Tag name","required":true,"autocomplete":true},{"type":3,"name":"content","description":"Tag content","required":true},{"type":3,"name":"category","description":"Tag category","autocomplete":true}]},{"type":1,"name":"delete","description":"Delete a tag","options":[{"type":3,"name":"name","description":"Tag name","required":true,"autocomplete":true},{"type":3,"name":"category","description":"Tag category","autocomplete":true}]},{"type":1,"name":"create","description":"Create a tag","options":[{"type":3,"name":"name","description":"Tag name","required":true,"autocomplete":true},{"type":3,"name":"content","description":"Tag content","required":true},{"type":3,"name":"category","description":"Tag category","autocomplete":true}]},{"type":1,"name":"category","description":"Creates a tag category","options":[{"type":3,"name":"category","description":"Category name","required":true}]},{"type":1,"name":"categories","description":"Creates a tag category"},{"type":1,"name":"delcat","description":"Deletes a tag category","options":[{"type":3,"name":"category","description":"Category name","required":true,"autocomplete":true}]}]},"attachments":[]}}\r\n------WebKitFormBoundary8cOu4YCjwIllrLVf--\r\n'
                    % (guild, channel, uuid.uuid4().hex, tag, f"{message} {pings}")
                )

                response = session.post(
                    "https://discord.com/api/v9/interactions",
                    headers=headers,
                    data=data,
                )

                match response.status_code:
                    case 204:
                        console.log("TAG", C["magenta"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", tag)
                    case 429:
                        retry_after = response.json().get("retry_after")
                        console.log("RATELIMIT", Fore.LIGHTYELLOW_EX, f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", f"Ratelimit Exceeded - {retry_after}s",)
                        time.sleep(float(retry_after))
                    case _:
                        console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", response.json().get("message"))
                        return
                time.sleep(5)

                headers[
                    "content-type"
                ] = "multipart/form-data; boundary=----WebKitFormBoundary7RNPUxNP2KkB0I2S"

                data = (
                    '------WebKitFormBoundary7RNPUxNP2KkB0I2S\r\nContent-Disposition: form-data; name="payload_json"\r\n\r\n{"type":2,"application_id":"161660517914509312","guild_id":"%s","channel_id":"%s","session_id":"%s","data":{"version":"1116144106687692895","id":"824701594749763611","name":"tag","type":1,"options":[{"type":1,"name":"raw","options":[{"type":3,"name":"name","value":"%s"}]}],"application_command":{"id":"824701594749763611","application_id":"161660517914509312","version":"1116144106687692895","default_member_permissions":null,"type":1,"nsfw":false,"name":"tag","description":"Get or create a tag","dm_permission":false,"contexts":null,"integration_types":[0],"options":[{"type":1,"name":"raw","description":"Get the raw tag for use copying/editing.","options":[{"type":3,"name":"name","description":"Tag name","required":true,"autocomplete":true},{"type":3,"name":"category","description":"Tag category","autocomplete":true}]},{"type":1,"name":"get","description":"Get a tag","options":[{"type":3,"name":"name","description":"Tag name","required":true,"autocomplete":true},{"type":3,"name":"category","description":"Tag category","autocomplete":true}]},{"type":1,"name":"edit","description":"Edit a tag","options":[{"type":3,"name":"name","description":"Tag name","required":true,"autocomplete":true},{"type":3,"name":"content","description":"Tag content","required":true},{"type":3,"name":"category","description":"Tag category","autocomplete":true}]},{"type":1,"name":"delete","description":"Delete a tag","options":[{"type":3,"name":"name","description":"Tag name","required":true,"autocomplete":true},{"type":3,"name":"category","description":"Tag category","autocomplete":true}]},{"type":1,"name":"create","description":"Create a tag","options":[{"type":3,"name":"name","description":"Tag name","required":true,"autocomplete":true},{"type":3,"name":"content","description":"Tag content","required":true},{"type":3,"name":"category","description":"Tag category","autocomplete":true}]},{"type":1,"name":"category","description":"Creates a tag category","options":[{"type":3,"name":"category","description":"Category name","required":true}]},{"type":1,"name":"categories","description":"Creates a tag category"},{"type":1,"name":"delcat","description":"Deletes a tag category","options":[{"type":3,"name":"category","description":"Category name","required":true,"autocomplete":true}]}]},"attachments":[]}}\r\n------WebKitFormBoundary7RNPUxNP2KkB0I2S--\r\n'
                    % (guild, channel, uuid.uuid4().hex, tag)
                )

                response = session.post(
                    "https://discord.com/api/v9/interactions",
                    headers=headers,
                    data=data,
                )

                match response.status_code:
                    case 204:
                        console.log("SENT", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", tag)
                    case 429:
                        retry_after = response.json().get("retry_after")
                        console.log("RATELIMIT", Fore.LIGHTYELLOW_EX, f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", f"Ratelimit Exceeded - {retry_after}s",)
                        time.sleep(float(retry_after))
                    case _:
                        console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", response.json().get("message"))
                        return
                time.sleep(5)
        except Exception as e:
            console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", e)

    def masspanel(self, token, guild, channel):
        try:
            while True:
                headers = self.headers(token)

                headers[
                    "content-type"
                ] = "multipart/form-data; boundary=----WebKitFormBoundary1hIjYVJbLUqgQTKR"

                data = (
                    '------WebKitFormBoundary1hIjYVJbLUqgQTKR\r\nContent-Disposition: form-data; name="payload_json"\r\n\r\n{"type":2,"application_id":"703886990948565003","guild_id":"%s","channel_id":"%s","session_id":"%s","data":{"version":"1014638915954675737","id":"1014638915954675733","name":"panel","type":1,"options":[],"application_command":{"id":"1014638915954675733","application_id":"703886990948565003","version":"1014638915954675737","default_member_permissions":null,"type":1,"nsfw":false,"name":"panel","description":"Send a verification panel/button in that channel","dm_permission":true,"contexts":null,"integration_types":[0]},"attachments":[]},"nonce":"1158803562642276352"}\r\n------WebKitFormBoundary1hIjYVJbLUqgQTKR--\r\n'
                    % (guild, channel, uuid.uuid4().hex)
                )

                time.sleep(3)

                response = session.post(
                    "https://discord.com/api/v9/interactions",
                    headers=headers,
                    data=data,
                )

                match response.status_code:
                    case 204:
                        console.log("SEND", C["magenta"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**")
                    case 429:
                        retry_after = response.json().get("retry_after")
                        console.log("RATELIMIT", Fore.LIGHTYELLOW_EX, f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", f"Ratelimit Exceeded - {retry_after}s",)
                        time.sleep(float(retry_after))
                    case _:
                        console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", response.json().get("message"))
        except Exception as e:
            console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", e)

    def join_voice_channel(self, guild_id, channel_id):
        ws = websocket.WebSocket()

        def check_for_guild(token):
            response = session.get(
                f'https://discord.com/api/v9/guilds/{guild_id}', headers=self.headers(token)
            )
            match response.status_code:
                case 200:
                    return True
                case _:
                    console.log("Failed", C["red"], "Missing Access")

        def check_for_channel(token):
            if check_for_guild(token):
                response = session.get(
                    f'https://discord.com/api/v9/channels/{channel_id}', headers=self.headers(token)
                )
                match response.status_code:
                    case 200:
                        return True
                    case _:
                        return False

        def run(token):
            if check_for_channel(token):
                console.log('Joined', C['green'], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", channel_id)
                self.voice_spammer(token, ws, guild_id, channel_id, True)
            else:
                console.log('Failed', C['red'], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", channel_id)

        args = [
            (token, ) for token in tokens
        ]
        Menu().run(run, args)

    def voice_spammer(self, token, ws, guild_id, channel_id, close=None):
        try:
            self.onliner(token, ws)
            ws.send(
                json.dumps(
                    {
                        "op": 4,
                        "d": {
                            "guild_id": guild_id,
                            "channel_id": channel_id,
                            "self_mute": True,
                            "self_deaf": False,
                            "self_stream": False,
                            "self_video": False,
                        },
                    }
                )
            )
            ws.send(
                json.dumps(
                    {
                        "op": 18,
                        "d": {
                            "type": "guild",
                            "guild_id": guild_id,
                            "channel_id": channel_id,
                            "preferred_region": "singapore",
                        },
                    }
                )
            )
            ws.send(json.dumps({"op": 1, "d": None}))
            if close:
                ws.close()
        except Exception as e:
            console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", e)

    def token_checker(self):
        valid = []
        def main(token):
            try:
                while True:
                    response = session.get(
                        "https://discordapp.com/api/v9/users/@me/library",
                        headers=self.headers(token)
                    )

                    match response.status_code:
                        case 200:
                            console.log("Valid", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**")
                            valid.append(token)
                            break
                        case 403:
                            console.log("LOCKED", C["yellow"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**")
                            break
                        case 429:
                            retry_after = response.json().get("retry_after")
                            console.log("RATELIMITED", C["pink"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", f"{retry_after}s")
                            time.sleep(retry_after)
                        case _:
                            console.log("Invalid", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
                            break
                with open("data/tokens.txt", "w") as f:
                    f.write("\n".join(valid))
            except Exception as e:
                console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        tokens = [token.replace('"', '') for token in tokens if token]
        tokens = list(set(tokens))
        args = [
            (token, ) for token in tokens
        ]
        Menu().run(main, args)

    def reactor_main(self, channel_id, message_id):
        try:
            access_token = []
            emojis = []
            with open("data/tokens.txt", "r") as f:
                tokens = f.read().splitlines()

            params = {
                "around": message_id, 
                "limit": 50
            }

            for token in tokens:
                response = session.get(
                    f"https://discord.com/api/v9/channels/{channel_id}/messages",
                    headers=self.headers(token),
                    params=params
                )

                match response.status_code:
                    case 200:
                        access_token.append(token)
                        break

            if not access_token:
                console.log("Failed", C["red"], "Missing Permissions")
                input()
                Menu().main_menu()
            else:
                data = response.json()
                for __ in data:
                    if __["id"] == message_id:
                        reactions = __["reactions"]
                        for emois in reactions:
                            if emois:
                                emoji_id = emois["emoji"]["id"]
                                emoji_name = emois["emoji"]["name"]

                                if emoji_id is None:
                                    emojis.append(emoji_name)
                                else:
                                    emojis.append(f"{emoji_name}:{emoji_id}")
                            else:
                                console.log("Failed", C["red"], "No reactions Found in this message",)
                                input()
                                Menu().main_menu()

                for i, emoji in enumerate(emojis, start=1):
                    print(f"{C['light_blue']}0{i}:{C['white']} {emoji}")

                choice = input(f"\n{console.prompt('Choice')}")
                selected = emojis[int(choice) - 1]

            def add_reaction(token):
                try:
                    url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{selected}/@me"

                    if emoji_id is None:
                        url += "?location=Message&type=0"
                    response = session.put(url, headers=self.headers(token))

                    match response.status_code:
                        case 204:
                            console.log("Reacted", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", selected)
                        case _:
                            console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
                except Exception as e:
                    console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

            args = [
                (token,) for token in tokens
            ]
            Menu().run(add_reaction, args)

        except Exception as e:
            console.log("FAILED", C["red"], "Failed to get emojis", e)
            input()
            Menu().main_menu()

            def add_reaction(token):
                try:
                    url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{selected}/@me"

                    if emoji_id is None:
                        url += "?location=Message&type=0"
                    response = session.put(url, headers=self.headers(token))

                    match response.status_code:
                        case 204:
                            console.log("REACTED", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", selected)
                        case _:
                            console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
                except Exception as e:
                    console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

            with open("data/tokens.txt", "r") as f:
                tokens = f.read().splitlines()
            args = [
                (token) for token in tokens
            ]
            Menu().run(add_reaction, args)

    def soundbord(self, token, channel):
        try:
            sounds = session.get(
                "https://discord.com/api/v9/soundboard-default-sounds",
                headers=self.headers(token)
            ).json()

            time.sleep(1)

            while True:
                sound = random.choice(sounds)
                name = sound.get("name")

                payload = {
                    "emoji_id": None,
                    "emoji_name": sound.get("emoji_name"),
                    "sound_id": sound.get("sound_id"),
                }

                response = session.post(
                    f"https://discord.com/api/v9/channels/{channel}/send-soundboard-sound", 
                    headers=self.headers(token), 
                    json=payload,
                )

                match response.status_code:
                    case 204:
                        console.log("Success", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", f"Played {name}")
                    case 429:
                        retry_after = response.json().get("retry_after")
                        console.log("RATELIMIT", C["yellow"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", f"Ratelimit Exceeded - {retry_after}s",)
                        time.sleep(float(retry_after))
                    case _:
                        console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
                time.sleep(random.uniform(0.56, 0.75))
        except Exception as e:
            console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

    def open_dm(self, token, user_id):
        try:
            payload = {
                "recipients": [user_id]
            }

            response = session.post(
                "https://discord.com/api/v9/users/@me/channels",
                headers=self.headers(token),
                json=payload
            )

            match response.status_code:
                case 200:

                    return response.json()["id"]
                case _:
                    console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
                    return
        except Exception as e:
            console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

    def mass_report(self, token, channelid, messageid):
        try:
            payload = {
                "version":"1.0",
                "variant":"3",
                "language":"en",
                "breadcrumbs":[3,31],
                "elements":{},
                "name":"message",
                "channel_id":channelid,
                "message_id":messageid
            }

            response = session.post(
                f"https://discord.com/api/v9/reporting/message",
                headers=self.headers(token),
                json=payload
            )
            if "Missing Access" in response.text:
                console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", "Missing Access")  
            elif "report_id" in response.text:
                console.log("Reported", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", messageid)
            else:
                console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json())  


        except Exception as e:
            console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

    def format_tokens(self):
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()

        try:
            formatted = []

            for token in tokens:
                token = token.strip()

                if token:
                    tokens_split = token.split(":")
                    if len(tokens_split) >= 3:
                        formatted_token = tokens_split[2]
                        formatted.append(formatted_token)
                    else:
                        formatted.append(token)

            console.log("SUCCESS", C["green"], f"Formatted {len(formatted)} tokens")

            with open("data/tokens.txt", "w") as f:
                for token in formatted:
                    f.write(f"{token}\n")
            Menu().main_menu()
        except Exception as e:
            console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", e)

    def button_bypass(self, token, message_id, channel_id, guild_id):
        try:
            payload = {"limit": "50", "around": message_id}
            response = session.get(
                f"https://discord.com/api/v9/channels/{channel_id}/messages",
                params=payload,
                headers=self.headers(token)
            )

            messages = response.json()
            message_to_click = next((msg for msg in messages if msg["id"] == message_id), None)

            if message_to_click is None:
                console.log("FAILED", C["red"], "Message not found")
                return

            buttons = [comp["components"][0] for comp in message_to_click.get("components", [])]
            if not buttons:
                console.log("FAILED", C["red"], "No buttons found in the message")
                return

            for button in buttons:
                data = {
                    "application_id": message_to_click["author"]["id"],
                    "channel_id": channel_id,
                    "data": {
                        "component_type": 2,
                        "custom_id": button["custom_id"],
                    },
                    "guild_id": guild_id,
                    "message_flags": 0,
                    "message_id": message_id,
                    "nonce": self.nonce(),
                    "session_id": uuid.uuid4().hex,
                    "type": 3,
                }

                response = session.post(
                    "https://discord.com/api/v9/interactions",
                    headers=self.headers(token),
                    json=data
                )

                match response.status_code:
                    case 204:
                        console.log(f"Clicked button {button['custom_id']}", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**")
                    case _:
                        console.log(f"Failed to click button {button['custom_id']}", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", {response.json().get("message")})
        except Exception as e:
            console.log("FAILED", C["red"], "Failed to Click Button", e)



    def accept_rules(self, guild_id):
        try:
            valid = []
            with open("data/tokens.txt", "r") as f:
                tokens = f.read().splitlines()

            for token in tokens:
                value = session.get(
                    f"https://discord.com/api/v9/guilds/{guild_id}/member-verification",
                    headers=self.headers(token)
                )

                match value.status_code:
                    case 200:
                        valid.append(token)
                        payload = value.json()
                        break

            if not valid:
                console.log("FAILED", C["red"], "All tokens are Invalid")
                input()
                Menu().main_menu()

        except Exception as e:
            console.log("FAILED", C["red"], "Failed to Accept Rules", e)

        def run_main(token):
            try:
                response = session.put(
                    f"https://discord.com/api/v9/guilds/{guild_id}/requests/@me",
                    headers=self.headers(token),
                    json=payload
                )

                match response.status_code:
                    case 201:
                        console.log("ACCEPTED", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", guild_id)
                    case _:
                        console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
            except Exception as e:
                console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        args = [
            (token, ) for token in tokens
        ]
        Menu().run(run_main, args)

    def mass_nick(self, token, guild, nick):
        try:
            payload = {
                "nick" : nick
            }

            while True:
                response = session.patch(
                    f"https://discord.com/api/v9/guilds/{guild}/members/@me", 
                    headers=self.headers(token),
                    json=payload
                )

                match response.status_code:
                    case 200:
                        console.log("SUCCESS", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**")
                        break
                    case 429:
                        retry_after = response.json().get("retry_after")
                        console.log("RATELIMIT", C["yellow"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", f"Ratelimit Exceeded - {retry_after}s",)
                        time.sleep(float(retry_after))
                    case _:
                        console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
                        break
        except Exception as e:
            console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

    def thread_spammer(self, token, channel_id, name):
        try:
            payload = {
                "name": name,
                "type": 11,
                "auto_archive_duration": 4320,
                "location": "Thread Browser Toolbar",
            }

            while True:
                response = session.post(
                    f"https://discord.com/api/v9/channels/{channel_id}/threads",
                    headers=self.headers(token),
                    json=payload
                )

                match response.status_code:
                    case 201:
                        console.log("CREATED", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", name)
                    case 429:
                        retry_after = response.json().get("retry_after")
                        if int(retry_after) > 10:
                            console.log("STOPPED", C["magenta"], token[:25], f"Ratelimit Exceeded - {int(round(retry_after))}s",)
                            break
                        else:
                            console.log("RATELIMIT", C["yellow"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", f"Ratelimit Exceeded - {retry_after}s",)
                            time.sleep(float(retry_after))
                    case _:
                        console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
                        break
        except Exception as e:
            console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)


    def friender(self, token, nickname):
        try:
            headers = self.headers(token)
            payload = {
                "username": nickname,
                "discriminator": None,
            }

            response = session.post(
                f"https://discord.com/api/v9/users/@me/relationships", 
                headers=headers, 
                json=payload
            )

            match response.status_code:
                case 204:
                    console.log(f"SUCCESS", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**")
                case 400:
                    console.log("CAPTCHA", C["yellow"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**")
                case _:
                    console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json())
        except Exception as e:
            console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

    def spambypass(self, token, channel_ids, SPAM_MESSAGE):
       api = itertools.cycle(["v9", "v10"])
       try:
           while True:
               ch = random.choice(channel_ids)
               res = session.post(f"https://discord.com/api/{next(api)}/channels/{ch}/messages", headers=self.headers(token), json={"content": SPAM_MESSAGE + " | " + " | ".join(random.choice(string.ascii_letters) for i in range(6)),"tts":True,"flags":0})
               if res.status_code == 200:
                   console.log("Sent", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}** -- {ch}")
               elif "retry_after" in res.text:
                   time.sleep(res.json()['retry_after'])
                   return self.spambypass(token, channel_ids, SPAM_MESSAGE)
               else:
                   #print(f" {Fore.RED}[-] fail to attack. {Fore.RESET} -- {ch}")
                   return self.spambypass(token, channel_ids, SPAM_MESSAGE)
       except:pass


    def onliner_(self, token):
        try:
            config = {
            "details": ".gg/vesperv",
            "state": ".gg/funvexcommunity",
            "name": f"x2saddddDM On Top",
        }   

            ws = websocket.WebSocket()
            ws.connect("wss://gateway.discord.gg/?encoding=json&v=9")
            console.log("Onlined", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**")
            response = ws.recv()
            event = json.loads(response)
            heartbeat_interval = int(event["d"]["heartbeat_interval"]) / 1000
            ws.send(
                json.dumps(
                    {
                        "op": 2,
                        "d": {
                            "token": token,
                            "properties": {
                                "$os": sys.platform,
                                "$browser": "RTB",
                                "$device": f"{sys.platform} Device",
                            },
                            "presence": {
                                "game": {
                                    "name": config["name"],
                                    "type": 0,
                                    "details": config["details"],
                                    "state": config["state"],
                                },
                                "status": random.choice(("online", "idle", "dnd")),
                                "since": 0,
                                "activities": [],
                                "afk": False,
                            },
                        },
                        "s": None,
                    "t": None,
                    }
                )
            )
        except:pass
    def onliner__(self):
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        try:

            with ThreadPoolExecutor(1000) as executor:
                for token in tokens:
                    executor.submit(self.onliner_, token)
        except:pass
        #for token in tokens:
        #    threading.Thread(target=self.onliner_,args=(token,)).start()

    def start_spambypass(self, GUILD_ID, message):
        """ Start the spam bypass process. """

        # Read tokens from file
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()

        # Get channel IDs from the guild
        tokenq = random.choice(tokens)
        channel_ids = []
        r = requests.get(f"https://discord.com/api/v9/guilds/{GUILD_ID}/channels", headers=self.headers(tokenq)).json()

        # Extract channel IDs
        try:
            for xd in r:
                channel_ids.append(xd["id"])
        except:
            print("Error getting channels, retrying...")
            self.start_spambypass(GUILD_ID, message)  # Retry fetching channels if error occurs

        threads = []
        while True:
            # Use a different token for each thread
            for token in tokens:
                thread = threading.Thread(target=self.spambypass, args=(token, channel_ids, message))
                threads.append(thread)
                thread.start()

    def joinVCrandom(self, GUILD_ID, token):
        try:
            headers = {
                "content-type": "application/json",
                "authorization": token
            }
            response = session.get(f'https://discord.com/api/v9/guilds/{GUILD_ID}/channels', headers=headers)
            channels = response.json()
            try:
                voice_channel_ids = [channel['id'] for channel in channels if channel['type'] == 2]
            except Exception as e:
                print(f"Error getting channels: {e}, retrying...")
                self.joinVCrandom(GUILD_ID)  # Retry fetching channels if error occurs
                return


            while True:
                aa = random.choice(voice_channel_ids)
                ws = websocket.WebSocket()
                try:
                    ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
                    ws.send(json.dumps({"op": 2, "d": {"token": token, "properties": {"$os": "windows", "$browser": "Discord", "$device": "desktop"}}}))
                    ws.send(json.dumps({"op": 4, "d": {"guild_id": GUILD_ID, "channel_id": aa, "self_mute": True, "self_deaf": True, "self_stream?": True, "self_video": False}}))
                    ws.send(json.dumps({"op": 1, "d": None}))
                    console.log("WS Connected", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", aa)
                except Exception as e:
                    pass
                finally:
                    console.log("WS Quit", C["green"], f"     {Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**", aa)
                    ws.close()
        except Exception as e:
            print(f"Unexpected error: {e}")

    def start_spammervcrandom(self, GUILD_ID):
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        try:

            with ThreadPoolExecutor(sys.maxsize) as executor:
                for token in tokens:
                    executor.submit(self.joinVCrandom, GUILD_ID, token)
        except:pass

    def onboard_bypass(self, guild_id):
        try:
            with open("data/tokens.txt", "r") as f:
                tokens = f.read().splitlines()
            onboarding_responses_seen = {}
            onboarding_prompts_seen = {}
            onboarding_responses = []
            in_guild = []

            for _token in tokens:
                response = session.get(
                    f"https://discord.com/api/v9/guilds/{guild_id}/onboarding",
                    headers=self.headers(_token)
                )
                match response.status_code:
                    case 200:
                        in_guild.append(_token)
                        break

            if not in_guild:
                console.log("FAILED", C["red"], "Missing Access")
                input()
                Menu().main_menu()
            else:
                data = response.json()
                now = int(datetime.now().timestamp())

                for __ in data["prompts"]:
                    onboarding_responses.append(__["options"][-1]["id"])

                    onboarding_prompts_seen[__["id"]] = now

                    for prompt in __["options"]:
                        if prompt:
                            onboarding_responses_seen[prompt["id"]] = now
                        else:
                            console.log(
                                "FAILED",
                                C["red"],
                                "No onboarding in This Server",
                            )
                            input()
                            Menu().main_menu()

        except Exception as e:
            console.log("FAILED", C["red"], "Failed to Pass Onboard", e)
            input()
            Menu().main_menu()

        def run_task(token):
            try:
                json_data = {
                    "onboarding_responses": onboarding_responses,
                    "onboarding_prompts_seen": onboarding_prompts_seen,
                    "onboarding_responses_seen": onboarding_responses_seen,
                }

                response = session.post(
                    f"https://discord.com/api/v9/guilds/{guild_id}/onboarding-responses",
                    headers=self.headers(token),
                    json=json_data
                )

                match response.status_code:
                    case 200:
                        console.log("ACCEPTED", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**")
                    case _:
                        console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
            except Exception as e:
                console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

        args = [
            (token, ) for token in tokens
        ]
        Menu().run(run_task, args)

        def run_task(token):
            try:
                json_data = {
                    "onboarding_responses": onboarding_responses,
                    "onboarding_prompts_seen": onboarding_prompts_seen,
                    "onboarding_responses_seen": onboarding_responses_seen,
                }

                response = session.post(
                    f"https://discord.com/api/v9/guilds/{guild_id}/onboarding-responses",
                    headers=self.headers(token),
                    json=json_data
                )

                match response.status_code:
                    case 200:
                        console.log("ACCEPTED", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**")
                    case _:
                        console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
            except Exception as e:
                console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

        args = [
            (token, ) for token in tokens
        ]
        Menu().run(run_task, args)

class Menu:
    def __init__(self):
        self.raider = Raider()
        self.options = {
            "1": self.joiner, 
            "2": self.leaver,
            "3": self.spammer, 
            "4": self.checker,
            "5": self.reactor, 
            "6": self.soundbord,
            "7": self.formatter,
            "8": self.button,
            "9": self.accept,
            "10": self.bio,
            "11": self.onlinqs,
            "12": self.voicejoiner,
            "13": self.nick_chang,
            "14": self.thad,
            "15": self.friend,
            "16": self.onboard,
            "17": self.inviter,
            "18": self.all_spammer,
            "19": self.vc_random,
            "20": self.pronoun,
            "21": self.poll,
            "22": self.mass_report,
            "23": self.exit,
        }

    def main_menu(self, _input=None):

        Clear()
        if _input:
            input()
        console.run()
        choice = input(f"{' '*4}{Fore.LIGHTWHITE_EX}          > ")

        if choice in self.options:
            console.render_ascii()
            self.options[choice]()
        else:
            self.main_menu()





    def run(self, func, args):
        threads = []
        Clear()
        console.render_ascii()
        for arg in args:
            thread = threading.Thread(target=func, args=arg)
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        input("\n ~/> press enter to continue ")
        self.main_menu()

    @wrapper
    def mass_report(self):
        os.system('title Funvex - Reactor')
        message = input(console.prompt("Message Link"))
        if message == "":
            Menu().main_menu()
        if message.startswith("https://"):
            pass
        else:
            Menu().main_menu()
        channel_id = message.split("/")[5]
        message_id = message.split("/")[6]
        Clear()
        console.render_ascii()
        args = [
            (token, channel_id, message_id) for token in tokens
        ]
        self.run(self.raider.mass_report, args)

    @wrapper
    def poll(self):
        os.system('title Funvex - poll')
        guild = input(console.prompt("channel ID"))
        GUILD_ID = int(guild)
        if GUILD_ID == "":
            Menu().main_menu()
        Clear()
        args = [
            (token, GUILD_ID) for token in tokens
        ]
        self.run(self.raider.poll_spammer, args)

    @wrapper
    def vc_random(self):
        os.system('title Funvex - Spammer')
        guild = input(console.prompt("Guild ID"))
        GUILD_ID = int(guild)
        if GUILD_ID == "":
            Menu().main_menu()
        Clear()
        args = [
            (GUILD_ID,)
        ]
        self.run(self.raider.start_spammervcrandom, args)


    @wrapper
    def soundbord(self):
        os.system('title Funvex - Soundboard Spam')
        Link = input(console.prompt("Channel LINK"))
        if Link == "":
            Menu().main_menu()
        if Link.startswith("https://"):
            pass
        else:
            Menu().main_menu()
        channel = Link.split("/")[5]
        guild = Link.split("/")[4]
        Clear()
        console.render_ascii()
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        tokenq = random.choice(tokens)
        for token in tokens:
            threading.Thread(target=self.raider.vc_joiner, args=(token, guild, channel, websocket.WebSocket())).start()
            threading.Thread(target=self.raider.soundbord, args=(token, channel)).start()
        input("\n ~/> press enter to continue ")
        self.main_menu()

    @wrapper
    def inviter(self):
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        os.system('title Funvex - inviter')
        Link = input(console.prompt("Channel LINK"))
        if Link == "":
            Menu().main_menu()
        if Link.startswith("https://"):
            pass
        else:
            Menu().main_menu()
        channel = Link.split("/")[5]
        Clear()
        args = [
            (token, channel) for token in tokens
        ]
        self.run(self.raider.inviter, args)
        Clear()
        console.render_ascii()

    @wrapper
    def all_spammer(self):
        os.system('title Funvex - Spammer')
        Link = input(console.prompt("Guild ID"))
        if Link == "":
            Menu().main_menu()
        guild = int(Link)
        Clear()
        console.render_ascii()
        Clear()
        console.render_ascii()
        message = input(console.prompt("Message"))
        Clear()
        args = [
            (guild, message)
        ]
        self.run(self.raider.start_spambypass, args)

    @wrapper
    def caller(self):
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        os.system('title Funvex - Caller')
        user_id = input(console.prompt("User ID"))
        if user_id == "":
            Menu().main_menu()
        Clear()
        console.render_ascii()
        for token in tokens:
            threading.Thread(target=self.raider.call_spammer, args=(token, user_id)).start()
        input("\n ~/> press enter to continue ")
        self.main_menu()

    @wrapper
    def onlinq(self):
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        os.system('title Funvex - Onliner')
        for token in tokens:
            print(f"{Fore.RESET}[{datetime.now().strftime(f'{Fore.LIGHTBLACK_EX}%H:%M:%S{Fore.RESET}')}] {Fore.RESET}[{Fore.GREEN}Onlined{Fore.RESET}] {Fore.RESET}{token[:25]}.{Fore.LIGHTWHITE_EX}**")
            threading.Thread(target=self.raider.onliner, args=(token, websocket.WebSocket())).start()
        input("\n ~/> press enter to continue ")
        self.main_menu()

    @wrapper
    def onlinqs(self):

        os.system('title Funvex - Onliner')
        threading.Thread(target=self.raider.onliner__).start()
        input("\n ~/> press enter to continue ")
        self.main_menu()


    @wrapper
    def friend(self):
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        os.system('title Funvex - Friender')
        nickname = input(console.prompt("Nick"))
        if nickname == "":
            Menu().main_menu()
        Clear()
        console.render_ascii()
        args = [
            (token, nickname) for token in tokens
        ]
        self.run(self.raider.friender, args)

    @wrapper
    def nick_chang(self):
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        os.system('title Funvex - Nickname Changer')
        nick = input(console.prompt("Nick"))
        if nick == "":
            Menu().main_menu()
        Clear()
        console.render_ascii()
        guild = input(console.prompt("Guild ID"))
        if guild == "":
            Menu().main_menu()
        Clear()
        console.render_ascii()
        args = [
            (token, guild, nick) for token in tokens
        ]
        self.run(self.raider.mass_nick, args)

    @wrapper
    def voicejoiner(self):
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        os.system('title Funvex - Voice Joiner')
        Link = input(console.prompt("Channel LINK"))
        if Link == "":
            Menu().main_menu()
        if Link.startswith("https://"):
            pass
        else:
            Menu().main_menu()
        guild = Link.split("/")[4]
        channel = Link.split("/")[5]
        Clear()
        console.render_ascii()
        args = [
            (token, guild, channel, websocket.WebSocket()) for token in tokens
        ]
        self.run(self.raider.vc_joiner, args)

    @wrapper
    def thad(self):
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        os.system('title Funvex - Thread Spammer')
        name = input(console.prompt("Name"))
        if name == "":
            Menu().main_menu()
        Clear()
        console.render_ascii()
        Link = input(console.prompt("Channel LINK"))
        if Link == "":
            Menu().main_menu()
        if Link.startswith("https://"):
            pass
        else:
            Menu().main_menu()
        channel_id = Link.split("/")[5]
        Clear()
        console.render_ascii()
        args = [
            (token, channel_id, name) for token in tokens
        ]
        self.run(self.raider.thread_spammer, args)

    @wrapper
    def joiner(self):
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        os.system('title Funvex - Joiner')
        invite = input(console.prompt(f"Invite"))
        if invite == "":
            Menu().main_menu()
        invite = invite.replace("https://discord.gg/", "").replace("https://discord.com/invite/", "").replace("discord.gg/", "").replace("https://discord.com/invite/", "").replace(".gg/", "")
        Clear()
        console.render_ascii()
        args = [
            (token, invite) for token in tokens
        ]
        self.run(self.raider.joiner, args)

    @wrapper 
    def leaver(self):
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        os.system('title Funvex - Leaver')
        guild = input(console.prompt("Guild ID"))
        if guild == "":
            Menu().main_menu()
        Clear()
        console.render_ascii()
        args = [(token, guild) for token in tokens]
        self.run(self.raider.leaver, args)

    @wrapper
    def spammer(self):
        title(f"Funvex - Spammer")
        Link = input(console.prompt(f"Channel LINK"))
        if Link == "" or not Link.startswith("https://"):
            self.main_menu()

        guild_id = Link.split("/")[4]
        channel_id = Link.split("/")[5]

        emojispam = input(console.prompt("Lag Channel", True))
        Clear()

        if "y" in emojispam:
            args = [(token, channel_id, None, guild_id, False, None, False, True) for token in tokens]
            self.run(self.raider.spammer, args)
        else:
            massping = input(console.prompt("Massping ( Not working )", True))

            if "y" in massping:
                Clear()
                console.log(f"Scraping users", C["light_blue"], False, "this may take a while...")
                self.raider.member_scrape(guild_id, channel_id)
                count = input(console.prompt("Pings Amount"))
                Clear()
                if count == "":
                    Menu().main_menu()

                message = input(console.prompt("Message"))
                Clear()
                if message == "":
                    Menu().main_menu()
                args = [
                    (token, channel_id, message, guild_id, True, count) for token in tokens         # not my finest code
                ]
                self.run(self.raider.spammer, args)
            else:
                random_str = input(console.prompt("Random String", True))
                Clear()
                if "y" in random_str:
                    message = input(console.prompt("Message"))
                    if message == "":
                        Menu().main_menu()
                    args = [
                        (token, channel_id, message, guild_id, False, None, True) for token in tokens
                    ]
                    self.run(self.raider.spammer, args)
                else:
                    message = input(console.prompt("Message"))
                    Clear()

                    if message == "":
                        Menu().main_menu()
                    args = [
                        (token, channel_id, message, guild_id, False, None) for token in tokens
                    ]
                    self.run(self.raider.spammer, args)



    def checker(self):
        os.system('title Funvex - Checker')
        threading.Thread(target=self.raider.token_checker).start()


    @wrapper
    def reactor(self):
        os.system('title Funvex - Reactor')
        message = input(console.prompt("Message Link"))
        if message == "":
            Menu().main_menu()
        if message.startswith("https://"):
            pass
        else:
            Menu().main_menu()
        channel_id = message.split("/")[5]
        message_id = message.split("/")[6]
        Clear()
        console.render_ascii()
        self.raider.reactor_main(channel_id, message_id)

    def formatter(self):
        os.system('title Funvex - Formatter')
        self.run(self.raider.format_tokens, [()])

    @wrapper
    def button(self):
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        os.system('title Funvex - Clicker')
        message = input(console.prompt("Message Link"))
        if message == "":
            Menu().main_menu()
        if message.startswith("https://"):
            pass
        else:
            Menu().main_menu()
        guild_id = message.split("/")[4]
        channel_id = message.split("/")[5]
        message_id = message.split("/")[6]
        Clear()
        console.render_ascii()
        Clear()
        console.render_ascii()
        args = [
            (token, message_id, channel_id, guild_id) for token in tokens
        ]
        self.run(self.raider.button_bypass, args)

    @wrapper
    def accept(self):
        os.system('title Funvex - Accept Rules')
        guild_id = input(console.prompt("Guild ID"))
        if guild_id == "":
            Menu().main_menu()
        Clear()
        console.render_ascii()
        self.raider.accept_rules(guild_id)


    @wrapper
    def bio(self):
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        os.system('title Funvex - Bio Changer')
        bio = input(console.prompt("Bio"))
        if bio == "":
            Menu().main_menu()
        Clear()
        console.render_ascii()
        args = [
            (token, bio) for token in tokens
        ]
        self.run(self.raider.bio_changer, args)

    @wrapper
    def pronoun(self):
        Clear()
        self.run(self.raider.prooun, [()])

    @wrapper
    def onboard(self):
        os.system('title Funvex - Onboarding Bypass')
        guild_id = input(console.prompt("Guild ID"))
        if guild_id == "":
            Menu().main_menu()
        Clear()
        console.render_ascii()
        self.raider.onboard_bypass(guild_id)

    @wrapper
    def exit(self):
        os.system('title Funvex - Exit')
        print(f"{Fore.RED}Exiting...")
        time.sleep(2)
        os._exit(0)







if __name__ == "__main__":
    Clear()
    fmt()
    time.sleep(0.5)
    Menu().main_menu()