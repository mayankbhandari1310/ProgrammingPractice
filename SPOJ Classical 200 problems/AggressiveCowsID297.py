'''
Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls. The stalls are located along a straight line at positions x1,...,xN (0 <= xi <= 1,000,000,000).

His C (2 <= C <= N) cows don't like this barn layout and become aggressive towards each other once put into a stall. 
To prevent the cows from hurting each other, FJ wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. 
What is the largest minimum distance?

Input
t – the number of test cases, then t test cases follows.
* Line 1: Two space-separated integers: N and C
* Lines 2..N+1: Line i+1 contains an integer stall location, xi

Output
For each test case output one integer: the largest minimum distance.

Example:
Input:
1
5 3
1
2
8
4
9
Output:
3
'''


#assumes a list of stalls and distance to be maintained
def check_if_possible(stalls, dist, num_stalls, num_cows):
	last_stall_where_cow_was_placed = stalls[0]
	num_cows_placed = 1
	for ix in range(1, num_stalls):
		if num_cows_placed == num_cows:
			break

		if stalls[ix] - last_stall_where_cow_was_placed >= dist:
			last_stall_where_cow_was_placed = stalls[ix]
			num_cows_placed += 1

	#mistake was made in for loop, about num_cows_placed and num_cows comparison
	if num_cows_placed == num_cows:
		return True
	else:
		return False 



test_cases = int(input())
while test_cases:
	test_cases-=1
	
	input_data = input().split()
	num_stalls, num_cows = int(input_data[0]), int(input_data[1])

	stalls = [0 for ix in range(num_stalls)]
	
	for ix in range(num_stalls):
		stalls[ix] = int(input())

	stalls.sort()
	#print(stalls)

	max_dist = -1
	start = 0
	end = stalls[-1]-stalls[0] + 1

	while start <= end:
		mid = (start + end)//2
		if check_if_possible(stalls, mid, num_stalls, num_cows):
			if max_dist < mid:
				max_dist = mid
			start = mid + 1
		else:
			end = mid-1
	print(max_dist)

