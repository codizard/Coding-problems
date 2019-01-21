import Queue

class Node:
	def __init__(self, val):
		self.data = val
		self.left = None
		self.right = None

currentSum = 0

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def addNode(self, val):
		if self.root is None:
			self.root = Node(val)
		else:
			self.addNodeHelper(self.root, val)

	def addNodeHelper(self, currentNode, val):
		if val < currentNode.data:
			if currentNode.left is None:
				currentNode.left = Node(val)
			else:
				self.addNodeHelper(currentNode.left, val)
		elif val > currentNode.data:
			if currentNode.right is None:
				currentNode.right = Node(val)
			else:
				self.addNodeHelper(currentNode.right, val)

	def printTreeInorder(self):
		if self.root:
			ele =  self._printTreeInorder(self.root, [])
			return ele
		else:
			print "Tree is empty"
	def _printTreeInorder(self, currentNode, arr):
		if currentNode:
			self._printTreeInorder(currentNode.left, arr)
			arr.append(currentNode.data)
			self._printTreeInorder(currentNode.right, arr)
		return arr

	def validateBST(self):
		if self.root:
			return self._validateBST(self.root,[])
		else:
			return True

	def _validateBST(self, currentNode, arr):
		if currentNode:
			self._validateBST(currentNode.left, arr)
			if len(arr) > 1 and currentNode.data < arr[-1]:
				return False
			else:
				arr.append(currentNode.data)
			self._validateBST(currentNode.right, arr)
		return True

	def printTreePreorder(self):
		if self.root:
			ele =  self._printTreePreorder(self.root, [])
			ele = [x for x in ele if x is not None]
			print ele
		else:
			print "Tree is empty"

	def _printTreePreorder(self, currentNode, arr):
		if currentNode is None:
			arr.append("None")
			return arr
		arr.append(currentNode.data)
		self._printTreePreorder(currentNode.left, arr)
		self._printTreePreorder(currentNode.right, arr)
		return arr	

	def isNodePresent(self, val):
		if self.root:
			return self._isNodePresent(self.root, val)

	def _isNodePresent(self, currentNode, val):
		if currentNode is None:
			return False
		if currentNode.data == val:
			return True
		elif currentNode.data > val:
			return self._isNodePresent(currentNode.left, val)
		else:
			return self._isNodePresent(currentNode.right, val)

	def getMiminumOfRightSubtree(self, currentNode):
		if currentNode.left is None:
			return currentNode.data
		else:
			return self.getMiminumOfRightSubtree(currentNode.left)

	def constructTreeFromInorderTraversal(self, arr):
		if len(arr) == 0:
			return None
		if len(arr) == 1:
			node = Node(arr[0])
			return node
		mid = len(arr)/2
		root = Node(arr[mid])
		root.left = self.constructTreeFromInorderTraversal(arr[:mid])
		root.right = self.constructTreeFromInorderTraversal(arr[mid+1:])

	def sumOfBinaryTree (self):
		return self.sumOfBinaryTreeHelper(self.root)

	def sumOfBinaryTreeHelper(self, currentNode):
		if not currentNode:
			return 0
		else:
			return self.sumOfBinaryTreeHelper(currentNode.left) + self.sumOfBinaryTreeHelper(currentNode.right) + currentNode.data

	def convertToGreaterSumTree(self):
		self._convertToGreaterSumTree(self.root)

	def _convertToGreaterSumTree(self, currentNode):
		global currentSum
		if currentNode:
			self._convertToGreaterSumTree(currentNode.right)
			temp = currentNode.data 
			if currentSum > currentNode.data:
				currentNode.data = currentSum
			currentSum +=temp
			self._convertToGreaterSumTree(currentNode.left)
		return currentNode

	def levelOrderTraversal(self):
		self._levelOrderTraversal(self.root)

	def _levelOrderTraversal(self, currentNode):
		if not currentNode:
			return
		stack = []
		stack.append((currentNode, 1))
		while stack:
			node, level = stack.pop(0)
			print node.data, level
			if node.left:
				stack.append((node.left, level+1))
			if node.right:
				stack.append((node.right, level+1))

	def delNode(self, val):
		if self.root is None:
			return
		else:
			self.head = self._delNode(self.root, val)

	def findMin(self, root):
		if root.left:
			self.findMin(root.left)
		return root.data
	def _delNode(self, currentNode, val):
		
		if val < currentNode.data:
			currentNode.left = self._delNode(currentNode.left, val)
		elif val > currentNode.data:
			currentNode.right = self._delNode(currentNode.right, val)
		else:
			if currentNode.left is None:
				temp = currentNode.right
				# currentNode = None
				return temp
			elif currentNode.right is None:
				temp = currentNode.left
				# currentNode = None
				return temp
			else:
				minElement = self.findMin(currentNode.right)
				currentNode.val = minElement
				currentNode.right = self.delNode(minElement)
				
		return currentNode

	def _levelOrderTraversalWithMap(self, root):
		if root is None:
			return {}
		else:
			res = {}
			s = [root]
			while len(s) > 0:
				cur = s.pop(0)
				if cur.left:
					if cur.left.data in res:
						res[cur.left.data].append(cur.data)
					else:
						if cur.data != self.root.data:
							res[cur.left.data] = [res[cur.data], cur.data]
						else:
							res[cur.left.data] = [cur.data]	
					s.append(cur.left)
				if cur.right:
					if cur.right.data in res:
						res[cur.right.data].append(cur.data)
					else:
						res[cur.right.data] = [cur.data]
					s.append(cur.right)
		return res
	def levelOrderTraversalWithMap(self):
		return self._levelOrderTraversalWithMap(self.root)

	def lowestCommonAncestor(self, n1, n2):
		return self.findLCA(self.root, n1, n2).data

	def findLCA(self, root, n1, n2): 
	      
	    # Base Case 
	    if root is None: 
	        return None
	  
	    # If either n1 or n2 matches with root's key, report 
	    #  the presence by returning root (Note that if a key is 
	    #  ancestor of other, then the ancestor key becomes LCA 
	    if root.data == n1 or root.data == n2: 
	        return root  
	  
	    # Look for keys in left and right subtrees 
	    left_lca = self.findLCA(root.left, n1, n2)  
	    right_lca = self.findLCA(root.right, n1, n2) 
	  
	    # If both of the above calls return Non-NULL, then one key 
	    # is present in once subtree and other is present in other, 
	    # So this node is the LCA 
	    if left_lca and right_lca: 
	        return root  
	  
	    # Otherwise check if left subtree or right subtree is LCA 
	    return left_lca if left_lca is not None else right_lca 

	def _findKthlargestNode(self, currentNode):
		global x
		if currentNode.right:
			return self._findKthlargestNode(currentNode.right)
		else:
			x-=1
		if x == 0:
			return currentNode.data


	def findKthLargestNode(self, k):
		if self.root is None:
			return None
		else:
			return self._findKthlargestNode(self.root)


	def getHeight(self):
		if self.root is None:
			return 0
		else:
			return self._getHeight(self.root)

	def _getHeight(self, currentNode):
		if currentNode is None:
			return 0

		lHeight = self._getHeight(currentNode.left) + 1
		rHeight = self._getHeight(currentNode.right) + 1

		if lHeight > rHeight:
			return lHeight
		else:
			return rHeight

	def BFS(self):
		if self.root is None:
			return []
		else:
			res = []
			stack = [self.root]
			while len(stack) > 0:
				curr = stack.pop(0)
				res.append(curr.data)
				if curr.left:
					stack.append(curr.left)
				if curr.right:
					stack.append(curr.right)
		return res

x = 2
arr2 = [25, 15, 12, 20, 75, 50, 100, 85]
a = BinarySearchTree()
for num in arr2:
	a.addNode(num)
print a.printTreeInorder()
a.delNode(12)
print a.printTreeInorder()
