import random
'''
String matching algorithms:
1. Brute force method
2. Rabin Karp
3. With Finite Automata
4. KMP
'''

'''
Find if str2 exists in str1 if found return the starting index of first occurence
'''

#by brute force method
def stringMatchingBruteForce(str1, str2):
	if len(str1) < len(str2):
		return -1
	start_index = -1
	for ix in range(len(str1) - len(str2) + 1):
		for iy in range(len(str2)):
			if str1[ix+iy] != str2[iy]:
				break

		else:
			start_index = ix
			break
	return start_index


print(stringMatchingBruteForce('manish', 'ish'))
print(stringMatchingBruteForce('mayank', 'manu'))

#by rabin karp method, we will need rolling hash for rabin karp
def rabinKarp(str1, str2):
	
	start_index = -1
	if len(str1) < len(str2):
		return start_index

	primeToTakeModWith = 9887
	commonMultiple = 101
	count = 1

	#should be set to (101^len(str2))%primeToTakeModWith
	#leaving character's value as index in alphabet should be multplied with this number 
	#and then subtracted from the original hash
	val_to_be_multiplied_and_subtracted = 1
	for ix in range(len(str2)-1):
		val_to_be_multiplied_and_subtracted = val_to_be_multiplied_and_subtracted*commonMultiple
		#val_to_be_multiplied_and_subtracted = (val_to_be_multiplied_and_subtracted)%primeToTakeModWith
	def generateFirstHash(str_val):
		#hash1 and hash2 are initial hashes for str1 and str2
		hash_val = 0
		for ix in range(len(str_val)):
			hash_val = ((hash_val*commonMultiple)%primeToTakeModWith + ord(str_val[ix]))%primeToTakeModWith
		return hash_val

	def getNextHash(str_val, cur_hash, index_to_remove, index_to_add):
		#remove the removing index
		temp_val = (cur_hash - (val_to_be_multiplied_and_subtracted*ord(str_val[index_to_remove]))%primeToTakeModWith + primeToTakeModWith)%primeToTakeModWith
		#multiply the temp val by common multiple, and add the val at index_to_add
		hash_val = ((temp_val*commonMultiple)%primeToTakeModWith + ord(str_val[index_to_add]))%primeToTakeModWith
		return hash_val

	def full_check(str1, str2, start_index):
		for ix in range(len(str2)):
			if str1[ix+start_index] != str2[ix]:
				return False
		return True

	#hash of str2
	hash_to_be_matched_with = generateFirstHash(str2)
	#get the starting hash
	cur_hash = generateFirstHash(str1[:len(str2)])
	
	for ix in range(0, len(str1) - len(str2)):
		if cur_hash == hash_to_be_matched_with:
			if full_check(str1, str2, ix):
				start_index = ix
				break
		cur_hash = getNextHash(str1, cur_hash, ix,  ix+len(str2))	
	
	#if no match found then check the last portion
	if start_index == -1:
		if cur_hash == hash_to_be_matched_with:
			if full_check(str1, str2, len(str2)- len(str1)):
				start_index = len(str1) - len(str2)
	
	return start_index

start_index = rabinKarp("Manish", 'ish')
print("'ish' found in  'Manish' at index :", start_index)
start_index =rabinKarp('Mayank', 'manu')
if start_index == -1:
	print("'manu' not found in  'Mayank'")
else:
	print("'manu' found in  'Mayank' at index :", start_index)



'''
KMP algorithm, uses a table the contains info about the suffix that is also a prefix in the array till a point
Video by Back to Back SWE : https://www.youtube.com/watch?v=BXCEFAzhxGY very well explained
'''
def KMP(str1, str2):

	if len(str1) < len(str2):
		return -1

	table = [0]*len(str2)

	def generate_table():
		jx = 1
		ix = 0
		while jx < len(str2):
			while jx < len(str2) and str2[jx] == str2[ix]:
				table[jx] = ix+1
				jx += 1
				ix += 1
			if jx < len(str2):
				table[jx] = 0
				ix = 0
				jx+=1
		
	def findUsingTable():
		jx = 0
		start_index = -1
		ix = 0
		while ix < len(str1) and jx < len(str2):
			if str2[jx] == str1[ix]:
				ix+=1
				jx+=1
			else:
				if jx > 0:
					jx = table[jx-1]
				else:
					ix += 1
		if jx == len(str2):
			start_index = ix-len(str2)

		return start_index

	generate_table()
	start_index = findUsingTable()
	return start_index


start_index = KMP("Manish", 'ish')
print("'ish' found in  'Manish' at index :", start_index)
start_index =KMP('Mayank', 'manu')
if start_index == -1:
	print("'manu' not found in  'Mayank'")
else:
	print("'manu' found in  'Mayank' at index :", start_index)

start_index = KMP("AABAACAADAABAABA", "BAAB")
print("'AABAACAADAABAABA' found in  'BAAB' at index", start_index)