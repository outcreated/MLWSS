from colorama import Fore as clr
from datetime import datetime as dt
import enum
import random

def getTimeStamp() -> str:
    return dt.now().strftime('%H:%M:%S')

def generateSessionUUID() -> str:
    alphabet = '1234567890qwertyuiopasdfghjklzxcvbnm'
    uuid = ''

    for i in range(0, len(alphabet)):
        if i % 8: 
            uuid += '-' 
            continue

        uuid += alphabet[random.randint(0, len(alphabet)-1)]
    
    return uuid

class LogLevel(enum.Enum):
    INFO: 10
    WARN: 20
    ERROR: 30
    FATAL: 40
    DEBUG: 50


class Logger():
    def log(level: LogLevel, text: str) -> None:
        """
        param: level -> (`INFO`, `WARN`, `ERROR`, `FATAL`, `DEBUG`);
        param: text -> Any text
        """
        match level:
            case LogLevel.INFO:
                print(f"{clr.RESET}[{clr.YELLOW}{getTimeStamp()}{clr.RESET}] [{clr.CYAN}INFO{clr.RESET}] {text}{clr.RESET}")
            case LogLevel.WARN:
                print(f"{clr.RESET}[{clr.YELLOW}{getTimeStamp()}{clr.RESET}] [{clr.YELLOW}WARNING{clr.RESET}] {text}{clr.RESET}")
            case LogLevel.ERROR:
                print(f"{clr.RESET}[{clr.YELLOW}{getTimeStamp()}{clr.RESET}] [{clr.RED}ERROR{clr.RESET}] {text}{clr.RESET}")
            case LogLevel.FATAL:
                print(f"{clr.RESET}[{clr.YELLOW}{getTimeStamp()}{clr.RESET}] [{clr.MAGENTA}FATAL{clr.RESET}] {text}{clr.RESET}")
            case LogLevel.DEBUG:
                print(f"{clr.RESET}[{clr.YELLOW}{getTimeStamp()}{clr.RESET}] [{clr.GREEN}DEBUG{clr.RESET}] {text}{clr.RESET}")
        