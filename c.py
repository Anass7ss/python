# python calc
operator=input("enter an operator")
num1=float(input("entrer le premiere numero"))
num2=float(input("entrer le deuxieme numero"))
if operator == "+":
    result=num1+num2
    print(round(result))
elif operator=="-":
    result=num1-num2
    print(round(result))
elif operator=="*":
    result= num1*num2
    print(round(result))
elif operator == "/":
    result= num1/num2
    print(round(result))
else:
    print(f"{operator}is not valid")
