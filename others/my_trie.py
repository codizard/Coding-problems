class TrieNode():

	def __init__(self):
		self.children = [None] * 26
		self.isEndOfWord = False

class Trie():

	def __init__(self):
		self.root = TrieNode()

	def hasNoChildren(self, node):
		for x in node.children:
			if x:
				return False
		return True

	def isLeafNode(self, node):
		return node.isEndOfWord == True

	def insert(self, word):
		cur = self.root
		for i in range(len(word)):
			index = ord(word[i]) - ord('a')
			if not cur.children[index]:
				cur.children[index] =TrieNode()
			cur = cur.children[index]


		cur.isEndOfWord = True

	def delete(self, key):
		if len(key) > 0:
			return self._delete(self.root, key, 0)


	def _delete(self, currentNode, key, level):
		if currentNode:
			if level == len(key):
				if currentNode.isEndOfWord == True:
					currentNode.isEndOfWord = False

				return self.hasNoChildren(currentNode)
			
			else:
				index = ord(key[level]) - ord('a')
				if self._delete(currentNode.children[index], key, level + 1):
					del currentNode.children[index]

					return (not self.isLeafNode(currentNode) and self.hasNoChildren(currentNode))

		return

	def search(self, word):   
		# Search key in the trie 
		# Returns true if key presents  
		# in trie, else false 
		cur = self.root 
		for i in range(len(word)):
			index = ord(word[i]) - ord('a')
			if cur.children:
				if cur.children[index] is None:
					return False
			cur = cur.children[index]
		return cur is not None and cur.isEndOfWord == True
			
		
keys = ["these","p","there","anaswe","any","by","their"] 

t = Trie() 
for key in keys: 
	t.insert(key)

# print t.search("these")
# print t.search("answer")
print t.search("these")
t.delete("these")
print t.search("these ")
