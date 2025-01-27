from task_list.application.domain.model import ToDoList
from task_list.console import Console


class ShowService:
    def __init__(self, todo_list: ToDoList, console: Console):
        self._todo_list = todo_list
        self._console = console

    def show(self) -> None:
        for project in self._todo_list.projects:
            self._console.print(str(project.entity_id))
            for task in project.tasks:
                self._console.print(f"  [{'x' if task.is_done() else ' '}] {task.entity_id}: {task.description}")
            self._console.print()
