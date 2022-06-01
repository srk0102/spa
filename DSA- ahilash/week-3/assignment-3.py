def preop(operator):
	if operator == '+' or operator == '-':
		return 1
	return 0

def applyOp(a, b, operator):
	if operator == '+': return a + b
	if operator == '-': return a - b

def evaluate(tkns):
	values = []
	operators = []
	i = 0
	while i < len(tkns):
		if tkns[i] == ' ':
			i += 1
			continue
		elif tkns[i] == '(':
			operators.append(tkns[i])
		elif tkns[i].isdigit():
			val = 0
			while (i < len(tkns) and
				tkns[i].isdigit()):
				val = (val * 10) + int(tkns[i])
				i += 1
			values.append(val)
			i-=1
		elif tkns[i] == ')':
			while len(operators) != 0 and operators[-1] != '(':
				val2 = values.pop()
				val1 = values.pop()
				operator = operators.pop()
				values.append(applyOp(val1, val2, operator))
			operators.pop()
		else:
			while (len(operators) != 0 and
				preop(operators[-1]) >=
				preop(tkns[i])):
				val2 = values.pop()
				val1 = values.pop()
				operator = operators.pop()
				values.append(applyOp(val1, val2, operator))
			operators.append(tkns[i])

		i += 1
	while len(operators) != 0:
		val2 = values.pop()
		val1 = values.pop()
		operator = operators.pop()
		values.append(applyOp(val1, val2, operator))
	return values[-1]



print(evaluate("10 + 2 - 6"))
print(evaluate("100 + 2 + 12"))
print(evaluate("100 + ( 2 + 12 )"))
print(evaluate("100 + ( 2 + 12 ) - 14"))