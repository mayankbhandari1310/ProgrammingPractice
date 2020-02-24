class Node:
	def __init__(self, data=None):
		self.data = data
		self.prev = None

class MyStack:
	def __init__(self, top=None):
		self.top = top
		self.size = 0

	def push(self, data):
		new_top = Node(data)
		new_top.prev = self.top
		self.top = new_top
		self.size += 1

	def pop(self):
		if self.size>0:
			temp = self.top
			self.top = self.top.prev
			temp.prev = None
			temp = None
			self.size -=1
		else:
			print("Stack is already empty")

	def peek(self):
		if self.top:
			return self.top.data

	def traverse(self):
		temp = self.top
		print("Stack contains : ", end="->")
		while temp:
			print(temp.data, end='->')
			temp = temp.prev
		print()
	
	def isempty(self):
		return self.size == 0

	def size(self):
		return self.size


stack = MyStack()
for ix in range(5):
	stack.push(ix)

stack.traverse()

print(stack.peek())
stack.pop()
print(stack.isempty())
stack.pop()
print(stack.isempty())
stack.pop()
print(stack.isempty())
stack.pop()
print(stack.isempty())
stack.pop()
print(stack.isempty())
stack.pop()
print(stack.isempty())
stack.pop()
print(stack.isempty())
stack.pop()
print(stack.isempty())



'''
Find the maximum area in a histogram.
input : given a list of numbers which contains heights in order
'''
from collections import deque

def find_max_area(histogram):
	aux_stack = deque()
	max_area = 0
	print("Max_area : ")
	for ix in range(len(histogram)):
		if not aux_stack:
			aux_stack.append((ix, histogram[ix]))
		else:
			while aux_stack:
				(idx, val) = aux_stack[-1]
				if val <= histogram[ix]:
					break
				else:
					aux_stack.pop()
					cur_area = 0
					if aux_stack:
						(idx2, val2) = aux_stack[-1]
						cur_area = (ix -1 - idx2)*val
					else:
						cur_area = (ix)*(val)
					max_area = max(max_area, cur_area)
			aux_stack.append((ix, histogram[ix]))
		print(max_area, end =" -> ")

	while aux_stack:
		len_hist = len(histogram)
		(idx, val) = aux_stack[-1]
		aux_stack.pop()
		cur_area = 0
		if aux_stack:
			(idx2, val2) = aux_stack[-1]
			cur_area = (len_hist - 1 - idx2)*val
		else:
			cur_area = (len_hist)*(val)
		max_area = max(max_area, cur_area)
		print(max_area, end =" -> ")
	print()
	return max_area

#hist = [9, 10, 10, 11, 8, 7, 6, 5, 4, 3, 2, 1]
#hist = [1, 10, 10, 11, 8, 7, 6, 5, 4, 3, 2, 1]
hist = [6, 2, 5, 4, 5, 1, 6]
area = find_max_area(hist)
print("Maximum area is : ", area)

'''
Min stack , getting min element in the stack till now in O(1)
'''
import random
min_stack = deque()
my_stack = deque()

def print_min():
	if min_stack:
		print(my_stack)
		print("Min value is: ", min_stack[-1])
	else:
		print("Stack is empty")

#create data
my_list = [random.randint(1, 50) for ix in range(200)]
print(my_list)
idx = 0

while idx < 150:
	x = random.randint(1, 999999999)%3
	if x==0:
		print_min()
	elif x==1:
		my_stack.append(my_list[idx])
		if min_stack and my_list[idx] > min_stack[-1]:
			pass
		else:
			min_stack.append(my_list[idx])
			#print("Pushed element: ", my_list[idx])
		#print("Stack contains: ", my_stack)
	else:
		if my_stack:
			x = my_stack.pop()
			if min_stack[-1] == x:
				min_stack.pop()
		#	print("Element popped: ", x)
		#	print("Stack contains: ", my_stack)
		else:
			print("Stack is already empty")
	idx += 1