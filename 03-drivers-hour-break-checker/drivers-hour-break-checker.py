"""A driver’s day is a list of stints, e.g. ("drive", 120) or ("break", 15) in minutes. 
The simple rule is: after 4 hours 30 minutes of driving, there must be a break of at least 45 minutes. 
Flag the stint where the rule is broken."""

driving_log = [("drive", 120), ("break", 15), ("drive", 150), ("break", 30), ("drive", 100)]

driving_count = 0

driving_limit = ((4 * 60) + 30)

print(driving_limit)

print(driving_log)

for record in driving_log:
    if record[0] == "drive":
        print(record[0],record[1])
        driving_count = driving_count + record[1]
        if driving_count > driving_limit:
            print("Driver has went over drive limit at:")
            print(record[0], record[1])
            