password = input('What is the password? ')
while password not in ['Open Sesame']:
	password = input('Password is invalid, try agian! ')

print('Password is valid, welcome! ')