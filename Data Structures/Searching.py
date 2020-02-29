from collections import defaultdict

def check_repeating_element_blind_search(arr):
	# blind searching, O(n^2) method  
	for ix in range(len(arr)):
		for iy in range(ix+1, len(arr)):
			if arr[ix] == arr[iy]:
				print("duplicate found ", arr[ix])
				return
	print("No duplicates found")

def check_repeating_element_by_sorting(arr):
	#O(nlogn)
	arr.sort()
	for ix in range(1, len(arr)):
		if arr[ix] == arr[ix-1]:
			print("duplicate found ", arr[ix])
			return
	print("No duplicates found")


def check_repeating_element_by_hashing(arr):
	#O(n)
	count_dict = defaultdict(lambda: 0)
	for item in arr:
		if count_dict[item]:
			print("duplicate found ", item)
			return
		else:
			count_dict[item] += 1 
	print("No duplicates found")

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 2, 3, 1, 2, 2]
check_repeating_element_by_hashing(arr1)
check_repeating_element_by_sorting(arr1)
check_repeating_element_blind_search(arr1)
check_repeating_element_by_hashing(arr2)
check_repeating_element_by_sorting(arr2)
check_repeating_element_blind_search(arr2)

'''
Given an array of size N, and all the entries are in range (1, N-1), check if duplicates occur, 
in O(N) time complexity and O(1) space complexity
Sol: for every val in arr set arr[val] negative, the first negative to be encountered will be the first repeated element found  
'''
import math
def check_repeating_if_entries_less_than_N(arr):
	for ix in range(len(arr)):
		if arr[abs(arr[ix])] < 0:
			print("Duplicate found: ", abs(arr[ix]))
			return
		#use abs other wiseit will treat arr[ix] as negative
		arr[abs(arr[ix])] = -arr[abs(arr[ix])]
	print("No duplicate found")

arr1 = [1, 2, 3, 4, 2]
arr2 = [3, 2, 3, 1, 2, 2]
check_repeating_if_entries_less_than_N(arr1)
check_repeating_if_entries_less_than_N(arr2)


'''
Two elements who sum is nearest to zero, assumes two elements atleast
'''
def find_two_elements_with_sum_closest_to_zero(arr):
	if len(arr) < 2:
		print("Array must have atleast 2 elements")
		return
	arr.sort()
	start = 0
	end = len(arr)-1

	min_start_ind = start
	min_end_ind = end
	diff = abs(arr[start] + arr[end])
	while start < end-1:
		if abs(arr[start] + arr[end-1]) < abs(arr[start+1] + arr[end]):
			if abs(arr[start] + arr[end-1]) < diff:
				diff = abs(arr[start] + arr[end-1])
				min_end_ind = end - 1
			end = end-1
		else:
			if abs(arr[start+1] + arr[end]) < diff:
				diff = abs(arr[start+1] + arr[end])
				min_start_ind =start+1
			start = start+1
	print("Elements with sum closest to zero are : ", arr[min_start_ind], arr[min_end_ind])
arr = [1, 60, -10, 70, -80, 85]
find_two_elements_with_sum_closest_to_zero(arr)

'''
Find minimum in a rotated sorted array
'''
def findMinInRotatedSortedArray(arr):
	start = 0
	end = len(arr) - 1
	while start < end:
		mid = (start+end)//2
		if arr[start] <= arr[end]:
			break
		if arr[mid] >= arr[start] and arr[mid] >= arr[end]:
			start = mid+1
		else:
			end = mid
	print("Minimum element found is : ", arr[start])
	return
findMinInRotatedSortedArray([5, 6, 7, 8, 9, 10, 1, 2, 3, 4])
findMinInRotatedSortedArray([15, 16, 19, 20, 25, 3, 1, 5, 7, 10, 14])

'''
Find an element in a rotated sorted array
'''
def findElementInRotatedSortedArray(arr, val):
	#find the minimum element first, check if the num lies in range 
	#[min_element, arr[-1] ] or not, if yes then search in the right part from min element to arr[-1]
	#else search in the left part
	if val == arr[0]:
		return 0
	if val == arr[-1]:
		return len(arr)-1

	val_index = -1
	start = 0
	end = len(arr)-1
	while start < end:
		mid = (start+end)//2
		#if we reached in the starting part of increasing part, then break
		if arr[start] <= arr[end]:
			break
		if arr[mid] >= arr[start] and arr[mid]>=arr[end]:
			start = mid+1
		else:
			end = mid

	#check in which part does the element might exist
	end = len(arr)-1
	if val > arr[end]:
		end = start
		start = 0

	#use binary search in the probable section
	while start < end:
		mid = (start+end)//2
		if arr[mid] == val:
			start = mid
			break
		if arr[mid]>val:
			end  = mid
		else:
			start = mid+1
	if arr[start] == val:
		return start
	else:
		return -1

import random

arr = [15, 16, 19, 20, 25, 1, 3, 5, 7, 10, 14]
max_val_in_arr = max(arr)
for ix in range(4):
	found_index = -1
	ind = random.randint(0, len(arr)*2)
	if ind < len(arr):
		found_index = findElementInRotatedSortedArray(arr, arr[ind])
		print('Element searched was : ', arr[ind])
	else:
		rand_val = random.randint(max_val_in_arr + 1, abs(max_val_in_arr)*4)
		found_index = findElementInRotatedSortedArray(arr, rand_val)
		print('Element searched was : ', rand_val)

	if found_index == -1:
		print("Element searched was not found")
	else:
		print("Element found at index : ", found_index)
		print("Value at index: {}, is {}".format(found_index, arr[found_index]))

#returns the index first occurence of an element greater than or equal to val in a sorted array
#assumes sorted behaviour of the array
def lowerBound(arr, val):
	last_found_index = -1
	start = 0
	end = len(arr)-1
	while start <= end:
		#if all the elements in the remaining range are smaller than val 
		#then break out of loop and return the last found index
		if arr[end] < val:
			break

		#if the first element is greater than val, in the remaining section 
		#then break and return the starting index of the remaining range
		if arr[start] >= val:
			last_found_index = start
			break

		#we need to update start and end in such a way that 
		#only smaller elements are always to the left of start
		mid = (start+end)//2
		if arr[mid] >= val:
			last_found_index = mid
			end = mid-1
		else:
			start = mid+1


	return last_found_index

#upper bound returns the first occurence of element that is greater than value we search upper bound for
def upperBound(arr, val):
	#upper bound for a number is just a lower bound of the number+1
	return lowerBound(arr, val+1)

arr = [1, 3, 5, 7, 10, 14, 15, 19, 25]
print("Array is: ", arr)
lower_bound_ind = lowerBound(arr, 0)
upper_bound_ind = upperBound(arr, 0)
print("Lower bound for 0 is: ", lower_bound_ind)
print("Upper bound for 0 is: ", upper_bound_ind)
lower_bound_ind = lowerBound(arr, 1)
upper_bound_ind = upperBound(arr, 1)
print("Lower bound for 1 is: ", lower_bound_ind)
print("Upper bound for 1 is: ", upper_bound_ind)
upper_bound_ind = upperBound(arr, 2)
lower_bound_ind = lowerBound(arr, 2)
print("Lower bound for 2 is: ", lower_bound_ind)
print("Upper bound for 2 is: ", upper_bound_ind)
lower_bound_ind = lowerBound(arr, 12)
upper_bound_ind = upperBound(arr, 12)
print("Lower bound for 12 is: ", lower_bound_ind)
print("Upper bound for 12 is: ", upper_bound_ind)
lower_bound_ind = lowerBound(arr, 19)
upper_bound_ind = upperBound(arr, 19)
print("Lower bound for 19 is: ", lower_bound_ind)
print("Upper bound for 19 is: ", upper_bound_ind)
lower_bound_ind = lowerBound(arr, 25)
upper_bound_ind = upperBound(arr, 25)
print("Lower bound for 25 is: ", lower_bound_ind)
print("Upper bound for 25 is: ", upper_bound_ind)
lower_bound_ind = lowerBound(arr, 26)
upper_bound_ind = upperBound(arr, 26)
print("Lower bound for 26 is: ", lower_bound_ind)
print("Upper bound for 26 is: ", upper_bound_ind)

'''
Binary Search, use lower bound and check if the element at index returned is equal to the value we searched for
'''
def binary_search(arr, val):
	index = lowerBound(arr, val)
	#if lower bound found
	if index != -1:
		#if the element at lower bound index is not equal to val, then return -1
		if arr[index] != val:
			index = -1
	return index


index = binary_search(arr, 0)
print("Number 0 found at index", index)
index = binary_search(arr, 1)
print("Number 1 found at index", index)
index = binary_search(arr, 2)
print("Number 2 found at index", index)
index = binary_search(arr, 12)
print("Number 12 found at index", index)
index = binary_search(arr, 19)
print("Number 19 found at index", index)
index = binary_search(arr, 25)
print("Number 25 found at index", index)
index = binary_search(arr, 26)
print("Number 26 found at index", index)


'''
Sort an array of 0's 1's and 2's
'''
def sort_zeros_ones_twos(arr):
	end = len(arr)-1
	start = 0
	while start < end and arr[start] == 0:
		start+=1

	while end > start and arr[end] == 2:
		end -= 1

	pivot_start = start
	pivot_end = end

	while end >= pivot_start:
		if arr[end] == 0:
			arr[pivot_start], arr[end] = arr[end], arr[pivot_start]
			pivot_start += 1
		else:
			if arr[end] == 2:
				arr[pivot_end], arr[end] = arr[end], arr[pivot_end]
				pivot_end -=1
				if pivot_end == end:
					end -= 1
			else:
				end -= 1

arr = [random.randint(0, 2) for ix in range(15)]
print(arr)
sort_zeros_ones_twos(arr)
print(arr)

'''
Given an arr find the maximum j-i such that A[j] > A[i]
'''

def find_max_diff_i_j(arr):
	if len(arr) <= 1:
		raise ValueError("Array must contain atleast 2 elements")

	max_arr = list(arr)
	min_arr = list(arr)
	for ix in range(1, len(arr)):
		min_arr[ix] = min(min_arr[ix], min_arr[ix-1])
	for ix in range(len(arr)-2, -1, -1):
		max_arr[ix] = max(max_arr[ix], max_arr[ix+1])

	print(max_arr)
	print(min_arr)
	max_diff = -1
	start = 0
	end = 0
	while start < len(arr) and end < len(arr):
		if min_arr[start] < max_arr[end]:
			max_diff = max(max_diff, end-start)
			end += 1
		else:
			start += 1
	return max_diff

#arr = [6699, 6047, 5482, 3021, 2739, 7642]
arr = [random.randint(1, 10000) for ix in range(6)]
print("\n\n\n\nArray: ", arr)
x = find_max_diff_i_j(arr)
print("Max value for j-i = ", x)