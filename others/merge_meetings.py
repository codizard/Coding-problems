def mergeMeetings(meetingArr):
	if len(meetingArr) == 0:
		return []
	res = []
	sorted_arr = sorted(meetingArr, key = lambda x:x[0])
	start_time, end_time = None, None
	for i in range(len(sorted_arr)):
		if not start_time and not end_time:
			start_time = sorted_arr[i][0]
			end_time = sorted_arr[i][1]
		else:
			curr_start_time, curr_end_time = sorted_arr[i][0], sorted_arr[i][1]
			if curr_start_time <= end_time:
				end_time = max(end_time, curr_end_time)	
			else:
				res.append((start_time, end_time))
				start_time, end_time = curr_start_time, curr_end_time
	if start_time and end_time:
		res.append((start_time,end_time))
	
	return res
print mergeMeetings([(1, 10), (2, 6), (3, 5), (7, 9)])