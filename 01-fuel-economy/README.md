# 1. Fuel economy log

## The problem

A van's fill-ups are stored as (miles driven, litres put in). Work out the MPG for each fill-up, the best and worst, and the overall average. UK MPG uses 4.546 litres per gallon.

## My approach

1. A function, `getmpg()`, converts litres to gallons and works out the MPG for one fill-up.
2. A `for` loop runs each fill-up through the function, printing its MPG and building three lists: the MPGs, the miles and the gallons.
3. `max()` and `min()` on the MPG list give the best and worst fill-ups.
4. The overall average is total miles divided by total gallons.

## Output

```
Fill up 1 shows 41.44 mpg
Fill up 2 shows 39.26 mpg
Fill up 3 shows 43.55 mpg

The average mpg for the fill ups is 41.5

The highest mpg recorded was 43.55

The lowest mpg recorded was 39.26
```

## What I learned

My first version added up the three MPGs and divided by 3, which gave 41.4 instead of 41.5. The gap looks small, but the method is wrong: averaging the MPGs treats every fill-up as equally important, however far the van went on it. The real figure is total miles ÷ total gallons, which weights each fill-up by the fuel it used. With very different fill-ups the difference is big. A 50-mile run on 10 litres and a 500-mile run on 50 litres average out at 34.1 MPG, but the van actually did 41.7 MPG over those 550 miles. This is how fleet fuel reports work it out too.

## Running it

```
python3 fuel-economy.py
```