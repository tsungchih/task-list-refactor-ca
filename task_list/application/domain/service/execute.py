from task_list.application.domain.model import TaskId, ToDoList
from task_list.application.domain.service.add import AddService
from task_list.application.domain.service.error import ErrorService
from task_list.application.domain.service.help import HelpService
from task_list.application.domain.service.setdone import SetDoneService
from task_list.application.domain.service.show import ShowService
from task_list.console import Console


class ExecuteService:
    def __init__(self, todo_list: ToDoList, console: Console):
        self._todo_list = todo_list
        self._console = console

    def execute(self, command_line: str) -> None:
        command_rest = command_line.split(" ", 1)
        command = command_rest[0]
        if command == "show":
            ShowService(todo_list=self._todo_list, console=self._console).show()
        elif command == "add":
            AddService(todo_list=self._todo_list, console=self._console).add(command_rest[1])
        elif command == "check":
            self._check(command_rest[1])
        elif command == "uncheck":
            self._uncheck(command_rest[1])
        elif command == "help":
            HelpService(console=self._console).help()
        else:
            ErrorService(console=self._console).error(command)

    def _check(self, task_id: str) -> None:
        SetDoneService(todo_list=self._todo_list).set_done(task_id=TaskId(value=task_id), done=True)

    def _uncheck(self, task_id: str) -> None:
        SetDoneService(todo_list=self._todo_list).set_done(task_id=TaskId(value=task_id), done=False)
