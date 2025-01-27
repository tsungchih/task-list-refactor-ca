from pydantic import Field, PrivateAttr
from task_list.application.domain.model.base import Entity, ValueObject
from task_list.application.domain.model.project import Project, ProjectName
from task_list.application.domain.model.task import Task, TaskId


class ToDoListId(ValueObject):
    value: str = Field(..., description="The todo list ID.")

    def __str__(self) -> str:
        return self.value


class ToDoList(Entity[ToDoListId]):
    projects: list[Project] = Field(default_factory=list, description="The projects.")
    _last_task_id: int = PrivateAttr(default=0)

    def add_project(self, project_name: ProjectName, /) -> None:
        self.projects.append(Project(entity_id=project_name))

    def add_task(self, project_name: ProjectName, description: str, done: bool = False) -> None:
        if project := self.get_project(project_name):
            project.add_task(Task(entity_id=self._next_task_id(), description=description, done=done))

    def get_project(self, project_name: ProjectName, /) -> Project | None:
        try:
            project = next(filter(lambda project: project.entity_id == project_name, self.projects))
        except StopIteration:
            return None
        return project

    def set_done(self, task_id: TaskId, done: bool) -> None:
        """Set the state of done for the given `task_id`.

        Args:
            task_id (TaskId): The task ID to set the state of done.
            done (bool): The target state of done.
        """
        for project in self.projects:
            if project.get_task(task_id):
                project.set_task_done(task_id=task_id, done=done)

    def _next_task_id(self) -> TaskId:
        self._last_task_id += 1
        return TaskId(value=str(self._last_task_id))
