---
title: IRR
tags:
categories:
date: 2023-05-30
lastMod: 2023-05-31
---
The Internal Rate of Return (IRR) of an investment made in the past (period 0) is the discount rate (interest rate) that the investment needs in order to generate the actual cash flows of period 1 - n.

PP calculates an ex-post (after the fact) IRR. The investment has been made and the actual cashflows are known. The IRR is the annual discount (interest) rate that will generate these actual cashflows; given the initial investment. It is an indication of the performance of the investment.

Given an interest rate, calculating the future value of a present investment is easy: FV = PV *(1+i)^n where i is the interest rate for the investment and n is the number of years.

![future-value.svg](/assets/future-value_1685557639639_0.svg)

The formula for the present value could be easily derived from this: PV = FV/(1+ i)^n

Because IRR is the annual discount (interest) rate that will generate these actual cashflows the following equation holds.
![image.png](/assets/image_1685524323158_0.png)
*Equation to derive the IRR*

There is no easy way to derive IRR from this equation. The Excel function IRR for example solves the problem by trying out different values for IRR (starting form the parameter Guess).

The previous equation also assumes that the periods are evenly spread in time and have a duration of exactly 1 year. If you want to specify the periods in days, you need a fraction of days from period 0 to period n/365. The result 1 means exactly 1 year later, 1.5 is one and a half year later, ... Excel uses for this the function XIRR.

Simplified example in PP: you bought a security two years ago for 5 EUR/share. Today you can sell it at 8 EUR/share. What is the IRR?
![image.png](/assets/image_1685476115692_0.png)
*Deposit of 5 EUR, followed by Buy of Share-1 for 5 EUR, followed by sell two years later for 8 EUR*

According to the Performance Dashboard, it is 26.45%. In Reports > Performance > Trades you find all necessary info.
![image.png](/assets/image_1685562551192_0.png) 
*Reports > Performance > Trades*

There are 731 days between the buy and sell transaction.  According to  the equation above:
5 EUR = 8 EUR/(1 + IRR)^(731/365)
Setting IRR = 26.45% will exactly balance the equation: 5 EUR = 8 EUR/1.2645^(731/365).

Suppose that a dividend of 2 EUR is paid on 2021-05-01. Now , there are two periods for the IRR calculation with 486 days and 731 days and the equation becomes:
5 EUR = 2 EUR/(1+IRR)^(486/731) + 8 EUR/(1+IRR)^(731/365).
As is evident from this formula, the IRR will be larger (you add a positive number to the previous equation). Deriving IRR from this equation takes some trial-and-error.  The exact solution is 47.97%. According to Excel, it should be 45.32%. Pluging this last value in equation seems to be correct.
