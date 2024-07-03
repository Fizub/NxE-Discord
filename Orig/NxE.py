import requests
import random
import colored
from colored import fg, attr
import inifile
import numbers
import time
import os

ini = inifile.IniFile("Config/configuration.ini")

def SendMessage(S_id, S_ch_id, M_c, D_t):
    x = requests.post(
        "https://discord.com/api/v9/channels/"+S_ch_id+"/messages",
        json={"mobile_network_type":"unknown","content":M_c,"nonce":random.randint(100000,999999999999),"tts":False,"flags":0},
        headers={
            "authorization":D_t
        }
    )
    return x

def SendDM(C_id,M_c,D_t):
    x = requests.post(
        "https://discord.com/api/v9/channels/"+C_id+"/messages",
        json={"mobile_network_type":"unknown","content":M_c,"nonce":random.randint(100000,999999999999),"tts":False,"flags":0},
        headers={
            "authorization":D_t
        }
    )
    return x

def menu():
    os.system("cls")
    # Print ASCII art using colored.cprint
    colored.cprint("""         
        ,--.                     
       ,--.'|               ,---,.
   ,--,:  : |             ,'  .' |
,`--.'`|  ' :           ,---.'   |
|   :  :  | |,--,  ,--, |   |   .'
:   |   \ | :|'. \/ .`| :   :  |-,
|   : '  '; |'  \/  / ; :   |  ;/|
'   ' ;.    ; \  \.' /  |   :   .'
|   | | \   |  \  ;  ;  |   |  |-,
'   : |  ; .' / \  \  \ '   :  ;/|
|   | '`--' ./__;   ;  \|   |    |
'   : |     |   :/\  \ ;|   :   .'
;   |.'     `---'  `--` |   | ,'  
'---'                   `----'    """, 147)

    # Print the welcome message in blue
    blue = fg('blue')
    reset = attr('reset')
    print(blue + r"""         Welcome to NxE          
    What option would you like to choose?""" + reset)
    print("[1] Save Main Token | [2] Send Messages | [E] Exit\n[3] Send DM")

    inp = input("> ")

    if inp == "1":
        token = input("Enter your token > ")
        ini["Tokens.MainToken"] = token
        ini.save(True)
        colored.cprint("Success!",154)
        time.sleep(2)
        menu()
    if inp == "2":
        token = ini["Tokens.MainToken"]
        S_id, S_ch_id, M_c, D_t, T = input("Server Id: "), input("Server Channel Id: "), input("Message Content: "), token, input("Times: ")
        converted = int(T)
        while converted > 0:
            SendMessage(S_id,S_ch_id,M_c,D_t)
            converted -= 1
        colored.cprint("Success!",154)
        time.sleep(2)
        menu()
    if inp == "E":
        exit()
    if inp == "3":
        token = ini["Tokens.MainToken"]
        C_id,M_c,D_t,T = input("Channel Id: "), input("Message Content: "), token, input("Times: ")
        converted = int(T)
        while converted > 0:
            SendDM(C_id,M_c,D_t)
            converted -= 1
        colored.cprint("Success!",154)
        time.sleep(2)
        menu()
        

menu()