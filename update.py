import requests
import os

with open("VERSION") as f:
    VERSION = f.read().strip()


def self_update():
    r_version = requests.get("https://raw.githubusercontent.com/DocSystem/EfreiRPC/master/VERSION")
    if r_version.status_code == 200:
        new_ver = r_version.text.strip()
        if new_ver != VERSION:
            print("Une mise à jour de EfreiRPC est disponible !")
            print("Mise à jour de EfreiRPC v" + VERSION + " vers v" + new_ver)
            r_main = requests.get("https://raw.githubusercontent.com/DocSystem/EfreiRPC/master/main.py")
            r_setup = requests.get("https://raw.githubusercontent.com/DocSystem/EfreiRPC/master/setup.py")
            r_update = requests.get("https://raw.githubusercontent.com/DocSystem/EfreiRPC/master/update.py")
            with open("main.py", "w") as f:
                f.write(r_main.text)
            with open("setup.py", "w") as f:
                f.write(r_setup.text)
            with open("update.py", "w") as f:
                f.write(r_update.text)
            with open("VERSION", "w") as f:
                f.write(new_ver)
            print("Mise à jour effectuée !")
            print("Veuillez relancer EfreiRPC.")
            exit(0)


if not os.path.exists(".DEV"):
    self_update()
