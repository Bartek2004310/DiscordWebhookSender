import requests
import pyfiglet


ascii_banner = pyfiglet.figlet_format("DiscordSender By Booscik")
print(ascii_banner)

mUrl = input("[1] Webhook = ")
a = input("[2] Message = ")

message = {"content": a}
send = requests.post(mUrl, json=message)

print(send.status_code)

print(send.content)
