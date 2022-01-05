# Version 1

class Node:
    def __init__(self, val):
        print(f"Creating a node with a val {val}")
        self.val = val
        self.nxt = None

class LL:
    def __init__(self):
        print("I am called")
        self.head = None

h = LL()
first = Node(10)

h.head = first

second = Node(20)
third = Node(30)
fourth = Node(40)
first.nxt = second
second.nxt = third
third.nxt = fourth

# t = h.head
# while t:
#     print(t.val)
#     t = t.nxt

head = h.head
while head is not None:
    print(head.val)
    head = head.nxt