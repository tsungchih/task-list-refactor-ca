from contextlib import suppress

from pydantic import Field
from task_list.application.domain.model.base import Entity, ValueObject
from task_list.application.domain.model.task import Task, TaskId


class ProjectName(ValueObject):
    value: str = Field(..., description="Project name.")

    def __str__(self) -> str:
        return self.value


class Project(Entity[ProjectName]):
    tasks: list[Task] = Field(default_factory=list, description="The tasks in this project.")

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def has_task(self, task_id: TaskId) -> bool:
        task = None
        with suppress(StopIteration):
            task = next(filter(lambda task: task.entity_id == task_id, self.tasks))
        return task is None
