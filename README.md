Fantasy Football Picks
----------------------

This is a simple Python program to compare average draft position (ADP) between different years, by assigning a weighted value for each ranking associated with each year.  My theory is that players who have ranked highly over previous years are safer - less prone to injury, and more capable of producing consistent numbers over time.  The current year's ADP is ranked with a weight of 100, and previous years can be ranked lower--I have found that 25-65 produces interesting rankings, but I just adjust the numbers and then look at the results vs the current year's results to see if the results make sense to me.. I wrote this 2 years ago, but figured it might be useful to others.

How to get data:

* go to https://fantasyfootballcalculator.com/adp
* Choose Draft, and then PPR ADP, Half-PPR ADP, Non-PPR ADP, or 2-QB ADP from the left side.
* Go to Display -> JSON to download the data for that year.  Name it:
  <YEAR>-ppr.json
  <YEAR>-halfppr.json

* Update bin/picks.py to reflect information you know (i.e. this_year variable)
* run it to get the overall weighted rankings you've chosen, or grep out the position of your choice
