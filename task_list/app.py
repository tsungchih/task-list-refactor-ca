from task_list.application.domain.model import ProjectName, TaskId, ToDoList, ToDoListId
from task_list.application.domain.service import ShowService
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
            self.add(command_rest[1])
        elif command == "check":
            self.check(command_rest[1])
        elif command == "uncheck":
            self.uncheck(command_rest[1])
        elif command == "help":
            self.help()
        else:
            self.error(command)

    def add(self, command_line: str) -> None:
        sub_command_rest = command_line.split(" ", 1)
        sub_command = sub_command_rest[0]
        if sub_command == "project":
            self.add_project(ProjectName(value=sub_command_rest[1]))
        elif sub_command == "task":
            project_task = sub_command_rest[1].split(" ", 1)
            self.add_task(ProjectName(value=project_task[0]), project_task[1])

    def add_project(self, project_name: ProjectName) -> None:
        self.todo_list.add_project(project_name)

    def add_task(self, project_name: ProjectName, description: str) -> None:
        project = self.todo_list.get_project(project_name)
        if project is None:
            self.console.print(f"Could not find a project with the name {project_name}.")
            self.console.print()
            return
        self.todo_list.add_task(project_name=project_name, description=description)

    def check(self, task_id: str) -> None:
        self.todo_list.set_done(task_id=TaskId(value=task_id), done=True)

    def uncheck(self, task_id: str) -> None:
        self.todo_list.set_done(task_id=TaskId(value=task_id), done=False)

    def help(self) -> None:
        self.console.print("Commands:")
        self.console.print("  show")
        self.console.print("  add project <project name>")
        self.console.print("  add task <project name> <task description>")
        self.console.print("  check <task ID>")
        self.console.print("  uncheck <task ID>")
        self.console.print()

    def error(self, command: str) -> None:
        self.console.print(f"I don't know what the command {command} is.")
        self.console.print()
