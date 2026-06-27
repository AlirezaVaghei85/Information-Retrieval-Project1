import pickle
import sys
import psutil
import os


"""
import nltk
from nltk.corpus import reuters
from nltk.tokenize import word_tokenize
# download resources (only once)
nltk.download('reuters')
nltk.download('punkt')
nltk.download('punkt_tab')

data = []

for doc_id in reuters.fileids():
    text = reuters.raw(doc_id)          # get raw text
    tokens = word_tokenize(text)        # tokenize using NLTK
    data.append((doc_id, tokens))       # (doc_id, tokens)

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
"""


with open("data.pkl", "rb") as f:
    data = pickle.load(f)


# print('First document id', data[0][0])
# print('First document tokens', data[0][1])
# print('Total number of documents', len(data))


class Node():
    def __init__(self, term: str, DocID: str | None = None):
        self.left = None
        self.right = None
        self.data = {"term": term, "DocID": [DocID] if DocID else []}


def Insert(root: Node, term: str, DocID: str):
    if root is None:
        return Node(term, DocID)
    elif term < root.data["term"]:
        root.left = Insert(root.left, term, DocID)
    elif term > root.data["term"]:
        root.right = Insert(root.right, term, DocID)
    else:
        if DocID not in root.data["DocID"]:
            root.data["DocID"].append(DocID)
            root.data["DocID"].sort()
    return root


def Inorder(root: Node):
    if root:
        Inorder(root.left)
        print(f"term: {root.data["term"]}")
        print(f"DocIDs: {root.data["DocID"]}")
        Inorder(root.right)


def Search(root: Node, term: str):
    if term > root.data["term"] and root.right != None:
        root = Search(root.right, term)
    elif term < root.data["term"] and root.left != None:
        root = Search(root.left, term)
    if term == root.data["term"] and root != None:
        return root
    if root.left == None or root.right == None:
        return Node(" ", " ")
    return root


def Search_with_AND(root: Node, term: str):
    term = term.split()
    term1 = Search(root, term[0])
    term2 = Search(root, term[2])
    if term1.data["term"] == " " or term2.data["term"] == " ":
        return Node(" ", " ")
    i = 0
    j = 0
    t_INX = 0
    temp_list = []
    while True:
        if term1.data["DocID"][i] == term2.data["DocID"][j]:
            temp_list.append(term1.data["DocID"][i])
            i += 1
            j += 1
            t_INX += 1
        elif term1.data["DocID"][i] < term2.data["DocID"][j]:
            i += 1
        elif term1.data["DocID"][i] > term2.data["DocID"][j]:
            j += 1
        if i == len(term1.data["DocID"]) or j == len(term2.data["DocID"]):
            break
    tmp_term = Node(term)
    for string in temp_list:
        tmp_term.data["DocID"].append(string)
    return tmp_term


def get_nodes(root: Node):
    List: list[Node] = []
    Stack = []
    Stack.append(root)
    tmp = root.right
    while len(Stack) != 0 or tmp != None:
        while tmp != None:
            Stack.append(tmp)
            tmp = tmp.right
        tmp = Stack.pop()
        List.append(tmp)
        tmp = tmp.left
    return List


def Sort_freq(List):
    for n1 in List:
        for n2 in list[n1+1:]:
            if len(n1.data["DocID"]) > len(n2.data["DocID"]):
                list.index()


root = Node(data[0][1][0], data[1][0])
n = 0
while n < 10788:
    for term in data[n][1]:
        root = Insert(root, term.lower(), data[n][0])
    n += 1

s = "oil AND market"

process = psutil.Process(os.getpid())
print(f"Memory usage: {process.memory_info().rss / (1024 * 1024):.2f} MB")

print("1. Search for one query")
print("2. Search for two queries with AND")
print("3. See 30 most frequent terms")
Choice = int(input("Choose an option: "))
if Choice == 1:
    query = input("Enter your query: ").lower()
    tmp = Search(root, query)
    if tmp.data["term"] == " ":
        print("Query not found!")
    else:
        print(f"Query: {query}")
        print(f"Documents retrieved: {len(tmp.data["DocID"])}")
        sys.stdout.write(f"Doc IDs: [")
        for i in tmp.data["DocID"][:10]:
            sys.stdout.write(f"'{i}', ")
        sys.stdout.write("]")
elif Choice == 2:
    query = input("Enter your query: ").lower()
    tmp = Search_with_AND(root, query)
    if tmp.data["term"] == " ":
        print("Query not found!")
    else:
        print(f"Query: {query}")
        print(f"Documents retrieved: {len(tmp.data["DocID"])}")
        sys.stdout.write(f"Doc IDs: [")
        for i in tmp.data["DocID"][:10]:
            sys.stdout.write(f"'{i}', ")
        sys.stdout.write("]")
elif Choice == 3:
    l = get_nodes(root)
    all_nodes_freq = []
    for node in l:
        all_nodes_freq.append(
            {
                "term": node.data["term"],
                "freq": len(node.data["DocID"])
            }
        )

    sorted_nodes = sorted(all_nodes_freq, key=lambda d: d["freq"])

    sorted_nodes.reverse()
    n = 1
    for x in sorted_nodes:
        print(f"{n}-{x["term"]}, {x["freq"]}")
        n += 1
        if n == 31:
            break
