class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class MyQueue:
	def __init__(self, queue=None):
		self.front = None
		self.rear = None
		self.size = 0

	def enqueue(self, data):
		temp_node = Node(data)
		if self.front == None:
			self.front = self.rear = temp_node
		else:
			self.rear.next = temp_node
			self.rear = self.rear.next
		self.size += 1

	def deque(self):
		if self.size == 1:
			self.front = self.rear = None
			self.size = 0
		elif self.size > 0:
			temp = self.front
			self.front = self.front.next
			temp.next = None
			temp = None
			self.size -= 1
		else:
			print("Queue is already empty")
	def traverse(self):
		temp = self.front
		print("Queue contains : ", end="")
		while temp:
			print(temp.data, end="->")
			temp = temp.next
		print()

	def isempty(self):
		return self.size == 0

	def get_size(self):
		return self.size


queue = MyQueue()
for ix in range(5):
	queue.enqueue(ix)
queue.traverse()
if queue.isempty():
	print("Queue is empty")
else:
	print("Queue is not empty")
queue.deque()
queue.deque()
queue.deque()
queue.traverse()
queue.deque()
queue.deque()
queue.deque()
queue.deque()
if queue.isempty():
	print("Queue is empty")
else:
	print("Queue is not empty")
from collections import deque

d = deque([1, 2, 3])
d.appendleft(0)
print(d)
d.append(4)
print(d)
d.popleft()
print(d)
d.pop()
print(d)
print(d[1])
