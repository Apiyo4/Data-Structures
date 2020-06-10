"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# LIST QUEUE IMPLEMENTATION
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size = self.size + 1
#         self.storage.insert(0, value)

#     def dequeue(self):
#         if self.size == 0:
#             print("IndexError: Pop from empty List")
#         else:
#             self.size = self.size - 1
#             return self.storage.pop()

# lINKEDLIST QUEUE IMPLEMENTATION
class Node:
    def  __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_node):
        self.next_node = new_node
class Queue:
    def __init__(self, node=None):
        self.size = 1 if node is not None else 0
        self.storage = []
        self.head = node
        self.tail = node
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size = self.size + 1
        # self.storage.insert(0, value)
        new_node = Node(value,None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        

    def dequeue(self):
       if not self.tail:
            return None
       if not self.head:
            self.size -= 1
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
       value = self.head.get_value()
       self.head = self.head.get_next()
       return value 
        