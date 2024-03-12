import threading
import time
import random
import os
import sys
import config


from colorama import Fore
from colorama import init as colorama_init
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout
from system import command_executor
from neverapi import core
from neverapi.core import Logger as nlog


def onEnable() -> None:
    config.MAIN_SESSION_UUID = core.generateSessionUUID()
    nlog.log("info", f"Запуск NEVER SYSTEM | Версия: {config.VERSION} | UUID Сессии: {config.MAIN_SESSION_UUID}")

if __name__ == "__main__":
    os.system('cls' if os.name=='nt' else 'clear')
    session = PromptSession()
    threading.Thread(target=onEnable, daemon=True).start()
    with patch_stdout(raw=True):
        while True:
            try:
                text = session.prompt(f"CMD > ")
                #print(f"Вы ввели: {text}")+
                match text:
                    case "/stop":
                        break
                    case "/restart":
                        pass
                    case _: 
                        command_executor.execute(text)
            except KeyboardInterrupt:
                break