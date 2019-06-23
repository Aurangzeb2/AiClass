num1 = float(input('Enter Operand 1:'))
num2 = float(input('Enter Operand 2:'))
op = input('Please provide operator')
if op == '+':
	print('Result of Adding of Numbers:' + str(num1) +','+ str(num2) + '=' + str(num1 + num2))
elif op == '-':
	print('Result of Subtracting of Numbers:' + str(num1) +','+ str(num2) + '=' + str(num1 - num2))
elif op == '*':
	print('Result of Multiplication of Numbers:' + str(num1) +','+ str(num2) + '=' + str(num1 * num2))
elif op == '/':
	print('Result of Division of Numbers:' + str(num1) +','+ str(num2) + '=' + str(num1 / num2))