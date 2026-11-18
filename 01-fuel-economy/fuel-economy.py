"""1. Fuel economy log
A van’s fill-ups are stored as (miles driven, litres put in). Work out the MPG for each fill-up, 
the best and worst, and the overall average. UK MPG uses 4.546 litres per gallon."""

testdata = [(412, 45.2), (380, 44.0), (455, 47.5)]

def getmpg(miles, litres):
    gallons = litres / 4.546
    mpg = miles / gallons
    return mpg, gallons

x = 1
mpg_list = []
total_miles = []
total_gallons = []

for van in testdata:
    mpg, gallons = getmpg(van[0],van[1])
    print(f"Fill up {x} shows {mpg:.2f} mpg")
    x = x + 1
    mpg_list.append(mpg)
    total_miles.append(van[0])
    total_gallons.append(gallons)

average = sum(total_miles) / sum(total_gallons)

print("")
print(f"The average mpg for the fill ups is {average:.1f}\n")

print(f"The highest mpg recorded was {max(mpg_list):.2f}\n")

print(f"The lowest mpg recorded was {min(mpg_list):.2f}\n")