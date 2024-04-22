import sys
import time

func = str(sys.argv[1])
input0 = int(sys.argv[2])
input1 = int(sys.argv[3])

#magic numbers
x = []
y = []
z = []
j = 0

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

def prime(arg1):
	prevAtmpt = []
	tempVar = str(bin(arg1))
	tempVar = tempVar.replace("0b","")
	tempY=[]
	tempX = []
	for i in range(0,len(tempVar)-1):
		tempY.append(False)
		tempX.append(False)
	addLimit = len(tempY)-1
	tempZ = []
	for i in (reversed(tempVar)):
		if int(i):
			tempZ.append(True)
		else:
			tempZ.append(False)
	for a in range(0,(addLimit) if addLimit > 1 else 1):
		y = []
		for b in range(0,len(tempX)):
			y.append("(tempX[" + str(b) + "] and tempY[" + str(a+1) + "])")
		for b in range(0,a+1):
			y.insert(0,"False")
		if a == 0:
			z = []
			x=[]
			for b in range(0,len(tempX)):
				x.append("(tempX[" + str(b) + "] and tempY[" + str(a) + "])")
			for b in range(0,len(x)+a+2):
				z.append(False)
			for b in range(len(x),len(z)):
				x.append("False")
			for b in range(len(y),len(z)):
				y.append("False")
		else:
			z = []
			x=[]
			for b in range(0,len(prevAtmpt)):
				x.append(prevAtmpt[b])
			for b in range(0,len(x)+a+2):
				z.append(False)
			for b in range(len(x),len(z)):
				x.append("False")
			for b in range(len(y),len(z)):
				y.append("False")
		for i in range(0,len(z)):
			part1 = "((("
			part2 = "((("
			if i == 0:
				part1 = part1 + x[(i)] + " and not " + y[i] + ") or ( not " + x[(i)] + " and " + y[i] + ")"
				part2 = part2 + "False)"
			else:
				for k in range(0,i+1):
					if k == 0:
						part1 = part1 + x[(i-k)] + " and " + y[i-k] + ") or ( not " + x[i-k] + " and not " + y[(i-k)] + "))"
						part1 = part1 + " and ((("
						part2 = part2 + "not " + x[(i-k)] + " and " + y[(i-k)] + ") or ( " + x[(i-k)] + " and not " + y[(i-k)] + "))" #first line here
						part2 += " and ((("
					else:
						if k > 1:
							part1 = part1 + " or (("
							part2 += " and (( not "+x[(i-k)] + " and not " + y[(i-k)] + " ) or  ((("
						for l in range(1,k+1):
							if ((k-l) != 0):
								part1 += x[(i-l)] + " and not " + y[(i-l)] + ") or (not " + x[(i-l)] + " and " + y[(i-l)] + " )) and (("
								part2 += "(not "+x[(i-l)] + " and not " + y[(i-l)] + "))) or (("
							else:
								part1 += " ( " + x[(i-l)] + " and " + y[(i-l)] + ")))"
								part2 += "not ( " + x[i-l] + " and " + y[(i-l)] + ")))"
								if k > 1:
									part2 += "))"
			part1 += "))"
			part2 += "))"
			if i == len(prevAtmpt):
				prevAtmpt.append("(" + part1 + str(" or ") + part2 + ")")
			else:
				prevAtmpt[i] = ("(" + part1 + str(" or ") + part2 + ")")
			if a == addLimit - 1:
				z[i] = part1 +" or " + part2
	outputBoolForm = ""
	for i in range(len(tempZ),len(z)):
		tempZ.append(False)
	for i in range(0,len(z)):
		if addLimit != 0:
			if i == 0:
				if not(tempZ[i]):
					outputBoolForm += "not ( " + z[i] + ") "
				else:
					outputBoolForm += "( " + z[i] + ") "
			else:
				if tempZ[i]:
					outputBoolForm += "and ( " + z[i] + ") "
				else:
					outputBoolForm += "and not ( " + z[i] + ") "
		else:
			if i == 0:
				if not(tempZ[i]):
					outputBoolForm += "not ( " + prevAtmpt[i] + ") "
				else:
					outputBoolForm += "( " + prevAtmpt[i] + ") "
			else:
				if tempZ[i]:
					outputBoolForm += "and ( " + prevAtmpt[i] + ") "
				else:
					outputBoolForm += "and not ( " + prevAtmpt[i] + ") "
	return outputBoolForm

def fastMultiplication(arg1,arg2):
	tempVar = 0
	tempVar0 = str(bin(arg2))
	tempVar0 = tempVar0.replace("0b","")
	tempY=[]
	tempX = []
	for i in (reversed(tempVar0)):
		if int(i):
			tempY.append(True)
		else:
			tempY.append(False)
	for i in range(0,len(tempY)):
		if int(tempY[i]):
			tempVar = addition(tempVar,arg1*(pow(2,i)))[1]
	return tempVar

def multiplication(arg1,arg2):
	prevAtmpt = []
	tempVar = str(bin(arg1))
	tempVar = tempVar.replace("0b","")
	tempVar1 = str(bin(arg2))
	tempVar1 = tempVar1.replace("0b","")
	tempY=[]
	tempX = []
	for i in (reversed(tempVar)):
		if int(i):
			tempX.append(True)
		else:
			tempX.append(False)
	for i in (reversed(tempVar1)):
		if int(i):
			tempY.append(True)
		else:
			tempY.append(False)
	tempZ = []
	count0 = 0
	count1 = 0
	addLimit = len(tempY)-1
	for i in tempX:
		if int(i):
			count0 += 1
	for i in tempY:
		if int(i):
			count1 += 1
	if count1 > count0:
		for i in range(0,count1-count0):
			tempX.append(False)
	if count0 > count1:
		for i in range(0,count0-count1):
			tempY.append(False)
	for a in range(0,(addLimit) if addLimit > 1 else 1):
		y = []
		for b in range(0,len(tempX)):
			y.append("(tempX[" + str(b) + "] and tempY[" + str(a+1) + "])")
		for b in range(0,a+1):
			y.insert(0,"False")
		if a == 0:
			z = []
			x=[]
			for b in range(0,len(tempX)):
				x.append("(tempX[" + str(b) + "] and tempY[" + str(a) + "])")
			for b in range(0,len(x)+a+2):
				z.append(False)
			for b in range(len(x),len(z)):
				x.append("False")
			for b in range(len(y),len(z)):
				y.append("False")
		else:
			z = []
			x=[]
			for b in range(0,len(prevAtmpt)):
				x.append(prevAtmpt[b])
			for b in range(0,len(x)+a+2):
				z.append(False)
			for b in range(len(x),len(z)):
				x.append("False")
			for b in range(len(y),len(z)):
				y.append("False")
		for i in range(0,len(z)):
			part1 = "((("
			part2 = "((("
			if i == 0:
				part1 = part1 + x[(i)] + " and not " + y[i] + ") or ( not " + x[(i)] + " and " + y[i] + ")"
				part2 = part2 + "False)"
			else:
				for k in range(0,i+1):
					if k == 0:
						part1 = part1 + x[(i-k)] + " and " + y[i-k] + ") or ( not " + x[i-k] + " and not " + y[(i-k)] + "))"
						part1 = part1 + " and ((("
						part2 = part2 + "not " + x[(i-k)] + " and " + y[(i-k)] + ") or ( " + x[(i-k)] + " and not " + y[(i-k)] + "))" #first line here
						part2 += " and ((("
					else:
						if k > 1:
							part1 = part1 + " or (("
							part2 += " and (( not "+x[(i-k)] + " and not " + y[(i-k)] + " ) or  ((("
						for l in range(1,k+1):
							if ((k-l) != 0):
								part1 += x[(i-l)] + " and not " + y[(i-l)] + ") or (not " + x[(i-l)] + " and " + y[(i-l)] + " )) and (("
								part2 += "(not "+x[(i-l)] + " and not " + y[(i-l)] + "))) or (("
							else:
								part1 += " ( " + x[(i-l)] + " and " + y[(i-l)] + ")))"
								part2 += "not ( " + x[i-l] + " and " + y[(i-l)] + ")))"
								if k > 1:
									part2 += "))"
			part1 += "))"
			part2 += "))"
			if i == len(prevAtmpt):
				prevAtmpt.append("(" + part1 + str(" or ") + part2 + ")")
			else:
				prevAtmpt[i] = ("(" + part1 + str(" or ") + part2 + ")")
			if a == addLimit - 1:
				z[i] = (eval(part1)) or (eval(part2))
	mResult = 0
	for b in range(0,len(z)):
		if z[b]:
			mResult += 2 ** b
	return(mResult)

def addition(arg1,arg2):
	addEquation = ""
	tempVar = str(bin(arg1))
	tempVar = tempVar.replace("0b","")
	tempVar1 = str(bin(arg2))
	tempVar1 = tempVar1.replace("0b","")
	x = []
	y=[]
	z=[]
	for i in (reversed(tempVar)):
		if int(i):
			x.append(True)
		else:
			x.append(False)
	for i in (reversed(tempVar1)):
		if int(i):
			y.append(True)
		else:
			y.append(False)
	for i in range(0,max(len(x),len(y)) + 1):
		z.append(False)
	for j in range(len(x),len(z)):
		x.append(False)
	for j in range(len(y),len(z)):
		y.append(False)

	for i in range(0,len(z)):
		part1 = "((("
		part2 = "((("
		if i == 0:
			part1 = part1 + "x[" + str(i) +"]" + " and not " + "y[" + str(i) + "]" + ") or ( not " + "x[" + str(i) +"]" + " and " + "y["+str(i)+"]" + ")"
			part2 = part2 + "False)"
		else:
			for k in range(0,i+1):
				if k == 0:
					part1 = part1 + "x[" + str(i-k) + "]" + " and " + "y[" + str(i-k) + "]" + ") or ( not " + "x[" + str(i-k)+"]" + " and not " + "y[" + str(i-k) + "]" + "))"
					part1 = part1 + " and ((("
					part2 = part2 + "not " + "x[" + str(i-k) + "]" + " and " + "y["+ str(i-k) + "]" + ") or ( " + "x[" + str(i-k) + "]" + " and not " + "y[" + str(i-k) + "]" + "))" #first line here
					part2 += " and ((("
				else:
					if k > 1:
						part1 = part1 + " or (("
						part2 += " and (( not " + "x[" + str(i-k) + "]" + " and not " + "y[" + str(i-k) + "]" + " ) or  ((("
					for l in range(1,k+1):
						if ((k-l) != 0):
							part1 += "x[" + str(i-l) + "]" + " and not " + "y[" + str(i-l)+"]" + ") or (not " + "x[" + str(i-l)+"]" + " and " + "y["+str(i-l)+"]" + " )) and (("
							part2 += "(not "+"x[" + str(i-l)+"]" + " and not " + "y["+str(i-l)+"]" + "))) or (("
						else:
							part1 += " ( " + "x["+str(i-l)+"]" + " and " + "y["+str(i-l)+"]" + ")))"
							part2 += "not ( " + "x[" +str(i-l) +"]" + " and " + "y["+str(i-l)+"]" + ")))"
							if k > 1:
								part2 += "))"
		part1 += "))"
		part2 += "))"
		z[i] = (eval(part1)) or (eval(part2))
		if i != 0:
			addEquation += " and "
		if z[i]:
			addEquation += "(" + part1 + " or " + part2 + ")"
		else:
			addEquation += "not (" + part1 + " or " + part2 + ")"
	result = 0
	for i in range(0,len(z)):
		if z[i]:
			result += (2 ** i)
	return addEquation,result

if (func == "addition") or (func == "Addition") or (func == "Add") or (func == "add"):
	start = time.time()
	print(addition(input0,input1))
	finish = time.time()
	timeLapse = finish - start
	time_convert(timeLapse)
elif (func == "multiplication") or (func == "Multiplication") or (func == "mul") or (func == "Mul") or (func == "multiply") or (func == "Multiply"):
	start = time.time()
	temp = multiplication(input0,input1)
	print(temp)
	finish = time.time()
	timeLapse = finish - start
	time_convert(timeLapse)
elif (func == "prime"):
	start = time.time()
	temp = prime(input0)
	print(temp)
	finish = time.time()
	timeLapse = finish - start
	time_convert(timeLapse)
elif (func == "fastMultiplication") or (func == "fastmultiplication") or (func == "fmul") or (func == "fMul") or (func == "fmultiply") or (func == "fMultiply"):
	start = time.time()
	temp = fastMultiplication(input0,input1)
	print(temp)
	finish = time.time()
	timeLapse = finish - start
	time_convert(timeLapse)
else:
	print("Invalid function")