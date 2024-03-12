from system import commands
from colorama import Fore as clr
from neverapi.core import Logger as nlog


command_syntax = {
    "/help"     :     [0, ""],
    "/promote"  :     [3, "<telegram_id> <duration> <admin_level>"],
    "/demote"   :     [1, "<telegram_id>"],
    "/stop"     :     [0, ""],
    "/restart"  :     [0, ""]
}

def execute(command: str) -> str:
    parts = command.split()

    if len(parts) == 0:
        nlog.log('error', "Неизвестная команда, введите /help для получения информации")
        return
    
    command = parts[0]
    arguments = parts[1:]

    if len(arguments) < command_syntax[command][0]:
        nlog.log('error', f"Ошибка синтаксиса. Попробуйте: {format_command(command)} {format_args(command_syntax[command][1])}")
        return
    
    match command:
        case "/promote":
            commands.PromoteCommand(command, arguments).execute()

def format_command(command: str) -> str:
    return command.replace(command, f"{clr.RED}{command}{clr.RESET}")

def format_args(args: str) -> str:
    return args.replace("<", f"{clr.YELLOW}<{clr.CYAN}").replace(">", f"{clr.YELLOW}>{clr.RESET}")

