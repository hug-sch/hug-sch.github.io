---
title: IRR
tags:
categories:
date: 2023-05-30
lastMod: 2023-06-02
---
The Internal Rate of Return (IRR) of an investment is the annual interest rate for the investment in order to generate the actual cash flows later on.

PP calculates an ex-post (after the fact) IRR. The investment has been made and the actual cashflows are known.

The calculation of IRR is related to the calculation of the future or present value of an investment.

![present-future-value.png](/assets/present-future-value_1685730050469_0.png)

Because IRR is the annual interest rate that should generate these actual future cashflows the following equation holds.
![image.png](/assets/image_1685524323158_0.png)
*Equation (1)*

There is no easy way to derive IRR from this equation. The Excel function IRR for example solves the problem by trying out different values for IRR (starting form the parameter Guess).

Equation (1) also assumes that the periods are evenly spread in time and have a duration of exactly 1 year. If you want to specify the periods in days, you need a fraction: days from period 0 to period n/365. The result 1 means exactly 1 year later, 1.5 is one and a half year later, ... The extended or XIRR function can be used in Excel for this calculation.

PP calculates several variants of the IRR  key indicator. You can find them at:

  + Reports > Performance

  + Reports > Performance > Securities

  + Reports > Performance > Trades

Summary

  + Reports > Performance: the IRR is calculated for the whole project (all securities and all deposit accounts) and for the complete reporting period. If dividends are parked on a deposit account, they will contribute to the final result of the period. Only three numbers are important: initial value of portfolio, end value of portfolio and numbers of days between begin and end of reporting period. 

  + Reports > Performance > Securities: the IRR is calculated per security from the start of the reporting period until the end. If the buy or sell transactions lay before the reporting period the corresponding historical quote is taken to determine the value.  All transactions in the reporting period, including dividends, are evaluated at the transaction date (not the end date of the period).

  + Reports > Performance > Trades calculates the IRR per share without dividends or other income; from the first transaction (usually buy) until the last transaction (sell) or today. There is no reporting period.

## Buy and sell

Let's take a look at a simplified example: you bought a security two years ago for 5 EUR/share. Today you can sell it at 8 EUR/share. What is the IRR?
![image.png](/assets/image_1685721535723_0.png)
*Deposit of 5 EUR, followed by buy (share-1) for 5 EUR, followed by sell two years later for 8 EUR*

If you should redo this example in PP, then the [reporting period](period) is important. By default, it is set to 1 year; so may be the transactions aren't even in the reporting period. Let's assume that the reporting period is set to  "From 2020-01-01 until 2022-01-02".  Remember that the period runs from the end of the start date until the end of the finish date.

The different IRR metrics are:

  + Reports > Performance: 26.45%

  + Reports > Performance > Securities: 26.45%

  + Reports > Performance > Trades: 26.45%

  + Excel XIRR: 26.45%

Because the reporting period and the actual buy/sell dates convey, the IRR metric should also be the same. In order to make 8 EUR from 5 EUR in 731 days (2020 is a leap year), the interest rate (IRR) should be 26.45%.

From the equation (1):
5 EUR = 8 EUR/(1 + 0.2645)^(731/365)

## Dividends

Let's make the example a little more complex. A dividend of 2 EUR is paid on 2021-05-01.

  + Reports > Performance: 41.35%

  + Reports > Performance > Securities: 45.34%

  + Reports > Performance > Trades: 26.45%

  + Excel XIRR: 45.32%

The Trade IRR remains the same as in the buy/sell scenario. Dividends are not accounted for in this metric. Only the buy and sell transactions are used in the equation. It's the IRR of a trade.

The Securities IRR is the same as the Excel XIRR and fits with Equation (1). In the Securities view there is a column with sum of dividends. So, it seems logical that the dividends are considered as a cash inflow. In Equation (1) you need two periods: the dividend at 486 days and the sell transaction at 731 days. The equation becomes:
5 EUR = 2 EUR/(1+IRR)^(486/365) + 8 EUR/(1+IRR)^(731/365).
Deriving IRR from this equation takes some trial-and-error.  The exact solution is 45.34%.

The Performance IRR is calculated for the portfolio as a whole. So, there is only 1 period (from 2020-01-01 until 2022-01-02). The calculation takes the value of the complete portfolio at the beginning of the reporting period (= 5 EUR). This is the first cashflow, and again at the end date (=10 EUR) for the second and last cash flow. So, the portfolio increases from 5 EUR to 10 EUR in about 731 days. The interest rate to accomplish that is 41.35% annually. Why is the Performance IRR smaller than the Securities IRR? In the latter case, the dividend of 2 EUR is brought to PV from 2021-05-01 (the date of the payment) and for the Performance IRR, the 2 EUR is included in the final portfolio value of 10 EUR and is brought to PV from 2022-01-01. So, the dividend of 2 EUR will contribute more to the IRR in the Security IRR.
