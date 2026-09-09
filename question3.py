import json
from collections import deque
from pathlib import Path


def load_data(file_name="appendix_a.json"):
    path = Path(__file__).with_name(file_name)

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def depth_first(nodes):
    """
    Pre-order depth-first traversal.
    Yields: (node, depth)
    """
    for node in nodes:
        yield node, 0

        children = node.get("children", [])
        for child, depth in _depth_first_children(children, 1):
            yield child, depth


def _depth_first_children(nodes, depth):
    for node in nodes:
        yield node, depth

        children = node.get("children", [])
        yield from _depth_first_children(children, depth + 1)


def breadth_first(nodes):
    """
    Breadth-first traversal.
    Yields: (node, depth)
    """
    queue = deque((node, 0) for node in nodes)

    while queue:
        node, depth = queue.popleft()
        yield node, depth

        for child in node.get("children", []):
            queue.append((child, depth + 1))


def print_traversal(items):
    for node, depth in items:
        suffix = "/" if node["type"] == "folder" else ""
        print(f'{"    " * depth}{node["name"]}{suffix}')


if __name__ == "__main__":
    data = load_data()

    print("DEPTH FIRST")
    print_traversal(depth_first(data))

    print("\nBREADTH FIRST")
    print_traversal(breadth_first(data))
