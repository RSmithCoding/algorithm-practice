"""Given a price and the amount paid, give the change using the fewest notes and coins 
(£20, £10, £5, £2, £1, 50p, 20p, 10p, 5p, 2p, 1p)."""

price = float(13.47)

paid = float(20.00)

change_available = (2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1)

price_in_pence = round(price * 100)

paid_in_pence = round(paid * 100)

balance = paid_in_pence - price_in_pence

change_given = []




for change in change_available:
    while True:
        if balance - change >= 0:
            change_given.append(change)
            balance = balance - change
        elif balance - change < 0:
            break
        elif balance == 0:
            break
        


print("Here is your change..\n")

for change in change_given:
    if change >= 100:
        print(f"£{change / 100:.2f}")
        continue
    elif change < 100:
        print(f"{change}p")
        continue

print(f"\nTotal Change: £{(float(paid_in_pence - price_in_pence) / 100):.2f}p")
