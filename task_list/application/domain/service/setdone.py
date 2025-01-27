from task_list.application.domain.model import TaskId, ToDoList


class SetDoneService:
    def __init__(self, todo_list: ToDoList):
        self._todo_list = todo_list

    def set_done(self, task_id: TaskId, done: bool) -> None:
        self._todo_list.set_done(task_id=task_id, done=done)
