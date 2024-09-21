
import random

class node:
    def __init__(self):
        self.value=None
        self.next=None
        self.prev=None
class linkedlist:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def create(self,n,start,end):
        for i in range(n):
            if self.head is None:
                self.head=node()
                self.tail=self.head
                self.head.value=random.randint(start,end)
            else:
                self.tail.next=node()
                self.tail=self.tail.next
                self.tail.value=random.randint(start,end)

    def __str__(self) -> str:
        curr=self.head
        ans=''
        while curr:
            ans+=str(curr.value)+'->'
            curr=curr.next
        return ans


def remove_duplicates(ll):
    if ll.head is None:
        return
 
    current_node = ll.head
 
    while current_node:
        runner = current_node
        while runner.next:
            if runner.next.value == current_node.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        
        if current_node.next is None:
            ll.tail = current_node
            break
        current_node = current_node.next
    print(ll.tail.value)

    

linkedlist=linkedlist()
linkedlist.create(10,0,10)
print(linkedlist)
remove_duplicates(linkedlist)
print(linkedlist)
