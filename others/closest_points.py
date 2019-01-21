import math
import heapq
def find_distance(point, origin):
	return math.sqrt(pow(point[1] - origin[1], 2) + pow(point[0] - origin[0], 2)) 
def compute_distance(points):
	distance_map = {}

	for point in points:
		if point not in distance_map:
			distance_map[point] = find_distance(point, origin)
	return distance_map

def find_k_closest_points(points,origin,k):	
	distance_map = compute_distance(points)
	a = convert_map_to_array(distance_map)
	res = []
	print a[:k]
	return None
	# return a[:k]
	closestDistance = float('inf')
	currentPoint = []
	res = set()
	while k > 0:
		k-=1
		for point in points:
			if point not in res:
				if distance_map[point] < closestDistance:
					currentPoint = point
					closestDistance = distance_map[point]
		res.add(currentPoint)
		currentPoint = []
		closestDistance = float('inf')

	return list(res)
def convert_map_to_array(distance_map):
	arr = []
	for key in distance_map.keys():
		heapq.heappush(arr, (distance_map[key], key))
	return arr

arrpoints = [[1,2], [1,2], [2,2], [3,4], [-3,0], [1,2]]
points = [(1,2), (1,2), (2,2), (3,4), (-3,0), (1,2)]
origin = [0,0]
k = 2

print find_k_closest_points(points, origin, k)
# print sorted(points, key = lambda x: x[1])