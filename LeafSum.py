from BinaryTree import *
'''
Returns the sum of all Binary Tree leaves
'''

def leaf_sum_recursive(node):
	while node:
		if node.left and node.right:
			return leaf_sum_recursive(node.left) + leaf_sum_recursive(node.right)
		elif node.left:
			return leaf_sum_recursive(node.left)
		elif node.right:
			return leaf_sum_recursive(node.right)
		else:
			return node.value

def leaf_sum_iterative(node):
	if node is None:
		return None
	stack = []
	stack.append(node)
	sum = 0
	while len(stack) > 0:
		cur_node = stack.pop()
		if cur_node.left is not None:
			stack.append(cur_node.left)
			if cur_node.left.left is None and cur_node.left.right is None:
				sum += cur_node.left.value
		if cur_node.right is not None:
			stack.append(cur_node.right)
			if cur_node.right.left is None and cur_node.right.right is None:
				sum += cur_node.right.value
	return sum

b = BinaryTree()
b.add(10)
b.add(15)
b.add(5)
