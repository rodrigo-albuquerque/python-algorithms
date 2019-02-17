def inorderSuccessor(root, p):
	"""
  returns smallest larger value to p
	"""
	if root is None:
		return None
	n = root
	potential_successor = None
	while n:
		if p.value < n.value:
			potential_successor = n
			n = n.left
		elif p.value > n.value:  
			n = n.right
		elif n.value == p.value:
			if n.right:
				n = n.right
				while n.left:
					n = n.left
				return n.value
			else:
				return potential_successor.value
	return None
