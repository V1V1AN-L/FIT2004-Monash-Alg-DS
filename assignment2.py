# # Example
# connections = [(0, 1, 3000), (1, 2, 2000), (1, 3, 1000)
# (0, 3, 2000), (3, 4, 2000), (3, 2, 1000)]
# maxIn = [5000, 3000, 3000, 3000, 2000]
# maxOut = [5000, 3000, 3000, 2500, 1500]
# origin = 0
# targets = [4, 2]
# # Your function should return the maximum possible data throughput from the
# # data centre origin to the data centres specified in targets.
# >>> maxThroughput(connections, maxIn, maxOut, origin, targets)
# 4500
# Define a Vertex to store its value


class Queue:
    def __init__(self, max_size: int):
        self.queue = [None for _ in range (max_size)]
        self.rear = 0
        self.front = 0

    def push(self, vertex: int):
        self.queue[self.rear] = vertex
        self.rear += 1

    def pop(self):
        res = self.queue[self.front]
        self.front += 1
        return res

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False


# index: since each vertex will be break into 2 vertices, the actual vertex index * 2 = vertex(in), actual vertex index * 2 + 1 = vertex(out)
# connections stores each actual edge capacity, while the maxOut stores the actual capacity a vertex can take
class Graph:
    def __init__(self, connections, maxIn, maxOut):
        self.length = len(maxIn) * 2
        self.graph = [[0 for _ in range(self.length)]for _ in range (self.length)]

        for i in range(len(maxOut)):
            self.graph[i*2][i*2+1] = maxOut[i]

        for each_connection in connections:
            start = each_connection[0]
            end = each_connection[1]
            capacity = each_connection[2]
            self.graph[start*2+1][end*2] = capacity


def bfs(start: int, target: list[int], num_of_vertex: int):
    preq = [None for _ in range(num_of_vertex)]
    queue = Queue(num_of_vertex)
    queue.push(start)
    while queue.is_empty() == False:
        current_vertex = queue.pop()

