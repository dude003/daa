class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        self.huff = ''

def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)
    if not node.left and not node.right:
        print(f"{node.char} -> {newVal}")

def main():
    chars = []
    freq = []
    num_chars = int(input("Enter the number of characters: "))
    
    for _ in range(num_chars):
        char = input("Enter character: ")
        frequency = int(input(f"Enter frequency for {char}: "))
        chars.append(char)
        freq.append(frequency)

    nodes = []

    for x in range(len(chars)):
        nodes.append(Node(chars[x], freq[x]))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)

        left = nodes[0]
        right = nodes[1]
        left.huff = 0
        right.huff = 1

        newNode = Node(left.char + right.char, left.freq + right.freq)
        newNode.left = left
        newNode.right = right
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    printNodes(nodes[0])

if __name__ == "__main__":
    main()
