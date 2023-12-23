from dataclasses import dataclass
from typing import List,Dict, Tuple
from queue import SimpleQueue as Queue

@dataclass
class Edge:
    start: str
    end: str
    flow: int
    capacity: int

    @property
    def remaining_capacity(self):
        return self.capacity - self.flow
        


graph = [
    Edge("s", "0", 10, 10),
    Edge("s", "1", 0, 10),
    Edge("0", "2", 0, 25),
    Edge("1", "3", 0, 15),
    Edge("3", "0", 0, 6),
    Edge("3", "t", 10, 10),
    Edge("2", "t", 0, 10),
]

def find_augmenting_path(graph: List[Edge])-> List[Edge]:
    adjacency_list = get_adjacency_list(graph)
    indexed_graph = get_indexed_graph(graph)
    ancestry_map = {}
    vertex = 's'
    visited = set()
    visited.add(vertex)
    queue = Queue()
    queue.put(vertex)
    while not queue.empty():
        vertex = queue.get()
        path.append(vertex)
        neighbors = adjacency_list[vertex]
        for neighbor in neighbors:
            if neighbor not in visited and indexed_graph[(vertex, neighbor)].remaining_capacity >0 :
                queue.put(neighbor)
                visited.add(neighbor)
                ancestry_map[neighbor] = vertex
    path = [vertex]
    while vertex != 's':
        ancestor = ancestry_map[vertex]
        path.append(ancestor)
        vertex = ancestor
    return list(reversed(path))
    
    
def get_indexed_graph(graph: List[Edge]) -> Dict[Tuple[str,str], Edge]:
    result = {}
    for edge in graph:
        edge_tuple = (edge.start, edge.end)
        result[edge_tuple] = edge
    return result

def get_adjacency_list(graph:List[Edge]) -> Dict[Edge, List[Edge]]:
    result = {}
    for edge in graph:
        start_vertex = edge.start
        end_vertex = edge.end
        if start_vertex not in result:
            result[start_vertex] = []
        if end_vertex not in result:
            result[end_vertex] = []
        result[start_vertex].append(edge.end)
    return result

if __name__ == "__main__":
    ans =find_augmenting_path(graph)
    print(ans)