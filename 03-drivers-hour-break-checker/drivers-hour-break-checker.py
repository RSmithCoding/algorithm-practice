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


"""the real rule lets the 45 minutes be split into 15 then 30. With that rule, this day is legal. 
Change your code to handle it."""

driving_log2 = [("drive", 120), ("break", 15), ("drive", 150), ("break", 30), ("drive", 100)]

driving_count2 = 0
break_count = 0

driving_limit2 = ((4 * 60) + 30)

print(driving_limit2)


for record in driving_log2:
    if record[0] == "drive":
        print(record[0], record[1])
        driving_count2 = driving_count2 + record[1]
        print(driving_count2)
        if driving_count2 > driving_limit2:
            print(f"driving count 2: {driving_count2}")
            if break_count >= 45:
                print("Driver has gone over limit but had enough break therefore legal")
                break
            elif break_count < 45:
                print("Driver has gone over limit and not had enough break!")
                break
    elif record[0] == "break":
        print(record[0], record[1])
        break_count = break_count + record[1]
        print(break_count)
    