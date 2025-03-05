"""This python file will edit the tasklist in data.db."""

from sqlite3 import connect, Connection, Cursor, Error


async def add_task(
    task_name: str,
    task_description: str,
    task_type: str,  # Either: group or individual.
    assigner_id: int,
    assign_id: int,
    group_id: int = 0
) -> bool:
    """This will add the task."""
    return True


async def edit_task(
    task_id: int,
    task_name: str,
    task_description: str,
    task_type: str,  # Either: group, individual, or self.
    assigner_id: int,
    assign_id: int,
    group_id: int = 0
) -> bool:
    return True


async def get_task(
    task_name: str,
    task_type: str,  # Either: group, individual, or self.
    assigner_id: int,
    assign_id: int,
    group_id: int = 0
) -> dict[str, str]:
    return {}


if __name__ == "__main__":
    print("This is a 'task_editor' module, please run 'main.py'. Exiting...")