import random


'''
Bogosort, don't call it. Just don't. Okay fine, maybe with 2-3 elements
'''
from itertools import permutations
def bogosort(arr):
	def check_if_sorted(arr):
		length = len(arr)
		for ix in range(length-1):
			if arr[ix] > arr[ix+1] : 
				return False
		return True
	length = len(arr)
	perm = permutations(arr, length)
	for cur_perm in perm:
		if check_if_sorted(cur_perm):
			arr = cur_perm
			return arr

arr = [random.randint(1, 100000) for ix in range(3)]
print("Before sorting: ", arr)
arr = bogosort(arr)
print("After bogosort: ", arr)


'''
Bubble sort, keeps shifting max element to the right
'''
def bubble_sort(arr):
	arr_len = len(arr)
	for ix in range(arr_len, 0, -1):
		for iy in range(ix-1):
			if arr[iy] > arr[iy+1]:
				arr[iy], arr[iy+1] = arr[iy+1], arr[iy]

arr = [random.randint(1, 100000) for ix in range(5)]
print("Before sorting: ", arr)
bubble_sort(arr)
print("After bubble_sort: ", arr)



'''
Selection sort, selects minimum in the list and puts it in front 
'''
def selection_sort(arr):
	arr_len = len(arr)
	for ix in range(arr_len-1):
		min_ind = ix
		for iy in range(ix+1, arr_len):
			if arr[iy] < arr[min_ind]:
				min_ind = iy
		arr[min_ind], arr[ix] = arr[ix], arr[min_ind]

arr = [random.randint(1, 100000) for ix in range(5)]
print("Before sorting: ", arr)
selection_sort(arr)
print("After selction sort: ", arr)




'''
Heap Sort
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
	#aux_heap.print_heap()
	aux_heap.create_max_heap()
	#aux_heap.print_heap()
	for ix in range(aux_heap.size, 0, -1):
		aux_heap.heaplist[ix], aux_heap.heaplist[1] = aux_heap.heaplist[1], aux_heap.heaplist[ix]
		aux_heap.max_heapify(1, ix-1)
	for ix in range(0, aux_heap.size):
		arr[ix] = aux_heap.heaplist[ix+1]

arr = [random.randint(1, 100) for ix in range(10)]
print("Array before heapsort is: ", arr)
heap_sort(arr)
print("Array after heapsort: ", arr)


'''
Mergesort
'''

'''
Selection sort, selects minimum in the list and puts it in front 
'''

def merge(arr, start_1, end_1, start_2, end_2):
	#craete auxilliary array
	aux_size = end_2 - start_1 + 1
	aux_arr = [0 for ix in range(aux_size)]
	
	ix1 = start_1
	ix2 = start_2
	aux_ix = 0
	while ix1 <= end_1 and ix2 <= end_2:
		if arr[ix1] <= arr[ix2]:
			aux_arr[aux_ix] = arr[ix1]
			ix1 += 1
		else:
			aux_arr[aux_ix] = arr[ix2]
			ix2 += 1
		aux_ix += 1
	
	while ix1 <= end_1:
		aux_arr[aux_ix] = arr[ix1]
		ix1 += 1
		aux_ix += 1

	while ix2 <= end_2:
		aux_arr[aux_ix] = arr[ix2]
		ix2 += 1
		aux_ix += 1

	for ix in range(aux_size):
		arr[ix+start_1] = aux_arr[ix]

def merge_sort(arr, start, en):
	if start >= en:
		return
	mid = (start + en)//2
	merge_sort(arr, start, mid)
	merge_sort(arr, mid+1, en)
	merge(arr, start, mid, mid+1, en)
	
arr = [random.randint(1, 100000) for ix in range(10)]
print("Before merge sort: ", arr)
merge_sort(arr, 0, len(arr)-1)
print("After  merge sort: ", arr)


'''
QuickSort, random pivot implementation
'''

def quicksort(arr, start, en):
	if start >= en:
		return

	random_pivot = start + random.randint(0, en-start)
	front = start
	rear = en
	#go to the first element greater then pivot element
	while front < random_pivot and arr[front] < arr[random_pivot]:
		front += 1

	while rear > random_pivot and arr[rear] > arr[random_pivot]:
		rear -= 1

	while front < random_pivot:
		if arr[front] >= arr[random_pivot]:
			arr[front], arr[random_pivot-1] = arr[random_pivot-1], arr[front]
			arr[random_pivot-1], arr[random_pivot] = arr[random_pivot], arr[random_pivot-1]
			random_pivot -= 1
		else:
			front += 1
	while rear > random_pivot:
		if arr[rear] < arr[random_pivot]:
			arr[rear], arr[random_pivot+1] = arr[random_pivot+1], arr[rear]
			arr[random_pivot+1], arr[random_pivot] = arr[random_pivot], arr[random_pivot+1]
			random_pivot += 1
		else:
			rear -= 1
	quicksort(arr, start, random_pivot-1)
	quicksort(arr, random_pivot+1, en)

arr = [random.randint(1, 100) for ix in range(10)]
print("Array before quicksort is: ", arr)
quicksort(arr, 0, len(arr)-1)
print("Array  after quicksort is: ", arr)
