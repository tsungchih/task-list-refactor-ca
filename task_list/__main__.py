import sys

from task_list.app import TaskList
from task_list.console import Console


def main():
    task_list = TaskList(Console(sys.stdin, sys.stdout))
    task_list.run()


if __name__ == "__main__":
    main()
