# python weight convrter
weight=float(input("entrer votre poids"))
unit=input("kilograme ou pounnds??")
if unit=="k":
    weight=weight*2.205
    unit="lbs"
elif unit=="L":
     weigh=weight/2.205
     unit="kgs"
else:
     print(f"{unit} was not valid")
