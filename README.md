How to get data:

* go to https://fantasyfootballcalculator.com/adp
* Choose Draft, and then PPR ADP, Half-PPR ADP, Non-PPR ADP, or 2-QB ADP from the left side.
* Go to Display -> JSON to download the data for that year.  Name it:
  <YEAR>-ppr.json
  <YEAR>-halfppr.json

* Update bin/picks.py to reflect information you know (i.e. this_year variable)
* run it to get the overall weighted rankings you've chosen, or grep out the position of your choice
