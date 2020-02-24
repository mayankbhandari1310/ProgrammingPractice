import random
from collections import deque
class TreeNode:
	def __init__(self, val):
		self.data = val
		self.left_child = None
		self.right_child = None

#Better to use binary search tree, instead of simple binary tree 
class BSTree:
	def __init__(self):
		self.root = None

	def add_node(self, data):
		if not self.root:
			self.root = TreeNode(data)
			return
		temp = self.root
		while temp:
			if temp.data < data:
				if not temp.right_child:
					temp.right_child = TreeNode(data)
					break
				else:
					temp = temp.right_child
			else:
				if not temp.left_child:
					temp.left_child = TreeNode(data)
					break
				else:
					temp = temp.left_child


	def delete(self, root, val):
		if not root:
			return None
		if root.data == val:
			#if a leave return None
			if not root.left_child and not root.right_child:
				del root
				return None
			#if have right child only then return the right child
			if not root.left_child:
				temp = root.right_child
				del root
				return temp
			#if have left child only then return the left child only
			if not root.right_child:
				temp = root.left_child
				del root
				return temp

			#if have both child, then replace with just next greater element and replace and call recursively on the subtree
			temp = root.right_child
			while temp.left_child:
				temp = temp.left_child
			root.data, temp.data = temp.data, root.data
			root.right_child = self.delete(root.right_child, val)
			return root
		else:
			if root.data < val:
				root.right_child = self.delete(root.right_child, val)
			else:
				root.left_child = self.delete(root.left_child, val)
			return root
	#treat like bst
	def delete_node(self, val):
		self.root = self.delete(self.root, val)

	#treating like binary tree
	def inorder_traversal(self, root, order_list):
		if not root:
			return
		self.inorder_traversal(root.left_child, order_list)
		order_list.append(root.data)
		self.inorder_traversal(root.right_child, order_list)

	#treating like binary tree
	def preorder_traversal(self, root, order_list):
		if not root:
			return
		order_list.append(root.data)
		self.preorder_traversal(root.left_child, order_list)
		self.preorder_traversal(root.right_child, order_list)

	#treating like a binary tree
	def postorder_traversal(self, root, order_list):
		if not root:
			return
		self.postorder_traversal(root.left_child, order_list)
		self.postorder_traversal(root.right_child, order_list)
		order_list.append(root.data)

	#treating like a binary tree
	def level_wise_traversal(self, root, order_list=[]):
		if not root:
			return order_list
		d = deque()
		d.append((1, root))
		while d:
			level, node = d[0]
			order_list.append(node.data)
			d.popleft()
			if node.left_child:
				d.append((level+1, node.left_child))
			if node.right_child:
				d.append((level+1, node.right_child))

	#returns node if found else None
	def find_element_treating_as_binary_tree(self, root, val):
		if not root:
			return None

		if root.data == val:
			return root
		else:
			temp1 = self.find_element_treating_as_binary_tree(root.left_child, val)
			temp2 = self.find_element_treating_as_binary_tree(root.right_child, val)
			node = None
			if temp1:
				node = temp1
			else:
				node = temp2
			return node

	#returns node if found else None
	def find_element_treating_as_BST(self, root, val):
		if not root:
			return None
		if root.data == val:
			return root
		if root.data < val:
			return self.find_element_treating_as_BST(root.right_child, val)
		else:
			return self.find_element_treating_as_BST(root.left_child, val)
	

	#treating as binary tree
	def delete_tree(self, root):
		if not root:
			return None
		root.left_child = self.delete_tree(root.left_child)
		root.right_child = self.delete_tree(root.right_child)
		root = None
		return root

	#return the size of the tree
	def find_size_of_tree(self, root):
		if not root:
			return 0
		return self.find_size_of_tree(root.left_child) + self.find_size_of_tree(root.right_child) + 1


	#treating as binary tree
	def get_max_depth(self, root):
		if not root:
			return 0
		return max(self.get_max_depth(root.left_child), self.get_max_depth(root.right_child)) + 1

	#treating as binary tree
	def get_the_deepest_element(self, root):
		if not root:
			return None
		d = deuque()
		d.push(root)
		temp = None
		while d:
			temp = d[0]
			d.pop()
			if temp.left_child:
				d.append(temp.left_child)
			
			if temp.right_child:
				d.append(temp.right_child)
		return temp

	#check if two trees are identical
	def check_trees_identical(self, root1, root2):
		if root1==None and root2==None:
			return True
		if (root1 and not root2) or (root2 and not root1):
			return False
		if not root1.data == root2.data :
			return False
		else:
			return self.check_trees_identical(root1.left_child, root2.left_child) and self.check_trees_identical(root1.right_child, root2.right_child)

	#treating as binary_tree
	def print_all_paths_from_root_to_leaves(self, root, path):
		if not root:
			return
		if not root.left_child and not root.right_child:
			path.append(root.data)	
			print(path)		 
			path.pop()
			return
		path.append(root.data)
		self.print_all_paths_from_root_to_leaves(root.left_child, path)
		path.pop()
		path.append(root.data)
		self.print_all_paths_from_root_to_leaves(root.right_child, path)
		path.pop()
		return

	#treating as a binary tree
	def mirror_a_binary_tree(self, root):
		if not root:
			return
		root.left_child, root.right_child = root.right_child, root.left_child
		self.mirror_a_binary_tree(root.left_child)
		self.mirror_a_binary_tree(root.right_child)

	#return a copy of binary_tree
	def copy_tree(self, root):
		if not root:
			return None
		temp = TreeNode(root.data)
		temp.left_child = self.copy_tree(root.left_child)
		temp.right_child = self.copy_tree(root.right_child)
		return temp

my_tree = BSTree()
list_to_create_BST = [4, 3, 8, 1, 2, 6, 10, 5, 7, 9, 11]
for item in list_to_create_BST:
	my_tree.add_node(item)
order_list = []
my_tree.level_wise_traversal(my_tree.root, order_list)
print("Level order Traversal: ", order_list)

'''
Print all paths from root to leaves
'''
path = []
my_tree.print_all_paths_from_root_to_leaves(my_tree.root, path)

'''
PreOrder Traversal
'''
order_list = []
my_tree.preorder_traversal(my_tree.root, order_list)
print("preorder_traversal: ", order_list)


'''
PostOrder Traversal
'''
order_list = []
my_tree.postorder_traversal(my_tree.root, order_list)
print("postorder_traversal: ", order_list)

'''
InOrder Traversal
'''
order_list = []
my_tree.inorder_traversal(my_tree.root, order_list)
print("inorder_traversal: ", order_list)

'''
Finding element in a binary tree
'''
val = 9
node = my_tree.find_element_treating_as_binary_tree(my_tree.root, val)
print("Val searched = ", val, "Node returned : ", node.data)

'''
Finding element in a BST
'''
val = 6
node = my_tree.find_element_treating_as_BST(my_tree.root, val)
print("Val searched = ", val, "Node returned : ", node.data)


'''
Finding the size of the tree
'''
tree_size = my_tree.find_size_of_tree(my_tree.root)
print("Tree size = ", tree_size)

'''
Find max depth
'''
max_depth = my_tree.get_max_depth(my_tree.root)
print("Max depth = ", max_depth)
my_tree.add_node(12)
max_depth = my_tree.get_max_depth(my_tree.root)
print("Max depth = ", max_depth)

'''
Delete Node from a tree
'''
my_tree.delete_node(12)
max_depth = my_tree.get_max_depth(my_tree.root)
print("Max depth = ", max_depth)
order_list = []
my_tree.level_wise_traversal(my_tree.root, order_list)
print("level_wise_traversal: ", order_list)
print("Deleting the root")
my_tree.delete_node(4)
order_list = []
my_tree.level_wise_traversal(my_tree.root, order_list)
print("level_wise_traversal: ", order_list)

my_tree3 = BSTree()
list_to_create_BST = [4, 2, 8, 5, 1, 7, 6, 13, 10, 12, 11]
for item in list_to_create_BST:
	my_tree3.add_node(item)
my_tree3.delete_node(8)
order_list = []
my_tree3.level_wise_traversal(my_tree3.root, order_list)
print("Tree 3 level_order_traversal", order_list)

'''
Check if two trees are identical or not
'''
print("Creating by same list")
my_tree1 = BSTree()
my_tree2 = BSTree()
list_to_create_BST = [4, 3, 8, 1, 2, 6, 10, 5, 7, 9, 11]
for item in list_to_create_BST:
	my_tree1.add_node(item)
	my_tree2.add_node(item)

are_trees_identical = my_tree1.check_trees_identical(my_tree1.root, my_tree2.root)
print("Trees identical : ", are_trees_identical)

print("Creating by different lists")
my_tree1 = BSTree()
my_tree2 = BSTree()
list_to_create_BST = [4, 3, 8, 1, 2, 6, 10, 5, 7, 9, 11]
for item in list_to_create_BST:
	my_tree1.add_node(item)

for item in reversed(list_to_create_BST):
	my_tree2.add_node(item)

are_trees_identical = my_tree1.check_trees_identical(my_tree1.root, my_tree2.root)
print("Trees identical : ", are_trees_identical)


'''
Mirror a binary tree
'''
my_tree2 = BSTree()
my_tree2.root = my_tree1.copy_tree(my_tree1.root)
my_tree2.mirror_a_binary_tree(my_tree2.root)
order_list = []
my_tree2.level_wise_traversal(my_tree2.root, order_list)
print(order_list)
my_tree2.root = my_tree2.delete_tree(my_tree2.root)
order_list = []
my_tree2.level_wise_traversal(my_tree2.root, order_list)
print("Order list: ", order_list)

