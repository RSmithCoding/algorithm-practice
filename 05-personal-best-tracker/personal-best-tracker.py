"""Given logged sets as (date, exercise, weight, reps), find each exercise’s heaviest lift and its 
best estimated one-rep max using the Epley formula: weight × (1 + reps / 30)."""

from datetime import datetime

sets = {
    "Bench Press": "11/11/26" "weight" "reps",
    "Dumbell Press": "11/11/26" "weight" "reps",
    "Shoulder Press Bar": "11/11/26" "weight" "reps",
    "Shoulder Dumbell Press": "11/11/26" "weight" "reps",
    "Squats": "11/11/26" "weight" "reps",
    "Bicep Curls": "11/11/26" "weight" "reps",
    "Leg Extensions": "11/11/26" "weight" "reps",
    "Tricep Extensions": "11/11/26" "weight" "reps",
    "Leg Press": "11/11/26" "weight" "reps",
    "Upright Rows": "11/11/26" "weight" "reps",
    "Cable Rows": "11/11/26" "weight" "reps",
}

print(sets)