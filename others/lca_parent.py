class Node():
	def __init__(self, val):
		self.parent = None
		self.value = val

	def lca(p, q):
		if p.parent is None or q.parent is None:
			return None

		if p.parent == q.parent:
			return p.parent
		if p.parent == q:
			return q
		if q.parent == p:
			return p

		return lca(p.parent, q.parent)