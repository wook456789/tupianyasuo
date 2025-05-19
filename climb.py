mountains = {}

p_active = True

while p_active:
	name = input('\nwhat is your name ')
	m = input('which mountain you like to climb ')
	
	mountains[name] = m
	
	for name,m in mountains.items():
		print(f'{name} should like to climb {m}')
	
	repeat = input('would you like to continue(yes/no) ')
	if repeat == 'no':
		p_active = False 			
			
