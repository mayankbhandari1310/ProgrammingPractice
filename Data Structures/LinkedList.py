class Node:
	#constructor
	def __init__(self, data=None):
		self.data = data
		self.next = None

	#set data
	def set_data(self, data):
		self.data = data

	#get data
	def get_data(self):
		return self.data

	#set next
	def set_next(self, next):
		self.next = next

	#get next
	def get_next(self):
		return self.next

	#has next
	def has_next(self):
		return self.next != None


class LinkedList:
	#constructor
	def __init__(self):
		self.head = None
		self.size = 0

	#size
	def return_size(self):
		return self.size

	#insert at beginning
	def insert_in_beginning(self, data):
		temp_node = Node(data)
		if self.head:
			temp_node.next = self.head
		self.head = temp_node
		self.size += 1

	#insert at end
	def insert_at_end(self, data):
		node = Node(data)
		if self.size > 0:
			temp = self.head
			while temp.next:
				temp = temp.next
			temp.next = node
		else:
			self.head = node
		self.size += 1

	#insert at position
	def insert_at_position(self, pos, data):
		if self.size <= pos or pos < 0:
			print("Position provided is not valid, use zero based indexing")
		else:
			if pos == 0:
				insert_in_beginning(self, data)
			else:
				temp = self.head
				for ind in range(pos):
					temp = temp.next
				node = Node(data)
				node.next = temp.next
				temp.next = node
				self.size += 1

	def delete_at_beginning(self):
		if self.head:
			temp = self.head
			self.head = self.head.next
			self.size -= 1
			temp.next = None
		else:
			print("LinkedList is already empty")

	def delete_at_end(self):
		if self.head:
			temp = self.head
			#if only one node
			if self.head.next == None:
				self.head = None
			while temp.next.next:
				temp = temp.next
			temp.next = None
			self.size -= 1
		else:
			print("LinkedList is already empty")

	def delete_at_pos(self, pos):
		if pos > self.size or pos <0:
			print("Not a valid position")
		if pos == 0:
			delete_at_beginning(self)
		else:
			temp1 = self.head
			for i in range(pos-1):
				temp1 = temp1.next
			temp2 = temp1.next
			temp1.next = temp1.next.next
			temp2.next = None
			self.size -= 1
	
	def print_list(self):
		temp = self.head
		while temp:
			print(temp.data, " --> ", end="")
			temp = temp.next
		print()

	def get_node_at_pos(self, pos):
		if pos > self.size:
			print("Not a valid position")
			return None
		else:
			temp = self.head
			for ix in range(pos-1):
				temp = temp.next
			return temp

ll = LinkedList()
ll.insert_in_beginning(5)
ll.print_list()
ll.insert_at_end(6)
ll.print_list()
ll.insert_in_beginning(3)
ll.print_list()
ll.insert_at_position(1, 10)
ll.print_list()
ll.insert_in_beginning(20)
ll.print_list()
ll.insert_at_end(30)
ll.print_list()
ll.insert_at_position(6, 6)
ll.print_list()
ll.insert_at_position(5, 7)
ll.print_list()

ll.delete_at_end()
ll.print_list()
ll.delete_at_pos(2)
ll.print_list()
ll.delete_at_beginning()
ll.print_list()

cur_node = ll.get_node_at_pos(2)
if cur_node:
	print("Node at position 2 is : ", cur_node.data)




'''
Question : find a loop in linked list, size limit 10
'''
#returns the loop length if found
def find_loop_length(slowptr, fastptr):
	loop_size = 1
	while slowptr.next != fastptr:
		slowptr = slowptr.next
		loop_size += 1

	return loop_size

#return the starting point of the loop
def return_starting_node_of_loop(looped_ll, loop_length):
	node_ahead = looped_ll.head
	loop_start_node = looped_ll.head
	for ix in range(loop_length):
		node_ahead = node_ahead.next
	while loop_start_node != node_ahead:
		loop_start_node = loop_start_node.next
		node_ahead = node_ahead.next
	return loop_start_node

#returns the starting point of the loop if found, else returns None
def find_loop(looped_ll):
	slowptr = looped_ll.head
	fastptr = looped_ll.head
	while fastptr:
		if fastptr.next == None or fastptr.next.next == None:
			print("List does not contain a loop")
			return None
		else:
			fastptr = fastptr.next.next
			slowptr = slowptr.next
		if slowptr.next == fastptr.next:
			break
	#find the length of the loop
	loop_length = find_loop_length(slowptr, fastptr)
	print("Size of the loop is : ", loop_length)

	loop_start_node = return_starting_node_of_loop(looped_ll, loop_length)
	return loop_start_node

#printing a list with loop to check the loop
def print_list_for_some_time(looped_ll, num):
	temp = looped_ll.head
	for ix in range(num):
		print(temp.data, end= " ")
		temp = temp.next
	print()


#setting up a loop
looped_ll = LinkedList()
for ix in range(0, 10):
	looped_ll.insert_at_end(ix)

node_7 = looped_ll.get_node_at_pos(7)
node_10 = looped_ll.get_node_at_pos(10)

print(node_7.data)
print(node_10.data)

node_10.next = node_7

#try with a list with a loop
print_list_for_some_time(looped_ll, 30)
loop_start_node = find_loop(looped_ll)
print("Loop starts at node with value : ", loop_start_node.data)
#try with a linked list without loop
loop_start_node = find_loop(ll)






'''
Two lists merging into one, find the point of intersection
'''
def find_common_intersection(list1, list2):
	size_list1 = 0
	size_list2 = 0
	list1_ptr = list1.head
	list2_ptr = list2.head
	#assuming list1 is longer than list2
	bigger_list_ptr = list1.head
	smaller_list_ptr = list2.head
	while list1_ptr:
		size_list1 += 1
		list1_ptr = list1_ptr.next
	while list2_ptr:
		size_list2 += 1
		list2_ptr = list2_ptr.next
	if size_list2 > size_list1:
		bigger_list_ptr, smaller_list_ptr = smaller_list_ptr, bigger_list_ptr
	#get the difference in list size
	diff = abs(size_list1 - size_list2)
	print('Difference in size = ', diff)
	for ix in range(diff):
		bigger_list_ptr = bigger_list_ptr.next

	while smaller_list_ptr != bigger_list_ptr and bigger_list_ptr != None:
		print(smaller_list_ptr, bigger_list_ptr, smaller_list_ptr.data, bigger_list_ptr.data)
		smaller_list_ptr = smaller_list_ptr.next
		bigger_list_ptr = bigger_list_ptr.next
	print(bigger_list_ptr)
	return bigger_list_ptr



#Create lists
list1 = LinkedList()
list2 = LinkedList()
for ix in range(0, 10):
	list1.insert_at_end(ix)
for ix in range(20, 40):
	list2.insert_at_end(ix)

print("Lists before merging")
print("List 1 : ", end="")
list1.print_list()
print("")
print("List 2 : ", end="")
list2.print_list()

#merge lists
temp_node1 = list2.get_node_at_pos(15)
temp_node2 = list1.get_node_at_pos(10) #last node, will point to some intermediate node in list2
temp_node2.next = temp_node1

print("lists after merging")
print("List 1 : ", end="")
list1.print_list()
print("")
print("List 2 : ", end="")
list2.print_list()

common_intersection = find_common_intersection(list1, list2)
print("Common Intersection = ", common_intersection.data)









'''
Question : display the linked list in reverse order
'''
def print_reverse(list_ptr):
	if list_ptr == None:
		return
	print_reverse(list_ptr.next)
	print(list_ptr.data, end= "->")


print("Linked list in correct order : ")
ll.print_list()
print("List in reverse order : ")
print_reverse(ll.head)
print()






'''
Merging two sorted list in a sorted order
'''
import random

#create 2 sorted lists
list1 = [random.randint(1, 1000) for ix in range(30)]
list1.sort()
print(list1)
list2 = [random.randint(1, 1000) for ix in range(20)]
list2.sort()
print(list2)

#generated 2 linked lists using sorted lists
linked_list1 = LinkedList()
linked_list2 = LinkedList()
for item in list1:
	linked_list1.insert_at_end(item)
for item in list2:
	linked_list2.insert_at_end(item)

print("Sorted list 1 : ")
linked_list1.print_list()

print("sorted list 2 : ")
linked_list2.print_list()

#return a merged list
def merge_sorted_lists(list1, list2):
	head1 = list1.head
	head2 = list2.head
	list3 = LinkedList()
	while head1 and head2:
		if  head1.data < head2.data:
			list3.insert_at_end(head1.data)
			head1 = head1.next
		else:
			list3.insert_at_end(head2.data)
			head2 = head2.next

	while head1:
		list3.insert_at_end(head1.data)
		head1= head1.next

	while head1:
		list3.insert_at_end(head2.data)
		head2= head2.next
	
	return list3

merged_list = merge_sorted_lists(linked_list1, linked_list2)
print("Sorted merged list : ")
merged_list.print_list()






'''
Question : reverse a linked list
'''

#iteratively
def reverse_list(list):
	prev = None
	cur = list.head
	while cur:
		temp = cur.next
		cur.next = prev
		prev, cur = cur, temp
	return prev





'''
Question : reverse blocks of nodes of size K at a time in a linked list
'''
#reverse list for k nodes
def reverse_list_k_nodes(cur_ptr, K):
	count = 1
	prev_ptr = None
	last_ptr_in_cur_k = cur_ptr
	next_to_last_ptr_in_cur_k = None

	while count <= K and cur_ptr!=None:
		next_to_last_ptr_in_cur_k = cur_ptr.next
		temp = cur_ptr.next
		cur_ptr.next = prev_ptr
		prev_ptr, cur_ptr = cur_ptr, temp
		count += 1
	return prev_ptr, last_ptr_in_cur_k, next_to_last_ptr_in_cur_k

print("LL in correct order: ")
ll.print_list()
reverse_ll = LinkedList()
reverse_ll.head = reverse_list(ll)
print("Ll in reverse order" )
reverse_ll.print_list()


#make a list
def make_and_reverse_blockwise(num_nodes, K):
	ll = LinkedList()
	for ix in range(1, num_nodes+1):
		ll.insert_at_end(ix)

	print("Original list")
	ll.print_list()

	if K > num_nodes:
		print("K can't be greater than number of nodes")
	elif K==1:
		return
	else:
		start_ptr, last_ptr, next_to_last_ptr = reverse_list_k_nodes(ll.head, K) 
		head_reversed_by_k_ptr = start_ptr
		while next_to_last_ptr!=None:
			start_ptr, temp_last_ptr, next_to_last_ptr = reverse_list_k_nodes(next_to_last_ptr, K)  
			last_ptr.next = start_ptr
			last_ptr = temp_last_ptr
		ll.head = head_reversed_by_k_ptr
		print("List reversed {} block at a time : ".format(K))
		ll.print_list()


make_and_reverse_blockwise(20, 5)
make_and_reverse_blockwise(20, 4)
make_and_reverse_blockwise(20, 3)
make_and_reverse_blockwise(20, 2)
make_and_reverse_blockwise(20, 1)




'''
Ques : copy a linked list with random pointers
'''

class RandomNode:
	#constructor
	def __init__(self, data=None):
		self.data = data
		self.next = None
		self.random = None

class RandomLinkedList:
	#constructor
	def __init__(self):
		self.head = None
		self.size = 0

	#size
	def return_size(self):
		return self.size

	#insert at beginning
	def insert_in_beginning(self, data):
		temp_node = RandomNode(data)
		if self.head:
			temp_node.next = self.head
		self.head = temp_node
		self.size += 1

	#insert at end
	def insert_at_end(self, data):
		node = RandomNode(data)
		if self.size > 0:
			temp = self.head
			while temp.next:
				temp = temp.next
			temp.next = node
		else:
			self.head = node
		self.size += 1

	def print_list(self):
		temp = self.head
		while temp:
			print(temp.data, " --> ", end="")
			if temp.random:
				print(" Random: ", temp.random.data, ' --> ', end="")
			else:
				print(" --> Null ")
			temp = temp.next
		print()


	#assigning the random pointers
	def assign_random_ptr(self):
		temp = self.head
		addresses = {}
		count = 0
		while temp:
			addresses[count] = temp
			count += 1
			temp = temp.next
		temp = self.head
		while temp:
			temp.random = addresses[random.randint(0, self.size-1)]
			temp = temp.next

	def make_a_copy(self):
		cur_ptr = self.head
		
		#insert intermediate nodes
		while cur_ptr:
			temp_node = RandomNode()
			temp_node.data = cur_ptr.data
			temp_node.next = cur_ptr.next
			cur_ptr.next = temp_node
			cur_ptr = temp_node.next

		#copy random pointer assignments
		prev_ptr = self.head
		while prev_ptr:
			cur_ptr = prev_ptr.next
			if prev_ptr.random:
				cur_ptr.random = prev_ptr.random.next 
			else:
				cur_ptr.random = None
			prev_ptr = cur_ptr.next

		#remove and return the copied list
		cur_ptr = self.head
		copied_list_head = None
		if cur_ptr:
			copied_list_head = cur_ptr.next
		temp = copied_list_head
		while cur_ptr:
			cur_ptr.next = temp.next
			if cur_ptr.next:
				temp = cur_ptr.next
			cur_ptr = cur_ptr.next
			temp = temp.next

		return copied_list_head

print("\n\n\n")
print("Copying linked lists with random pointers")
random_linked_list = RandomLinkedList()
for ix in range(10):
	random_linked_list.insert_in_beginning(ix)
random_linked_list.assign_random_ptr()
random_linked_list.print_list()

copied_list = RandomLinkedList()
copied_list.head = random_linked_list.make_a_copy()
print("copied list: ")
copied_list.print_list()