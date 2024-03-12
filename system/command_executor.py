from colorama import Fore as clr

def execute(command: str) -> str:
    command_name = command.replace("/", "").split(" ")[0]
    arguments = command.replace("/" + command_name + " ", "").split(" ")

    match command_name:
        case "help":
            return "Список команд"
        case "promote":
            if len(arguments) == 1:
                return f"{clr.RED}[Ошибка]: {clr.WHITE}Введите ID пользователя, которого хотите назначить администратором"
            if len(arguments) == 2:
                return f"[Ошибка]: Введите срок, на который хотите назначить администратора. Пример: 1S, 1M, 1H, 1D, 1MO, 1Y"
        case "demote":
            pass
        case _:
            return "[Ошибка]: Неизвестная команда. Для просмотра списка команд наберите /help"
    return command_name + str(arguments)