# Version 2


# class Node:
#     def __init__(self, val):
#         print(f"Creating a node with a val {val}")
#         self.val = val
#         self.nxt = None

# class LL:
#     def __init__(self):
#         print("I am called")
#         self.head = None


# h = LL()
# # first = Node(10)

# # h.head = first


# # second = Node(20)
# # third = Node(30)
# # fourth = Node(40)
# # first.nxt = second
# # second.nxt = third
# # third.nxt = fourth

# li = [10, 20, 30, 40]


# t = h.head
# while t:
#     print(t.val)
#     t = t.nxt

# class Kiran:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
#     def getNxtNode(self):
#         return self.next
#     def setNxtNode(self, node):
#         self.next = node
# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head
#         self.size = 0
#     def addNode(self, data):
#         node = Kiran(data, self.head)
#         self.head = node
#         self.size += 1
#         return "inserted"
#     def print(self):
#         curr = self.head
#         while curr:
#             print(curr.data)
#             curr = curr.getNxtNode()
# List = LinkedList()
# print("Inserting a node")

# li = [20, 30, 40, 50, 60]
# for l in li:
#     List.addNode(l)
# List.print()

class Node:
  def __init__(self, data = None, nxt=None): 
    self.data = data
    self.nxt = nxt
class LL:
  def __init__(self):  
    self.h = None

  def insert(self, data):
    newNode = Node(data)
    if(self.h):
      currnt = self.h
      while(currnt.nxt):
        currnt = currnt.nxt
      currnt.nxt = newNode
    else:
      self.h = newNode
  
  def prntLL(self):
    currnt = self.h
    while(currnt):
      print(currnt.data)
      currnt = currnt.nxt
LLobj = LL()
li = [20, 30, 40, 50, 60]
for l in li:
    LLobj.insert(l)
# LLobj.insert(3)
# LLobj.insert(4)
# LLobj.insert(5)
LLobj.prntLL()
# # 
# templist = []

# print(templist.push(10))