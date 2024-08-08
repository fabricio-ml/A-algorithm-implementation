# Define a Node class to represent positions in the grid
class Node:
    # Initialize a Node with position and optional parent
    def __init__(self, position, parent=None):
        self.position = position  # Current position (x, y)
        self.parent = parent      # Parent node
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic (estimated cost from current node to end)
        self.f = 0  # Total cost (g + h)

    # Define equality for Node objects based on their positions
    def __eq__(self, other):
        return self.position == other.position

    # Define less than comparison for Node objects based on f value
    def __lt__(self, other):
        return self.f < other.f

    # Define string representation of Node objects
    def __repr__(self):
        return f"Node({self.position}, g={self.g}, h={self.h}, f={self.f})"

# Define heuristic function (Manhattan distance)
def heuristic(current, end):
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

# A* search algorithm implementation
def astar_search(grid, start, end):
    open_list = []    # List of nodes to be evaluated
    closed_list = []  # List of nodes already evaluated
    start_node = Node(start)  # Create start node
    end_node = Node(end)      # Create end node
    open_list.append(start_node)  # Add start node to open list

    # Main loop of A* algorithm
    while open_list:
        # Get node with lowest f value from open list
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)  # Remove current node from open list
        closed_list.append(current_node)  # Add current node to closed list

        # Check if we've reached the end node
        if current_node == end_node:
            path = []
            current = current_node
            while current:  # Reconstruct path
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        children = []  # List to store valid neighbor nodes
        # Check all adjacent squares
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range of grid
            if (0 <= node_position[0] < len(grid)) and (0 <= node_position[1] < len(grid[0])):
                # Make sure walkable terrain
                if grid[node_position[0]][node_position[1]] == 0:
                    new_node = Node(node_position, current_node)
                    children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list
            if child in closed_list:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = heuristic(child.position, end_node.position)
            child.f = child.g + child.h

            # Child is already in the open list
            if any(open_node for open_node in open_list if child == open_node and child.g > open_node.g):
                continue

            # Add the child to the open list
            open_list.append(child)

    # No path found
    return None

# Main function to run the A* algorithm
def main():
    # Define the grid (0 is walkable, 1 is obstacle)
    grid = [
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    start = (0, 0)  # Start position
    end = (4, 5)    # End position

    # Run A* search
    path = astar_search(grid, start, end)

    # Print result
    if path:
        print(f"Path found: {path}")
    else:
        print("No path found")

# Run main function if script is executed directly
if __name__ == "__main__":
    main()
