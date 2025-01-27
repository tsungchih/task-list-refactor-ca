from task_list.console import Console


class HelpService:
    def __init__(self, console: Console):
        self._console = console

    def help(self) -> None:
        self._console.print("Commands:")
        self._console.print("  show")
        self._console.print("  add project <project name>")
        self._console.print("  add task <project name> <task description>")
        self._console.print("  check <task ID>")
        self._console.print("  uncheck <task ID>")
        self._console.print()
