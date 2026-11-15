"""Given logged sets as (date, exercise, weight, reps), find each exercise’s heaviest lift and its 
best estimated one-rep max using the Epley formula: weight × (1 + reps / 30)."""

from datetime import datetime

sets = {
    "Bench Press": [("8/11/26", "50", "10"),("12/11/26", "60", 10),("15/11/26", "70", "8")],
    "Dumbell Press": [("8/11/26", "28", "10"),("12/11/26", "30", "10"),("15/11/26", "35", "10")],
    "Shoulder Press Bar": [("8/11/26", "45", "10"),("12/11/26", "50", "10"),("15/11/26", "60", "8")],
    "Shoulder Dumbell Press": [("8/11/26", "30", "10"),("12/11/26", "32", "10"),("15/11/26", "35", "10")],
   
}

for exercise, session in sets.items():
    heaviest = max(session, key=lambda x: x[1])
    print(f"Heaviest lift for {exercise} was {heaviest[1]}kg")
    maxlift = (int(heaviest[1]) * (1 + (int(heaviest[2]) / 30)))
    print(f"The estimated max lift for {exercise} is {maxlift:.0f}kg\n")
