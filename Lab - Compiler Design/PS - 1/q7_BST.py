import json
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return self.root
        else:
            self.insert_call(self.root, data)
    
    def insert_call(self, root, data):
        if data < root.data:
            if root.left:
                self.insert_call(root.left, data)
            else:
                root.left = Node(data)

        else:
            if root.right:
                self.insert_call(root.right, data)
            else:
                root.right = Node(data)
        
    def inorder(self):
        result = []
        self.inorder_call(self.root, result)
        return result
    
    def inorder_call(self, root, result):
        if root:
            self.inorder_call(root.left, result)
            result.append(root.data)
            self.inorder_call(root.right, result)
    
def readJson():
    with open('./storeKeywords.json', 'r') as f:
        data = json.load(f)
    return data['keywords']

def hash(keywords):
    dict = {}
    for key in keywords:
        dict[key] = True
    return dict

def search(dict, search_key):
    if search_key in dict:
        print(f"{search_key} is a keyword ")
    else:
        print(f"{search_key} is not a keyword ")

if __name__ == '__main__':
    keywords = readJson()
    bst = BST()
    for i in keywords:
        bst.insert(i)
    print("Inorder traversal of the BST:")
    result = bst.inorder()
    print(result)
    print("\nUsing hash Table: ")
    dict = hash(keywords)
    search(dict, "int")


