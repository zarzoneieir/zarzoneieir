from keyauth import api

import sys
import time
import platform
import os
import hashlib
from time import sleep
from datetime import datetime



if sys.version_info.minor < 10:  
    print("[Security] - Python 3.10 or higher is recommended. The bypass will not work on 3.10+")
    print("You are using Python {}.{}".format(sys.version_info.major, sys.version_info.minor))

if platform.system() == 'Windows':
    os.system('cls & title Макароны Client')  
elif platform.system() == 'Linux':
    os.system('clear')  
    sys.stdout.write("\x1b]0;Макароны Client\x07")  
elif platform.system() == 'Darwin':
    os.system("clear && printf '\e[3J'")  
    os.system('''echo - n - e "\033]0;Макароны Client\007"''')  

print("Initializing")


def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest



keyauthapp = api(
    name = "BEGULAstaff",
    ownerid = "9m7ywGAJdb",
    secret = "44dafeabbf302a64387589348bc93570b4fc56d1b06086acd4be7f09be3d9bd8",
    version = "1.0",
    hash_to_check = getchecksum()
)


def answer():
    try:
        print("""
 1.Войти
 2.Войти по ключу
        """)
        ans = input(" Ваш выбор: ")
        if ans == "1":
            user = input(' Ваш Логин: ')
            password = input(' Ваш Пароль: ')
            keyauthapp.login(user, password)
            os.system('cls')
        elif ans == "2":
            key = input( 'Ваш лицензионный ключ: ')
            keyauthapp.license(key)
            os.system('cls')
        else:
            print("\n Не верный выбор")
            time.sleep(1)
            os.system('cls')
            answer()
    except KeyboardInterrupt:
        os._exit(1)


answer()

'''try:
    if os.path.isfile('auth.json'): #Checking if the auth file exist
        if jsond.load(open("auth.json"))["authusername"] == "": #Checks if the authusername is empty or not
            print("""
1. Login
2. Register
            """)
            ans=input("Select Option: ")  #Skipping auto-login bc auth file is empty
            if ans=="1": 
                user = input('Provide username: ')
                password = input('Provide password: ')
                keyauthapp.login(user,password)
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            elif ans=="2":
                user = input('Provide username: ')
                password = input('Provide password: ')
                license = input('Provide License: ')
                keyauthapp.register(user,password,license) 
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            else:
                print("\nNot Valid Option") 
                os._exit(1) 
        else:
            try: #2. Auto login
                with open('auth.json', 'r') as f:
                    authfile = jsond.load(f)
                    authuser = authfile.get('authusername')
                    authpass = authfile.get('authpassword')
                    keyauthapp.login(authuser,authpass)
            except Exception as e: #Error stuff
                print(e)
    else: #Creating auth file bc its missing
        try:
            f = open("auth.json", "a") #Writing content
            f.write("""{
    "authusername": "",
    "authpassword": ""
}""")
            f.close()
            print ("""
1. Login
2. Register
            """)#Again skipping auto-login bc the file is empty/missing
            ans=input("Select Option: ") 
            if ans=="1": 
                user = input('Provide username: ')
                password = input('Provide password: ')
                keyauthapp.login(user,password)
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            elif ans=="2":
                user = input('Provide username: ')
                password = input('Provide password: ')
                license = input('Provide License: ')
                keyauthapp.register(user,password,license)
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            else:
                print("\nNot Valid Option") 
                os._exit(1) 
        except Exception as e: #Error stuff
            print(e)
            os._exit(1) 
except Exception as e: #Error stuff
    print(e)
    os._exit(1)'''


print("\n Информация: ")
print(" Логин: " + keyauthapp.user_data.username)
print("Аккаунт созданн: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.createdate)).strftime('%Y-%m-%d %H:%M:%S'))
print(" Тип подписки: " + keyauthapp.user_data.subscription)
print(f" IP: " + keyauthapp.user_data.ip)
print(f" HWID: " + keyauthapp.user_data.hwid)



print("Последний заход: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.lastlogin)).strftime('%Y-%m-%d %H:%M:%S'))

#ваш код


      
sleep(10)
os._exit(1)
