# Algorithm Practice

Beginner algorithm problems based on real-world situations from my own background in flooring, transport and the gym. Each problem has its own folder with my solution and a short write-up of how I approached it.

## Problems

| # | Problem | The task | What it practises | Status |
|---|---|---|---|---|
| 1 | [Fuel economy log](01-fuel-economy) | Work out a van's MPG for each fill-up, the best and worst, and the overall average | Loops, functions, why an overall average isn't the average of averages | Done |
| 2 | [Change from the till](02-change-from-the-till) | Give change using the fewest notes and coins | The greedy approach | Done |
| 3 | [Drivers' hours break checker](03-drivers-hour-break-checker) | Check a driver's day against the 4.5-hour driving limit and the 45-minute break rule | Running totals, conditions | Done |
| 4 | [Vehicle inspections due](04-vehicle-inspections-due) | List a fleet's overdue inspections and those due in the next 7 days, soonest first | `datetime`, `timedelta`, sorting | Done |
| 5 | [Personal best tracker](05-personal-best-tracker) | Find each exercise's heaviest lift and best estimated one-rep max | Dictionaries, the Epley formula | Done |
| 6 | [Find an order fast](06-find-an-order-fast) | Search 10,000 sorted order numbers, comparing linear and binary search | Binary search | Done |
| 7 | Carpet roll cutting | Fit carpet cuts into as few 25 m rolls as possible | Bin packing, "first fit decreasing" | To do |
| 8 | Delivery route | Plan a delivery route by always going to the nearest drop next | Nearest neighbour, `math.dist` | To do |

## How I approach each problem

1. Work out the example answer by hand.
2. Write the steps in plain English as comments.
3. Turn each comment into code, testing as I go.
4. Check the result against the expected answer.

I commit as each part starts working, so the commit history shows how each solution was built up.

## Running them

You need Python 3. No extra packages are required. From the top folder, run any problem with:

```
python3 01-fuel-economy/fuel-economy.py
```