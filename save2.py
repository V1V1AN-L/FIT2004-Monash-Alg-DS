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

                if i == len(sentence)-1:
                    current_node.childen[index].freq += 1
                    current_node = current_node.childen[index]
                    if current_node.childen[0] == None:
                        child_node = Node("")
                        child_node.freq += 1
                        child_node.parent = current_node
                        current_node.childen[0] = child_node
                    else:
                        current_node.childen[0].freq += 1
                    for j in range(len(sentence)+1):
                        if j == 0:
                            index = 0
                        else:
                            index = ord(sentence[len(sentence)-j])-96
                        current_node.childen_freq[index] = current_node.childen[index].freq
                        highest_freq = max(current_node.childen_freq)
                        current_node.freq = highest_freq
                        highest_freq_index = current_node.childen_freq.index(highest_freq)
                        current_node.highest_child = current_node.childen[highest_freq_index]
                        current_node = current_node.parent
                    break
                current_node = current_node.childen[index]

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