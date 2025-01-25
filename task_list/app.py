from task_list.application.domain.model import Project, ProjectName, Task, TaskId
from task_list.console import Console


class TaskList:
    QUIT = "quit"

    def __init__(self, console: Console) -> None:
        self.console = console
        self.last_id: int = 0
        self.tasks: dict[ProjectName, Project] = {}

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
            self.show()
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

    def show(self) -> None:
        for project_name, project in self.tasks.items():
            self.console.print(str(project_name))
            for task in project.tasks:
                self.console.print(f"  [{'x' if task.is_done() else ' '}] {task.entity_id}: {task.description}")
            self.console.print()

    def add(self, command_line: str) -> None:
        sub_command_rest = command_line.split(" ", 1)
        sub_command = sub_command_rest[0]
        if sub_command == "project":
            self.add_project(ProjectName(value=sub_command_rest[1]))
        elif sub_command == "task":
            project_task = sub_command_rest[1].split(" ", 1)
            self.add_task(ProjectName(value=project_task[0]), project_task[1])

    def add_project(self, project_name: ProjectName) -> None:
        self.tasks[project_name] = Project(entity_id=project_name)

    def add_task(self, project_name: ProjectName, description: str) -> None:
        project_tasks = self.tasks.get(project_name)
        if project_tasks is None:
            self.console.print(f"Could not find a project with the name {project_name}.")
            self.console.print()
            return
        project_tasks.add_task(Task(entity_id=self.next_id(), description=description, done=False))

    def check(self, task_id: str) -> None:
        self.set_done(TaskId(value=task_id), True)

    def uncheck(self, task_id: str) -> None:
        self.set_done(TaskId(value=task_id), False)

    def set_done(self, task_id: TaskId, done: bool) -> None:
        for _, project in self.tasks.items():
            for task in project.tasks:
                if task.entity_id == task_id:
                    task.set_done(done)
                    return
        self.console.print(f"Could not find a task with an ID of {task_id}")
        self.console.print()

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

    def next_id(self) -> TaskId:
        self.last_id += 1
        return TaskId(value=str(self.last_id))
