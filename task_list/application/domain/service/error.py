from task_list.console import Console


class ErrorService:
    def __init__(self, console: Console):
        self._console = console

    def error(self, command: str) -> None:
        self._console.print(f"I don't know what the command {command} is.")
        self._console.print()
