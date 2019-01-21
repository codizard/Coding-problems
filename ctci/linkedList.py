class Node:
	def __init__(self, val):
		self.data = val
		self.next = None
		
class LinkedList:
	def __init__(self):
		self.head = None

	def add(self, val):
		if self.head is None:
			self.head = Node(val)
		else:
			curr = self.head
			while curr.next:
				curr = curr.next
			curr.next = Node(val)

	def printList(self):
		curr = self.head
		while curr:
			print curr.data
			curr = curr.next

	def reverse_ll(self):
		if self.head is None:
			return None
		prev = None
		cur = self.head
		nxt = self.head
		while cur:
			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt
			self.head = prev

	def reverse_k_elements(self, k):
		def _reverse_k_elements(head, k):
			prev = None
			cur = head
			nxt = head
			count = 0
			while cur and count < k:
				nxt = cur.next
				cur.next = prev
				prev = cur
				cur = nxt
				count += 1
			if nxt is not None:
				head.next = _reverse_k_elements(nxt, k)
			return prev
		self.head = _reverse_k_elements(self.head, k)

class CircularLinkedList():
	def __init__(self):
		self.head = None

	def add(self, val):
		if self.head is None:
			self.head = Node(val)
			self.head.next = self.head
		else:
			if self.head.next == self.head:
				self.head.next = Node(val)
				self.head.next.next = self.head
			else:	
				curr = self.head 
				while curr.next != self.head :
					curr = curr.next
				curr.next = Node(val)
				curr.next.next = self.head

	def printList(self):
		if self.head is None:
			print None
		else:
			print self.head.data
			if self.head.next is None:
				print self.head.data
			else:
				curr = self.head.next
				while curr != self.head:
					print curr.data
					curr = curr.next

	def insertNodeIntoSortedLinkedList(self, val):
		if self.head is None:
			return False
		else:
			curr = self.head
			if val < curr.data:
				while curr.next != self.head:
					curr = curr.next
				curr.next = Node(val)
				curr.next.next = self.head
				self.head = curr.next
			else:
				while curr.next.data < val and curr.next != self.head:
					curr=curr.next
				temp = curr.next
				curr.next = Node(val)
				curr.next.next = temp

a = LinkedList()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.add(6)
a.add(7)
a.add(8)
a.reverse_k_elements(3)
a.printList()