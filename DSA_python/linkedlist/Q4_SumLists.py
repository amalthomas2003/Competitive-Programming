

from LinkedList import LinkedList

def sum_linked_list(l1, l2):
    l = LinkedList()
    current1 = l1.head
    current2 = l2.head
    carry = 0
    while current1 or current2:
        val1 = current1.data if current1 else 0
        val2 = current2.data if current2 else 0
        sum = val1 + val2 + carry
        carry = sum // 10
        l.add(sum % 10)
        if current1:
            current1 = current1.next
        if current2:
            current2 = current2.next
    if carry:
        l.add(carry)
    return l
llA = LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)


llB = LinkedList()
llB.add(5)
llB.add(9)
llB.add(3)
print(llA)
print(llB)
print(sumList(llA, llB))
