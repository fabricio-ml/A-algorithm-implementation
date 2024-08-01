class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  
        self.h = 0  
        self.f = 0  

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return f"Node({self.position}, g={self.g}, h={self.h}, f={self.f})"


def heuristic(current, end):
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


def astar_search(grid, start, end):
    open_list = []
    closed_list = []

    start_node = Node(start)
    end_node = Node(end)

    open_list.append(start_node)

    while open_list:
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if (0 <= node_position[0] < len(grid)) and (0 <= node_position[1] < len(grid[0])):
                if grid[node_position[0]][node_position[1]] == 0:
                    new_node = Node(node_position, current_node)
                    children.append(new_node)

        for child in children:
            if child in closed_list:
                continue

            child.g = current_node.g + 1
            child.h = heuristic(child.position, end_node.position)
            child.f = child.g + child.h

            if any(open_node for open_node in open_list if child == open_node and child.g > open_node.g):
                continue

            open_list.append(child)

    return None


def main():
    grid = [
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    end = (4, 5)

    path = astar_search(grid, start, end)
    if path:
        print(f"Path found: {path}")
    else:
        print("No path found")


if __name__ == "__main__":
    main()