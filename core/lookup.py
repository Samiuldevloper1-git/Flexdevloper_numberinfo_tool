import requests
import time
import os

from colorama import Fore

from core.banner import banner
from core.loading import loading
from core.nodata import no_data

from data.config import API_URL, API_KEY

SAVE_FOLDER = "Flex-NumberInfo-Tool"

if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

def save_result(user):

    name = user.get("name", "Not Found")
    fname = user.get("fname", "Not Found")
    mobile = user.get("mobile", "Not Found")
    circle = user.get("circle", "Not Found")
    address = user.get("address", "Not Found")
    email = user.get("email", "Not Found")
    uid = user.get("id", "Not Found")

    file_path = f"{SAVE_FOLDER}/{mobile}.txt"

    with open(file_path, "w", encoding="utf-8") as file:

        file.write(f"""
╔══════════════════════════════════╗
║          NUMBER RESULT          ║
╚══════════════════════════════════╝

Name      : {name}
Father    : {fname}
Mobile    : {mobile}
Circle    : {circle}

Address   :
{address}

Email     : {email}
ID        : {uid}

━━━━━━━━━━━━━━━━━━━━━━━━━━
Credit : Samiul Devloper
━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

def show_result(data):

    results = data.get("results", {})

    found = False

    for key in results:

        if key == "credit":
            continue

        user = results[key]

        found = True

        name = user.get("name", "Not Found")
        fname = user.get("fname", "Not Found")
        mobile = user.get("mobile", "Not Found")
        circle = user.get("circle", "Not Found")
        address = user.get("address", "Not Found")
        email = user.get("email", "Not Found")
        uid = user.get("id", "Not Found")

        print(Fore.GREEN + "\n╔══════════════════════════════════╗")
        print(Fore.GREEN + "║          NUMBER RESULT          ║")
        print(Fore.GREEN + "╚══════════════════════════════════╝\n")

        print(Fore.WHITE + f"[+] Name      : {name}")
        print(Fore.WHITE + f"[+] Father    : {fname}")
        print(Fore.WHITE + f"[+] Mobile    : {mobile}")
        print(Fore.WHITE + f"[+] Circle    : {circle}")

        print(Fore.WHITE + f"\n[+] Address   :")
        print(Fore.CYAN + f"{address}")

        print(Fore.WHITE + f"\n[+] Email     : {email}")
        print(Fore.WHITE + f"[+] ID        : {uid}")

        print(Fore.MAGENTA + "\n━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(Fore.YELLOW + " Credit : Samiul Devloper")
        print(Fore.MAGENTA + "━━━━━━━━━━━━━━━━━━━━━━━━━━")

        save_result(user)

        print(Fore.GREEN + f"\n[✓] Saved : {SAVE_FOLDER}/{mobile}.txt")

    if not found:
        no_data()

def lookup():

    while True:

        banner()

        number = input(
            Fore.GREEN + "\nEnter Number : "
        )

        if not number:
            continue

        loading()

        try:

            response = requests.get(
                f"{API_URL}?phone={number}&key={API_KEY}",
                timeout=20
            )

            data = response.json()

            if data.get("success") and data.get("count", 0) > 0:
                show_result(data)

            else:
                no_data()

        except Exception as e:
            print(Fore.RED + f"\n[✗] Error : {e}")

        print(Fore.CYAN + "\n[1] Search Another Number")
        print(Fore.CYAN + "[2] Exit Tool")

        option = input(
            Fore.YELLOW + "\nSelect Option : "
        )

        if option == "1":
            continue

        elif option == "2":

            print(Fore.GREEN + "\n[✓] Exiting Tool...")
            time.sleep(1)

            break
