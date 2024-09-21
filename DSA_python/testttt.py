
# def heapify(list1):

#     def heapify1(heap,element,index):
#         heap.append(element)
#         parent=index//2
#         while parent>0:
#             if heap[index]<heap[parent]:
#                 heap[index],heap[parent]=heap[parent],heap[index]
#             index=parent
#             parent=parent//2


#     heap=[None]
#     for i in range(len(list1)):
        
#         heapify1(heap,list1[i],i+1)
#     print(heap)
# l=[]
# while True:
#     n=int(input("1 for insert and 2 for delete"))
#     if n==1:
#         l.append(int(input()))
#         heapify(l)
#     else:
#         m=int(input(f"Enter value to delete form {l}"))
#         l.remove(m)
#         heapify(l)
            

class node:
    def __init__(self,value) -> None:
        self.value=value
        self.leftchild=None
        self.rightchild=None

class bst:
    def __init__(self):
        self.root=None


    def insertnode(self,value):
        temp_node=node(value)
        if not self.root:
            self.root=temp_node
        else:
            self.insert_recursive(self.root,temp_node)
    def insert_recursive(self,root,temp_node):
        if root==None:
            return temp_node
        elif temp_node.value<root.value:
            root.leftchild=self.insert_recursive(root.leftchild,temp_node)
        else:
            root.rightchild=self.insert_recursive(root.rightchild,temp_node)
        return root
    def print_tree(self):
        if self.root is None:
            print("Tree is empty")
            return

        def print_helper(node):
            if node is None:
                return
            print_helper(node.leftchild)
            print(node.value, end=" ")
            print_helper(node.rightchild)

        print_helper(self.root)
   

bst=bst()
bst.insertnode(3)
bst.insertnode(6)
bst.insertnode(2)
bst.insertnode(9)

bst.insertnode(1)
bst.insertnode(5)
bst.insertnode(1)


bst.print_tree()