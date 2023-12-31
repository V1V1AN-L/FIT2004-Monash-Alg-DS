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
    def __init__(self, max_size):
        self.queue = [None for _ in range(max_size)]
        self.rear = 0
        self.front = 0

    def push(self, vertex: int):
        self.queue[self.rear] = vertex
        self.rear += 1

    def pop(self):
        res = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        return res

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False
class Edge:
    def __init__(self, capacity, flow, source, sink):
        self.capacity = capacity
        self.flow = flow
        self.source = source
        self.sink = sink
        self.reverse_edge = None


# index: since each vertex will be break into 2 vertices, the actual vertex index * 2 = vertex(in), actual vertex index * 2 + 1 = vertex(out)
# connections stores each actual edge capacity, while the maxOut stores the actual capacity a vertex can take
class Graph:
    def __init__(self, connections, maxIn, maxOut, origin, targets):
        self.length = len(maxIn) * 2
        # self.graph = [[0 for _ in range(self.length)] for _ in range(self.length)]
        self.graph = [[]for _ in range(self.length)]

        for i in range(len(maxOut)):
            if maxOut[i]<= maxIn[i]:
                edge = Edge(maxOut[i], 0, i*2, i*2+1)
            else:
                edge = Edge(maxIn[i], 0, i*2, i*2+1)

            reverse_edge = Edge(0, 0, i*2+1, i*2)
            edge.reverse_edge = reverse_edge
            reverse_edge.reverse_edge = edge
            self.graph[i*2].append(edge)
            self.graph[i*2+1].append(reverse_edge)

        for each_connection in connections:
            start = each_connection[0]
            end = each_connection[1]
            capacity = each_connection[2]
            edge = Edge(capacity, 0, start*2+1, end*2)
            reverse_edge = Edge(0, 0, end*2, start*2+1)
            edge.reverse_edge = reverse_edge
            reverse_edge.reverse_edge = edge
            self.graph[start*2+1].append(edge)
            self.graph[end*2].append(reverse_edge)

        for target in targets:
            self.graph[target*2][0].capacity = maxIn[target]
        self.graph[origin*2][0].capacity = maxOut[origin]

def bfs(start:int, num_of_vertex, graph:Graph):
    preq = [None for _ in range(num_of_vertex)]

    queue = Queue(num_of_vertex)
    queue.push(start)
    while queue.is_empty() == False:
        current_vertex = queue.pop()
        for each_edge in graph.graph[current_vertex]:
            if preq[each_edge.sink]== None and each_edge.sink != start and each_edge.capacity > each_edge.flow:
                preq[each_edge.sink] = each_edge
                queue.push(each_edge.sink)
    return preq

def maxThroughput(connections, maxIn, maxOut, origin, targets):
    max_flow = 0
    processed_graph = Graph(connections,maxIn,maxOut, origin, targets)
    able_to_find_path = True
    while able_to_find_path == True:
        able_to_find_path = False
        preq_res = bfs(origin*2, processed_graph.length, processed_graph)

        for target in targets:
            if preq_res[target*2+1] != None:
                able_to_find_path = True
                bottleneck_flow = float('inf')
                path_edge = preq_res[target*2+1]
                while path_edge != None:
                    bottleneck_flow = min(bottleneck_flow, path_edge.capacity - path_edge.flow)
                    path_edge = preq_res[path_edge.source]

                path_edge = preq_res[target*2+1]
                while path_edge != None:
                    path_edge.flow += bottleneck_flow
                    path_edge.reverse_edge.flow -= bottleneck_flow
                    path_edge = preq_res[path_edge.source]

                max_flow += bottleneck_flow
                break
    # for j in range(len(processed_graph.graph)):
    #     for k in range(len(processed_graph.graph[j])):
    #         print(processed_graph.graph[k].capacity)

    return max_flow


# D = 5, C = 6, max_throughput = 15
# connections = [(2, 4, 4), (4, 0, 11), (2, 1, 5), (4, 3, 8), (1, 0, 7), (3, 2, 9)]
# maxIn = [2, 15, 12, 13, 3]
# maxOut = [7, 10, 6, 9, 3]
# origin = 2
# targets = [0, 3]
# print(maxThroughput(connections, maxIn, maxOut, origin, targets))
# self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 5)


class Node:
    def __init__(self, char):
        self.char = char
        self.parent = None
        self.childen_freq = [0 for _ in range(27)]
        self.childen = [None for _ in range(27)]
        self.highest_child = None
        self.freq = 0
class CatsTrie:
    def __init__(self, sentences):
        self.root_node = Node(" ")
        for sentence in sentences: # "abc"
            current_node = self.root_node
            for i in range(len(sentence)): #'a'
                index = ord(sentence[i]) - 96  # 0
                if current_node.childen[index] == None:
                    child_node = Node(sentence[i])
                    current_node.childen[index] = child_node
                    child_node.parent = current_node
                current_node = current_node.childen[index]

            if current_node.childen[0] == None:
                end_node = Node("")
                end_node.parent = current_node
                current_node.childen[0] = end_node
            current_node.childen[0].freq += 1

            index = 0
            for j in range(len(sentence)+1):
                current_node.childen_freq[index] = current_node.childen[index].freq
                highest_freq = max(current_node.childen_freq)
                current_node.freq = highest_freq
                highest_freq_index = current_node.childen_freq.index(highest_freq)
                current_node.highest_child = current_node.childen[highest_freq_index]
                current_node = current_node.parent
                index = ord(sentence[len(sentence)-j-1]) - 96

    def autoComplete(self, prompt):
        current_node = self.root_node
        res = []
        if len(prompt) != 0:
            for char in prompt:
                index = ord(char) - 96
                if current_node.childen[index] != None:
                    res.append(char)
                    current_node = current_node.childen[index]
                else:
                    return None
        check_freq=current_node.freq
        while current_node.freq == check_freq and current_node.highest_child is not None:
            res.append(current_node.highest_child.char)
            current_node = current_node.highest_child
        res_str = "".join(res)
        return res_str

# sentences = ["ab", "a", "abc", "abd"]
# trie = CatsTrie(sentences)
# print(trie.autoComplete(""))
# self.assertTrue(trie.autoComplete("ab") == "abazacy")