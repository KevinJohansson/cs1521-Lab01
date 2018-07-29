strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = strings[0]
for i in range(1,6):
	sentence += (' ' + strings[i])
print(sentence)


print(' '.join(strings))
