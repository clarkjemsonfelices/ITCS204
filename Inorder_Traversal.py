import random

class TreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def inOrderTraversal(node):
	if node is None:
		return
	inOrderTraversal(node.left)
	print(node.data, end=", ")
	inOrderTraversal(node.right)

array=['R', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
random.shuffle(array) # Cancel this to stop random

root = TreeNode(array[0])
nodeA = TreeNode(array[1])
nodeB = TreeNode(array[2])
nodeC = TreeNode(array[3])
nodeD = TreeNode(array[4])
nodeE = TreeNode(array[5])
nodeF = TreeNode(array[6])
nodeG = TreeNode(array[7])

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Traverse
inOrderTraversal(root)
print()