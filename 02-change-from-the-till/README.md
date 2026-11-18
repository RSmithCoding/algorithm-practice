# 2. Change from the till

## The problem

Given a price and the amount paid, give the change using the fewest notes and coins (£20, £10, £5, £2, £1, 50p, 20p, 10p, 5p, 2p, 1p).

## My approach

1. Convert the price and amount paid into pence, so all the maths uses whole numbers.
2. Go through the notes and coins from biggest to smallest.
3. For each one, keep taking it while it still fits into the balance, then move on to the next smaller one.
4. Print each note and coin, then the total change.

This is a **greedy algorithm**: at every step it takes the biggest note or coin that fits. With UK currency, that always gives the fewest notes and coins.

## Output

Price £13.47, paid £20:

```
Here is your change..

£5.00
£1.00
50p
2p
1p

Total Change: £6.53p
```

## What I learned

- **Each coin may be needed more than once.** My first version used a `for` loop that took each note or coin at most once. It worked for £6.53, but for £4 it gave £2, £1, 50p, 20p, 10p, 5p, 2p and 1p, which only adds up to £3.88. The fix was a `while` loop inside the `for` loop, so it keeps taking the same coin until it no longer fits.
- **Test more than the example.** The original example happened to never need two of the same coin, so the bug only showed up when I tried other prices.
- **Floats can't be trusted for money.** `int(0.29 * 100)` gives 28, not 29, because 0.29 is stored as 0.28999… Using `round()` when converting to pence fixes this.

## Running it

```
python3 change-from-the-till.py
```

Change `price` and `paid` at the top of the file to try other amounts.