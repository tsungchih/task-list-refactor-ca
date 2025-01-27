from task_list.application.domain.model import ToDoList, ToDoListId
from task_list.application.domain.service import ExecuteService
from task_list.console import Console


class TaskList:
    QUIT = "quit"
    DEFAULT_TODO_LIST_ID = "001"

    def __init__(self, console: Console) -> None:
        self.console = console
        self.todo_list: ToDoList = ToDoList(entity_id=ToDoListId(value=self.DEFAULT_TODO_LIST_ID))

    def run(self) -> None:
        while True:
            command = self.console.input("> ")
            if command == self.QUIT:
                break
            ExecuteService(todo_list=self.todo_list, console=self.console).execute(command)
