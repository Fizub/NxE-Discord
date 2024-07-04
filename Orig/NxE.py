import requests
import random
import colored
from colored import fg, attr
import numbers
import time
import os
import string
import inifile

ini = inifile.IniFile("Config/config.ini")
    

def Debugging(on):
    if on == True:
        ini["Inside.Debugger"] = True
        print("Debugging is on")
        ini.save(True)
    else:
        ini["Inside.Debugger"] = False
        print("Debugging is off")
        ini.save(True)

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
    if ini["Inside.Debugger"] == "false":
        os.system("cls")
    # Print ASCII art using colored.cprint
    colored.cprint("""     

U P D A T E : Multiple tokens and debug mode!                      
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
'---'                   `----'    
                   
        Made by: github.com/Fizub           """, 147)

    # Print the welcome message in blue
    blue = fg('blue')
    reset = attr('reset')
    print(blue + r"""         Welcome to NxE          
    What option would you like to choose?""" + reset)
    print("[1] Save a Token | [2] Send Messages | [E] Exit\n[3] Send DM | [D] Debug Mode")

    inp_ul = input("> ")

    inp = inp_ul.lower()

    if inp == "1":
        token = input("Enter your token > ")
        
        with open(os.path.dirname(os.path.realpath(__file__)) + "/Config/tokens", "r+") as f:
            global data,data_s
            data = f.read()
            data_s = str.split(data,"|",-1)
            for i in data_s:
                if data == "":
                    f.write(token)
                elif i == token:
                    print("Token already exists!")
                    menu()
                else:
                    f.write("|" + token)
        f.close()
            
            
        colored.cprint("Success!",154)
        time.sleep(2)
        menu()
    if inp == "2":
        with open(os.path.dirname(os.path.realpath(__file__)) + "/Config/tokens", "r+") as f:
            data = f.read()
            data_s = str.split(data,"|",-1)
            S_id, S_ch_id, M_c, T = input("Server Id: "), input("Server Channel Id: "), input("Message Content: "), input("Times (Not really accurate but does the job) : ")
            converted = ( int(T) / len(data_s) )
            while converted > 0:
                    round(converted)
                    
                    for i in data_s:
                        SendMessage(S_id,S_ch_id,M_c,i)
                        if ini["Inside.Debugger"] == "true":
                            print("Debug: Converted Before: " + str(int(converted)))
                            print("Debug: Token: " + i)
                        
                    converted -= 1
                    if ini["Inside.Debugger"] == "true":
                        print("Debug: Converted After: " + str(int(converted)))
            
                
            colored.cprint("Success!",154)
            time.sleep(2)
        
        menu()
        f.close()
        
    if inp == "e":
        exit()
    if inp == "3":
        with open(os.path.dirname(os.path.realpath(__file__)) + "/Config/tokens", "r+") as f:
            colored.cprint("Warning: This command makes the first token in the file: "+os.path.dirname(os.path.realpath(__file__)) + "/Config/tokens"+" the sender, continue?",220)
            inp = input("Continue? (y/n): ")
            if inp == "y":
                data = f.read()
                data_s = str.split(data,"|",-1)
                token = data_s[0]
                C_id,M_c,D_t,T = input("Channel Id: "), input("Message Content: "), token, input("Times: ")
                converted = int(T)
                while converted > 0:
                    SendDM(C_id,M_c,D_t)
                    converted -= 1
                colored.cprint("Success!",154)
                time.sleep(2)
                f.close()
            else:
                menu()
        menu()
    if inp == "d":
        D_on_un = input("On/Off > ")
        D_on = D_on_un.lower()
        if D_on == "on":
            Debugging(True)
        else:
            Debugging(False)
        menu()

menu()