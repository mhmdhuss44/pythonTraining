from collections import defaultdict, deque

class GraphBfs:
    def __init__(self):
        # we use this to handle searching for akey that doesnt exist and adding it
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def shortest_path(self, start, end):
        # Initialize a queue for BFS and a dictionary to store visited nodes
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            # popping the first element in the queue
            current, path = queue.popleft()
            # if we reached the end
            if current == end:
                return path
            # we add the current node to the visited array to mark it as visited
            if current not in visited:
                visited.add(current)

                # we add adjacent nodes with updated path
                for neighbor in self.graph[current]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        # If we didntt find a path
        return None

if __name__ == '__main__':
    graph = GraphBfs()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)
    graph.add_edge(3, 7)
    graph.add_edge(4, 8)
    graph.add_edge(5, 9)

    start_node = 1
    end_node = 9

    shortest_path_result = graph.shortest_path(start_node, end_node)

    if shortest_path_result:
        print(f"Shortest path between {start_node} and {end_node}: {shortest_path_result}")
    else:
        print(f"No path found between {start_node} and {end_node}")
