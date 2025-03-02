# bet-calculator
A simple python file that runs a telegram bot to calculate what size to use on each bet to ensure equal profit when arbitrage betting on sportsbooks.

The derivation of the formula used in the function to calulate bet size:

`cost = (bet size 1) + (bet size 2)`

`return 1 = (bet size 1)(odds 1) + (bet size 1)`

`return 2 = (bet size 2)(odds 2) + (bet size 2)`

`return 1 - cost = return 2 - cost`

`(bet size 1)(odds 1) - (bet size 2) = (bet size 2)(odds 2) - (bet size 1)`

`(bet size 1)(odds 1) + (bet size 1) = (bet size 2)(odds 2) + (bet size 2)`

`(bet size 1) = ((bet size 2)((odds 2) + 1))/((odds 1) + 1)`

The link for a google sheets file with my active trades: 

https://docs.google.com/spreadsheets/d/1izNBUCKYip4jji0GxSw4d_Eou8-vZwW6PS4_BL9l2J8/edit?usp=sharing
