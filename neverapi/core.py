from colorama import Fore as clr
from datetime import datetime as dt
import enum
import random

def getTimeStamp() -> str:
    return dt.now().strftime('%H:%M:%S')

def generateSessionUUID() -> str:
    alphabet = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    uuid = ''

    for i in range(0, 32):
        if i % 8 == 0 and i != 0: 
            uuid += '-' 
            continue

        uuid += alphabet[random.randint(0, len(alphabet)-1)]
    
    return uuid

class Logger():
    def log(level: str, text: str) -> None:
        """
        param: level -> (`INFO`, `WARN`, `ERROR`, `FATAL`, `DEBUG`);
        param: text -> Any text
        """
        match level.upper():
            case "INFO":
                print(f"{clr.RESET}[{clr.YELLOW}{getTimeStamp()}{clr.RESET}] [{clr.CYAN}INFO{clr.RESET}] {text}{clr.RESET}")
            case "WARN":
                print(f"{clr.RESET}[{clr.YELLOW}{getTimeStamp()}{clr.RESET}] [{clr.YELLOW}WARNING{clr.RESET}] {text}{clr.RESET}")
            case "ERROR":
                print(f"{clr.RESET}[{clr.YELLOW}{getTimeStamp()}{clr.RESET}] [{clr.RED}ERROR{clr.RESET}] {text}{clr.RESET}")
            case "FATAL":
                print(f"{clr.RESET}[{clr.YELLOW}{getTimeStamp()}{clr.RESET}] [{clr.MAGENTA}FATAL{clr.RESET}] {text}{clr.RESET}")
            case "DEBUG":
                print(f"{clr.RESET}[{clr.YELLOW}{getTimeStamp()}{clr.RESET}] [{clr.GREEN}DEBUG{clr.RESET}] {text}{clr.RESET}")
        