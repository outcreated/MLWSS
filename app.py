import os
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout
from system import command_executor

import threading
import time
import random

alphabet = "1234567890-=!@#$%^&*_+qwertyuiopasdfghjklzxcvbnm?~"


def print_messages():
    """Функция для демонстрации вывода системных сообщений."""
    for i in range(100000):
        time.sleep(2)
        message = f""
        for i in range(0, 32):
            message += alphabet[random.randint(1, len(alphabet)-1)]
        print(f"Системное сообщение:\t\t{message}")

if __name__ == "__main__":
    os.system("clear")
    session = PromptSession()
    threading.Thread(target=print_messages, daemon=True).start()
    with patch_stdout():
        while True:
            try:
                text = session.prompt(f">>> ")
                #print(f"Вы ввели: {text}")
                match text:
                    case "/stop":
                        break
                    case "/restart":
                        pass
                    case _: 
                        print(command_executor.execute(text))
            except KeyboardInterrupt:
                break