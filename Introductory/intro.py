print("Hello World")

variable1="India 1" #string in double quotes
variable2='India 2' #string in single quotes

variable3='India\'s 2'  #string having single quotes we can escape it by backward slash
variable4="India's 2" # if string having single quotes we can use double quotes
variable5="India\"s 2"  #string having double quotes we can escape it by backward slash
variable5='India\"s 2'  # if string having double quotes we can use single quotes

print(variable1)
print(variable2)
print(variable3)
print(variable4)
print(variable5)

concatVaribale=variable1+variable2+"!"  # using + we can do the concatenation
print(concatVaribale)

print("print only first characters = ",variable5[0])
print("print 0 to 3 characters = ",variable5[0:3])
print("print all characters = ",variable5[0:])
print("print last character of string = ",concatVaribale[-1])
print("length of variable1 = ",len(variable1))

concatVaribale=11

print("print last character of string = ",concatVaribale)

print(concatVaribale/10)
print(concatVaribale+10)
print(concatVaribale-10)
print(concatVaribale%10)

def arithmetic_operators(a,b):
    print("inside arithmetic_operators")
    print("a = ",a)
    print("b = ",b)
    print("addition = ",a+b)
    print("subtraction = ", a - b)
    return a*10

arithmetic_operators(5,4)

