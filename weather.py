import os
import time

try:
    import requests
except Exception as e:
    print(
        "Please install the requests library, you can do this by (pip install requests)\nAdvanced Error Details: " + str(
            e))
    exit(1)


class termColors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[97m'


lastUpdated = ""
lastWorking = ""


def fail(message):
    clear_console()
    print(f"{termColors.BLUE}Last Updated: {lastUpdated}")
    print(lastWorking)
    print(f"{termColors.RED}Error fetching weather data due to " + message)
    time.sleep(10)


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        os.system('clear')
    except:
        pass


clear_console()
print(f"{termColors.CYAN}Loading.....")
clear_console()
while True:
    try:
        response = requests.get("https://wttr.in")
        if response.status_code == 200 and response.text != lastWorking:
            lastUpdated = time.strftime("%Y-%m-%d %H:%M:%S")
            lastWorking = response.text
            clear_console()
            print(f"{termColors.WHITE}Last Updated: {lastUpdated}")
            print(response.text)
            time.sleep(180)
        elif response.status_code != 200:
            fail("Due to Status Code of " + str(response.status_code))
    except Exception as e:
        fail(str(e))
