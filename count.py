current_number = 1
while current_number <=10:
	print(current_number)
	current_number += 1
 
prompt = '\nTelling some thing,and I will repeat back to you'
prompt += "\nEnter 'quite' to end the program  "
 
message = ''
while message != 'quite':
	 message = input(prompt)
	 if message != 'quite':
		 print(message)
		 
number = 0
while number <= 10:
	number += 1
	if number %2 == 0:
		continue
	print(number)			 
		 
