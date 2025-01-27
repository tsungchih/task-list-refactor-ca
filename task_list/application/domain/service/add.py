from task_list.application.domain.model import ProjectName, ToDoList
from task_list.console import Console


class AddService:
    def __init__(self, todo_list: ToDoList, console: Console):
        self._todo_list = todo_list
        self._console = console

    def add(self, command_line: str) -> None:
        sub_command_rest = command_line.split(" ", 1)
        sub_command = sub_command_rest[0]
        if sub_command == "project":
            self._add_project(ProjectName(value=sub_command_rest[1]))
        elif sub_command == "task":
            project_task = sub_command_rest[1].split(" ", 1)
            self._add_task(ProjectName(value=project_task[0]), project_task[1])

    def _add_project(self, project_name: ProjectName) -> None:
        self._todo_list.add_project(project_name)

    def _add_task(self, project_name: ProjectName, description: str) -> None:
        project = self._todo_list.get_project(project_name)
        if project is None:
            self._console.print(f"Could not find a project with the name {project_name}.")
            self._console.print()
            return
        self._todo_list.add_task(project_name=project_name, description=description)
