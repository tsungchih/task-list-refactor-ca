from pydantic import Field
from task_list.application.domain.model import Entity, ValueObject


class TaskId(ValueObject):
    value: str = Field(..., description="The task ID.")

    def __str__(self) -> str:
        return self.value


class Task(Entity[TaskId]):
    description: str = Field(..., description="The description for the task.")
    done: bool = Field(..., description="Indicates whether the task is done.")

    def set_done(self, done: bool) -> None:
        self.done = done

    def is_done(self) -> bool:
        return self.done
