import heapq
from collections import defaultdict, Counter

# 节点类
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # 定义节点的比较运算符，优先队列需要
    def __lt__(self, other):
        return self.freq < other.freq

# 构建哈夫曼树
def build_huffman_tree(frequencies):
    priority_queue = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

# 生成哈夫曼编码
def generate_huffman_codes(root):
    huffman_codes = {}

    def generate_codes(node, current_code):
        if node is not None:
            if node.char is not None:
                huffman_codes[node.char] = current_code
            generate_codes(node.left, current_code + '0')
            generate_codes(node.right, current_code + '1')

    generate_codes(root, '')
    return huffman_codes

# 使用示例
if __name__ == "__main__":
    data = "this is an example for huffman encoding"
    frequency = Counter(data)

    huffman_tree_root = build_huffman_tree(frequency)
    huffman_codes = generate_huffman_codes(huffman_tree_root)

    print("Huffman Codes:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")
