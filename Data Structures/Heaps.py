from collections import deque
import random
class MinHeap:
	def __init__(self, arr=None):
		self.heaplist = [0]
		self.size = 0

		#extend the heaplist if arra given
		if arr:
			self.heaplist.extend(arr)
			self.size = len(arr)
	def generate_random_heaplist(self, size):
		random_list = [random.randint(1, 100) for ix in range(size)]
		self.heaplist.extend(random_list)
		self.size = size
	
	def min_heapify(self, index, cur_size):
		while index <= self.size:
			if index*2+1 <= self.size:
				smaller_child_index = index*2
				if self.heaplist[index*2] > self.heaplist[index*2+1]:
					smaller_child_index += 1
				if self.heaplist[index] > self.heaplist[smaller_child_index]:
					self.heaplist[index], self.heaplist[smaller_child_index] = self.heaplist[smaller_child_index], self.heaplist[index]
					index = smaller_child_index
				else:
					break

			elif index*2 <= self.size:
				if self.heaplist[index] > self.heaplist[index*2]:
					self.heaplist[index], self.heaplist[index*2] = self.heaplist[index*2], self.heaplist[index]
					index = index*2
				else:
					break
			else:
				break
	def create_min_heap(self):
		half_size = self.size//2
		for ix in range(half_size, 0, -1):
			self.min_heapify(ix, self.size)

	def print_heap(self):
		if self.size <= 0:
			print("Heap is already empty")
			return
		print(self.heaplist)

	def add_element(self, val):
		self.heaplist.append(val)
		self.size += 1
		temp = self.size
		while temp > 1:
			if self.heaplist[temp] < self.heaplist[temp//2]:
				self.heaplist[temp],  self.heaplist[temp//2] = self.heaplist[temp//2], self.heaplist[temp]
				temp = temp//2

	def delete_element(self, location):
		if location < 1:
			print("Location is not valid")
			return
		self.heaplist[self.size], self.heaplist[location] = self.heaplist[location], self.heaplist[self.size]
		self.size -= 1
		self.min_heapify(location, self.size)
		self.heaplist.pop()

heap = MinHeap()
heap.generate_random_heaplist(10)
heap.print_heap()
heap.create_min_heap()
heap.print_heap()

heap.delete_element(2)
heap.print_heap()


'''
Implement heapsort
Uses max_heap, can use min_heap and reverse the list in the end
'''
class MaxHeap:
	def __init__(self, arr=None):
		self.heaplist = [0]
		self.size = 0
		#extend the heaplist if arra given
		if arr:
			self.heaplist.extend(arr)
			self.size = len(arr)

	def generate_random_heaplist(self, size):
		random_list = [random.randint(1, 100) for ix in range(size)]
		self.heaplist.extend(random_list)
		self.size = size
	
	def max_heapify(self, index, cur_size):
		while index <= cur_size:
			if index*2+1 <= cur_size:
				smaller_child_index = index*2
				if self.heaplist[index*2] < self.heaplist[index*2+1]:
					smaller_child_index += 1
				if self.heaplist[index] < self.heaplist[smaller_child_index]:
					self.heaplist[index], self.heaplist[smaller_child_index] = self.heaplist[smaller_child_index], self.heaplist[index]
					index = smaller_child_index
				else:
					break

			elif index*2 <= cur_size:
				if self.heaplist[index] < self.heaplist[index*2]:
					self.heaplist[index], self.heaplist[index*2] = self.heaplist[index*2], self.heaplist[index]
					index = index*2
				else:
					break
			else:
				break
	def create_max_heap(self):
		half_size = self.size//2
		for ix in range(half_size, 0, -1):
			self.max_heapify(ix, self.size)

	def print_heap(self):
		if self.size <= 0:
			print("Heap is already empty")
			return
		print(self.heaplist)

	def add_element(self, val):
		self.heaplist.append(val)
		self.size += 1
		temp = self.size
		while temp > 1:
			if self.heaplist[temp] > self.heaplist[temp//2]:
				self.heaplist[temp],  self.heaplist[temp//2] = self.heaplist[temp//2], self.heaplist[temp]
				temp = temp//2

	def delete_element(self, location):
		if location < 1:
			print("Location is not valid")
			return
		self.heaplist[self.size], self.heaplist[location] = self.heaplist[location], self.heaplist[self.size]
		self.size -= 1
		self.max_heapify(location, self.size)
		self.heaplist.pop()

	def pop_max(self):
		max_element = self.heaplist[1]
		self.delete_element(1)
		return max_element


def heap_sort(arr):
	aux_heap = MaxHeap(arr)
	print("Before craeting max heap")	
	aux_heap.print_heap()
	aux_heap.create_max_heap()
	print("After craeting max heap")	
	aux_heap.print_heap()
	for ix in range(aux_heap.size, 0, -1):
		aux_heap.heaplist[ix], aux_heap.heaplist[1] = aux_heap.heaplist[1], aux_heap.heaplist[ix]
		aux_heap.max_heapify(1, ix-1)
	for ix in range(0, aux_heap.size):
		arr[ix] = aux_heap.heaplist[ix+1]

arr = [random.randint(1, 100) for ix in range(10)]
print("Array is: ", arr)
heap_sort(arr)
print(arr)
