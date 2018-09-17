
times = 3
while times <= 3 & times>0:
	password = input('Password: ')
	if password == 'a123456':
		print('access!')
		break
	else:
		times = times-1
		if times == 0:
			print('Fail, bye bye!')
			break
		print('again! 你剩下', times, '次機會')

