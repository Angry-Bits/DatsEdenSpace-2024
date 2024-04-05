from pprint import pprint
from typing import Dict, List


GarbageType = Dict[str, List[List[int]]]
ContainerType = Dict[int, Dict[int, bool]]


def get_mock_garbage() -> GarbageType:
    return {
        "6fTzQid": [
            [0, 0],
            [0, 1],
            [1, 1]
        ],
        "RVnTkM59": [
            [0, 0],
            [0, 1],
            [1, 1],
            [2, 1],
            [1, 2]
        ]
    }


def get_empty_trash_container(
    capacity_x: int = 1,
    capacity_y: int = 1
) -> ContainerType:
    container = {}
    for i in range(capacity_x):
        inner_dict = {}
        for j in range(capacity_y):
            inner_dict[j] = False
        container[i] = inner_dict
    return container


def push_trash_to_container(
    garbage: GarbageType,
    container: ContainerType
) -> ContainerType:
    # Сортируем объекты по убыванию их размеров (по количеству ячеек)
    sorted_garbage = sorted(garbage.values(), key=lambda obj: len(obj), reverse=True)

    # Проходим по каждому объекту
    for obj_cells in sorted_garbage:
        # Пытаемся разместить объект в первое подходящее место в контейнере
        placed = False
        for y in range(len(container)):
            for x in range(len(container[0])):
                if can_place_object(container, obj_cells, x, y):
                    place_object(container, obj_cells, x, y)
                    placed = True
                    break
            if placed:
                break
    return container


def can_place_object(
    container: ContainerType,
    obj_cells: List[List[int]],
    x_start: int,
    y_start: int
) -> bool:
    max_x = len(container[0])
    max_y = len(container)
    for x, y in obj_cells:
        if x + x_start >= max_x or y + y_start >= max_y:
            return False
        if container[y + y_start][x + x_start]:
            return False
    return True


def place_object(
    container: ContainerType,
    obj_cells: List[List[int]],
    x_start: int,
    y_start: int
) -> None:
    for x, y in obj_cells:
        container[y + y_start][x + x_start] = True


def tetris() -> ContainerType:
    container = get_empty_trash_container(8, 11)
    garbage = get_mock_garbage()
    push_trash_to_container(garbage, container)
    return container


if __name__ == '__main__':
    pprint(tetris())
