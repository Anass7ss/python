# python compound interset calculator
p=0
rate=0
time=0

while p<=0:
    p=input("entrer un principale amount:")
    if p<=0:
        print('principale cant be less than or equal to zero')

while time<=0:
    time=input("entrer une temps amount:")
    if time<=0:
        print('principale cant be less than or equal to zero')
        
while rate<=0:
    rate=input("entrer une temps amount:")
    if rate<=0:
        print('principale cant be less than or equal to zero')
total=p*pow((1+rate/100),time)
print(f"balence after {time}years:{rate}")