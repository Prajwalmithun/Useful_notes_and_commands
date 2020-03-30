
names = open('nameslist.txt','r').read().split('\n')
rever = open('reversedlist.txt','w')

reversed_name_list = []

for name in names:
	if name == '':
		break
	else:
		each_name_broken_list = name.split('.')	
		rev = each_name_broken_list[1] + '.' + each_name_broken_list[0]
		#reversed_name_list.append(rev)
		rever.write(rev + '\n')

#print(reversed_name_list)
