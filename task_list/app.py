from task_list.application.domain.model import TaskId, ToDoList, ToDoListId
from task_list.application.domain.service import AddService, HelpService, ShowService
from task_list.console import Console


class TaskList:
    QUIT = "quit"
    DEFAULT_TODO_LIST_ID = "001"

    def __init__(self, console: Console) -> None:
        self.console = console
        self.last_id: int = 0
        self.todo_list: ToDoList = ToDoList(entity_id=ToDoListId(value=self.DEFAULT_TODO_LIST_ID))

    def run(self) -> None:
        while True:
            command = self.console.input("> ")
            if command == self.QUIT:
                break
            self.execute(command)

    def execute(self, command_line: str) -> None:
        command_rest = command_line.split(" ", 1)
        command = command_rest[0]
        if command == "show":
            ShowService(todo_list=self.todo_list, console=self.console).show()
        elif command == "add":
            AddService(todo_list=self.todo_list, console=self.console).add(command_rest[1])
        elif command == "check":
            self.check(command_rest[1])
        elif command == "uncheck":
            self.uncheck(command_rest[1])
        elif command == "help":
            HelpService(console=self.console).help()
        else:
            self.error(command)

    def check(self, task_id: str) -> None:
        self.todo_list.set_done(task_id=TaskId(value=task_id), done=True)

    def uncheck(self, task_id: str) -> None:
        self.todo_list.set_done(task_id=TaskId(value=task_id), done=False)

    def error(self, command: str) -> None:
        self.console.print(f"I don't know what the command {command} is.")
        self.console.print()
