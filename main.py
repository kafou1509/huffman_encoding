# Huffman Coding in python
# string = "ABCDAACDAAAD"
string = "BCAADDDCCACACAC"
# stringx = "hello world"

# Creating tree nodes
class TreeNodes:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, binString):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    # print(l, r)
    d = dict()
    d.update(huffman_code_tree(l, binString + '0'))
    d.update(huffman_code_tree(r, binString + '1'))
    # print(d)
    return d


# Calculating frequency
freq = {}
for char in string:
    if char in freq:
        # this key is assigned the value using the equal sign
        freq[char] += 1
    else:
        freq[char] = 1

# sorted lowest to highest
freq = sorted(freq.items(), key=lambda x: x[1], reverse=False)

# queue
nodes = freq
while len(nodes) > 1:
    # first elm
    (key1, c1) = nodes[0]
    # print("key1 c1", key1, c1)
    # second elm
    (key2, c2) = nodes[1]
    # print("key2 c2", key2, c2)
    # removes the first two keys from queue
    nodes = nodes[2:]
    # print("remove first two keys from queue", nodes)

    # node z and sets this node with both of the key:value(freq)
    node = TreeNodes(key1, key2)
    # appends the new node to end of the list with the added k/v
    nodes.append((node, c1 + c2))

    # re-sort the queue using the value(freq) defined for key
    nodes = sorted(nodes, key=lambda x: x[1], reverse=False)
    # print("nodes", nodes)
    # print("~~~ end iteration ~~~")


huffmanCode = huffman_code_tree(nodes[0][0], '')

print(' Char | Huffman code ')
print('----------------------')
print("here", freq)
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))

if __name__ == "__main__":
    print('')