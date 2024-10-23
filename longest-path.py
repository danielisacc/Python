from collections import deque

class Edge:
    def __init__(self, name: str, weight: int, final_point: int):
        self.name = name
        self.weight = weight
        self.final_point = final_point

# Define the graph using a dictionary with lists
graph = {
    1: [Edge('A', 2, 2), Edge('B', 2, 3), Edge('C', 3, 4)],
    2: [Edge('D', 4, 5), Edge('E', 2, 3)],
    3: [Edge('F', 5, 5)],
    4: [Edge('G', 3, 6)],
    5: [Edge('I', 3, 7), Edge('H', 6, 6)],
    6: [Edge('J', 2, 7)],
    7: []  # Empty list for nodes with no edges
}

def longest_path_bfs(start_node):
    queue = deque([(start_node, 0, "")])  # (current_node, current_weight, path_string)
    highest_path = [0, ""]  # [weight, path_string]

    while queue:
        current_node, current_weight, path = queue.popleft()

        # Explore the edges from the current node
        for edge in graph.get(current_node, []):
            # Create the new path string with the edge included
            new_path = f"{path} -> {edge.name} (to {edge.final_point})" if path else f"{edge.name} (to {edge.final_point})"
            new_weight = current_weight + edge.weight
            
            # Check if it's a leaf node
            if edge.final_point not in graph or not graph[edge.final_point]:  # Check for empty list
                # Print the complete path and its weight
                print(f"Path: {new_path}, Total Weight: {new_weight}")

                # Check for the longest path
                if new_weight > highest_path[0]:  # Compare weights
                    highest_path = [new_weight, new_path]  # Update highest path
            
            # Enqueue the next node
            queue.append((edge.final_point, new_weight, new_path))

    return highest_path

# Example usage
start_node = 1
longest_path = longest_path_bfs(start_node)

# Output the longest path
print("\nLongest path from node", start_node, ":", longest_path[1], "with total weight:", longest_path[0])
