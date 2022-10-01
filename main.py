
words = input('Enter the list: ').split()

are = ['a', 'r', 'e']
idxlst = []
for i in range(len(words)):
	# idxlst = [ words[i].find(are[j]) for j in range(len(are))] 
	for j in range(len(are)):
		if j == 0: 
			prev = 0 
		else:
			prev = idxlst[j-1]
		idx = words[i].find(are[j], prev) 
		if idx == -1:
			break
		idxlst.append(idx)
	else:
		if sorted(idxlst) == idxlst:
			print (words[i], end=' ')
print ()


