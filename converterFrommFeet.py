#convert from feet to inches
def feetToInches(feet):
    inches = feet * 12
    return inches
#convert from feet to yards
def feetToYards(feet):
    yards = feet / 3
    return yards    
#convert from feet to miles
def feetToMiles(feet):
    miles = feet / 5280
    return miles

#take feet input from user
def takeFeetInput():
    feet = float(input("Enter the value in feet: "))
    return feet
def printConversions(feet):
    print(f"{feet} feet is equal to {feetToInches(feet)} inches.")
    print(f"{feet} feet is equal to {feetToYards(feet)} yards.")
    print(f"{feet} feet is equal to {feetToMiles(feet)} miles.")

feet = takeFeetInput()
printConversions(feet)
