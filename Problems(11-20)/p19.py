def countingSundays():
	days = []
	days.append([1,1,1901,2])
	days.append([2,1,1901,3])
	temp = [1,1,1901,2]
	thirty = [4,6,9,11]
	thirty_one = [1,3,5,7,8,10]
	
	while temp != [31,12,2000,7] :
		temp[3]+=1
		temp[0]+=1
		if temp[3] == 8:
			temp[3] = 1

		if temp[0] == 31 and temp[1] in thirty:
			temp[0] = 1
			temp[1] += 1
		elif temp[0] == 32 and temp[1] in thirty_one:
			temp[0] = 1
			temp[1] += 1
		elif temp[0] == 32 and temp[1] == 12:
			temp[0] = 1
			temp[1] = 1
			temp[2] += 1
		elif temp[0] == 30 and temp[1] == 2 and temp[2]%4 == 0:
			temp[0] = 1
			temp[1] +=1
		elif temp[0] == 29 and temp[1] == 2 and temp[2]%4 != 0:
			temp[0] = 1
			temp[1] += 1
		temp = [temp[0],temp[1],temp[2],temp[3]]
		days.append(temp)

	sundayfirst = 0
	for day in days:
		if day[0] == 1 and day[3] == 7:
			sundayfirst += 1
	return sundayfirst



# for some reason the 2nd of january of 1901 isn't included so I had to append it myself

print(countingSundays())
