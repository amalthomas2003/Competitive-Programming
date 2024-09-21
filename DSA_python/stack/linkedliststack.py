import sys
sys.stdout=open("output.abc","w+")


class node:
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next
class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
class stack:
    def __init__(self):
        self.linkedlist=linkedlist()
    def isempty(self):
        return self.linkedlist.head==None
    def push(self,value=None):
        new_node=node(value)
        if self.linkedlist.tail==None:
            self.linkedlist.head=new_node
            self.linkedlist.tail=new_node
        else:

            new_node.next=self.linkedlist.head
            self.linkedlist.head=new_node
    def __str__(self):
        curr_node=self.linkedlist.head
        list1=""
        while curr_node is not None:
            list1+=str(curr_node.value)
            curr_node=curr_node.next
        return list1
    
    def __iter__(self):
        curr_node=self.linkedlist.head
        while curr_node:
            yield curr_node.value
            curr_node=curr_node.next
    def pop(self):
        if self.isempty():
            return "no element to pop"
        else:
            new_node=self.linkedlist.head.next
            self.linkedlist.head.next=None
            print(self.linkedlist.head.value)
            self.linkedlist.head=new_node
        



stack=stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

for i in stack:
    print(i)

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack.pop())
print(stack)