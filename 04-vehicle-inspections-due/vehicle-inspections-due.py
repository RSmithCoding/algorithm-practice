"""Each vehicle in a fleet has a registration and a last-inspection date, and is inspected every 6 weeks. 
List the vehicles due in the next 7 days, soonest first, and any that are overdue."""

from datetime import datetime, timedelta

today = datetime.now()
plus_days = today + timedelta(days=7)

insp_overdue = {}
insp_next_seven_days = {}
insp_due_seven_days = []

vehicle_last_insp = {
    "Reg": "1/11/26",
    "Reg2": "17/10/26",
    "Reg3": "11/10/26",
    "Reg4": "10/10/26",
    "Reg5": "30/09/26",
    "Reg6": "20/08/26",
    "Reg7": "8/10/26",
    "Reg8": "6/10/26",
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

    if new_date < today:
        #INSPECTION OVER DUE
        insp_overdue.update({key: new_date})
        
    elif new_date >= today and new_date <= plus_days:    
        #INSP IN NEXT 7 DAYS
        insp_due_seven_days.append([key, new_date])
    
insp_due_seven_days.sort(key=lambda item:item[1])

print("\nThe following Inspections are OVERDUE:\n")
for key in insp_overdue:
    print(key, insp_overdue[key].strftime("%d/%m/%y"))
print("\nThe following Inspections are due in the NEXT 7 DAYS:\n")
for i in insp_due_seven_days:
    print(i[0],i[1].strftime("%d/%m/%y"))