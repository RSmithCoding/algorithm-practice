"""1. Fuel economy log
A van’s fill-ups are stored as (miles driven, litres put in). Work out the MPG for each fill-up, 
the best and worst, and the overall average. UK MPG uses 4.546 litres per gallon."""

def getmpg(miles, litres):
    gallons = litres / 4.546
    mpg = miles / gallons
    return mpg

x = 1
mpg_list = []

for van in input:
    mpg = getmpg(van[0],van[1])
    print(f"Fill up {x} shows {mpg:.2f} mpg")
    x = x + 1
    mpg_list.append(mpg)

average = sum(mpg_list) / len(mpg_list)

print("")
print(f"The average mpg for the fill ups is {average:.1f}\n")

print(f"The highest mpg recorded was {max(mpg_list):.2f}\n")

print(f"The lowest mpg recorded was {min(mpg_list):.2f}\n")