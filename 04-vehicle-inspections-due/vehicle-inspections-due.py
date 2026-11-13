"""Each vehicle in a fleet has a registration and a last-inspection date, and is inspected every 6 weeks. 
List the vehicles due in the next 7 days, soonest first, and any that are overdue."""

from datetime import datetime, timedelta

today = datetime.now()
plus_days = today + timedelta(days=7)

print(today)

print(f"{today.day}/{today.month}/{today.year}")



print(plus_days)

vehicle_last_insp = {
    "Reg": "1/11/26",
    "Reg2": "15/10/26",
    "Reg3": "5/10/26",
    "Reg4": "8/10/26",
    "Reg5": "30/09/26",
    "Reg6": "20/08/26",
    "Reg7": "18/10/26",
    "Reg8": "17/09/26",
}

def add_time_weeks(date):
    temp_date = datetime.strptime(date, "%d/%m/%y")
    return_date = temp_date + timedelta(weeks=6)
    return return_date

print("Last Insp Dates:\n")

for key in vehicle_last_insp:
    print(key, vehicle_last_insp[key])

print("\nNext insp dates:\n")

for key in vehicle_last_insp:
    new_date = add_time_weeks(vehicle_last_insp[key])
    print(key, new_date.strftime("%d/%m/%y"))