from colorama import Fore
import time

def loading():

    print(Fore.YELLOW + "\n[•] Connecting Secure Server...")
    time.sleep(1)

    print(Fore.YELLOW + "[•] Searching Leak Database...")
    time.sleep(1)

    print(Fore.GREEN + "[✓] Database Connected")
    time.sleep(1)
