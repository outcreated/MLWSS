
from neverapi.core import Logger as nlog

class BaseCommand:
    def __init__(self, command, args: list[str]):
        self.command = command
        self.args = args  # Здесь можно инициализировать общие атрибуты для всех команд

    def execute(self):
        """
        Этот метод предназначен для переопределения в дочерних классах
        для выполнения специфической логики команды.

        :param args: Аргументы команды.
        """
        raise NotImplementedError("Метод execute() должен быть переопределен в дочерних классах!")

# Пример создания конкретной команды, наследуемой от BaseCommand
class PromoteCommand(BaseCommand):
    def execute(self):
        nlog.log('info', f"Пользователь {self.args[0]} успешно повышен до {self.args[2]} на срок {self.args[1]}.")
