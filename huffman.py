# 1 make a tree with left and right nodes
# 2 count frequency
# 3 sort frequency into a list from lowest to highest
#       - sorting it will allow us to choose from the next lowest freq
# 4 take first two nodes and add them together
# 5 create new node of these two nodes


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def left(self):
        return self.left

    def right(self):
        return self.right


def count_frequency(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


# sorts the frequencies in the dictionary and converts it to a list
def sort_frequency(freq):
    sorted_freq_list = sorted(freq.items(), key=lambda x: x[1])
    return sorted_freq_list


# create new node with lowest freq
# new node to back of list
# use sorted() to sort the nodes
# creates the binary tree
def build_huffman_tree(list_of_nodes):
    # no nodes made here, just a list of tuple
    while len(list_of_nodes) > 1:
        (charx, numx) = list_of_nodes[0]
        (chary, numy) = list_of_nodes[1]

        # create node with left/right children
        new_node = Node(charx, chary)

        # append new node with the combined lowest freqs to the end of list
        list_of_nodes.append((new_node, numx + numy))

        # print("here", list_of_nodes)
        # remove node index 1 & 2 and sort dict -> list
        list_of_nodes = list_of_nodes[2:]

        list_of_nodes = sorted(list_of_nodes, key=lambda x: x[1])
    return list_of_nodes[0]


# method to print the huffman encoding
# traverses the built binary tree by 
def huffmanCode(nodes, code, d):
    # print(nodes.left)
    # print(nodes.right)
    if (type(nodes.left)) is str:
        d[nodes.left] = code + '0'
    else:
        huffmanCode(nodes.left, code + '0', d)

    if (type(nodes.right)) is str:
        d[nodes.right] = code + '1'
    else:
        huffmanCode(nodes.right, code + '1', d)
    return d


if __name__ == "__main__":
    user_input = input("Enter a piece of text to compress: ")
    while user_input == "":
        user_input = input("Please try again: ")

    freq = count_frequency(user_input)
    sorted_freq = sort_frequency(freq)
    sorted_nodes = build_huffman_tree(sorted_freq)

    d = dict()
    di = huffmanCode(sorted_nodes[0], code="", d=d)
    # print(sorted_freq)
    # print(sorted_nodes)
    print("Character |", "Frequency")
    print("-" * 21)
    for x in sorted(freq.items(), key=lambda x:x[1]):
        print(x[0], " " * 7, "|",  x[1])

    print()

    print("Character |", "Huffman Code")
    print("-" * 24)
    for x in sorted(freq.items(), key=lambda x:x[1]):
        print(x[0], " " * 7, "|", di[x[0]])
