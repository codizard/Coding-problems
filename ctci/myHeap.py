class MinHeap(object):
	def __init__(self):
		self.heap = []
		self.size = 0

	def insert(self, val):
		if len(self.heap) == 0:
			self.heap.append(val)
			self.size +=1
		else:
			self.heap.append(val)
			self.size +=1
			# print "This is the heap before performing heapify ",self.heap, self.getParent(self.size-1)
			self.heapifyUp()
			# print "This is the heap after performing heapify ",self.heap


	def delete(self):
		if len(self.heap) > 0:
			self.heap[0] = self.heap[self.size-1]
			self.size -=1	
			print "After delete", self.heap
			self.heapifyDown()

	def getParent(self, index):
		return self.heap[(index - 1) /2]

	def getParentIndex(self, index):
		return (index-1)/2

	def hasParent(self, index):
		if index == 0:
			return False
		if self.getParentIndex(index) < self.size:
			return True
		return False

	def heapifyUp(self):
		index = self.size-1
		last = self.heap[index]
		while (self.hasParent(index)):
			pIndex = self.getParentIndex(index)
			if self.heap[pIndex] > self.heap[index]:
				self.heap[pIndex], self.heap[index] = self.heap[index], self.heap[pIndex]
				index = pIndex
			else:
				break

	def printHeap(self):
		print self.heap
A = MinHeap()
A.insert(10)
A.insert(5)
A.insert(30)
A.insert(15)
A.insert(4)
A.insert(0)
A.printHeap()
A.delete()


