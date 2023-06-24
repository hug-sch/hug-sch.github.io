---
title: Transaction types
date: 2023-05-30
lastMod: 2023-06-24
categories: ["PortfolioPerformance"]
math:
image:
description: Security and deposit transactions are the core of PP.
---
{{<columns>}}
A financial transaction is an agreement between a buyer and seller to exchange goods, services, or assets for payment. In case of PP, the exchange is about securities.

Transactions are the core of PP. You can divide them broadly into security and deposit transactions (see figure 1).

Security transactions are: buy, sell delivery (inbound), and delivery (outbound).

Deposit transactions are: deposit, removal, interest, interest charge, fees, fees refund, taxes, tax refund.

A dividend is a special transaction because it has both a security and deposit component.
{{<column>}}
{{< figure
  src = "/pp/assets/transaction-2023-06-23-10-27-29.png"
  caption = "Figure 1: All transactions"
  class = "img-fluid rounded float-end" 
>}}
{{<endcolumns>}}

Security transfer ... and Transfer between accounts ... are no real transactions but manual operations between accounts.

## Buy transaction
{{< figure
  src = "/pp/assets/transaction-20230525-134306_1685198802956_0_1685361637474_0.png"
  caption = "Figure 2: Buying a USD security through a EUR deposit account"
  class = "img-fluid rounded" 
>}}

The minimum info that you need for a buying or selling transaction is:

  - Security: you can choose the security from the drop-down. If a particular security was already selected before the start op the transaction, this info is already filled in. Please note that the currency is automatically set because each security has a currency associated with it.
  - Securities Account: choose with drop-down or already filled in, if you started from the Securities account.
  - Deposit Account: choose with drop-down or already filled in with the  [account]({{< ref "/pp/account" >}}) of the security. If the currency of the deposit account is different from the security currency, then the Gross Amount and eventually Fees and Taxes (in the Security currency) have to be converted. So, you also need an Exchange Rate.
  - Date of transaction: you can choose it from a calendar or enter it manually.
  - Number of securities (shares): this can be a decimal number.
  - Quote: the price of the security; always in the currency of the security.
  - Debit Note: this is the amount that you have to pay or receive as a result of this transaction. Other names are: Value or Net Value.
  - Optional fields are: the Gross Amount (shares * Quote); Fees and Taxes; both in the deposit currency and Security currency. The fees and taxes in the securities currency however are converted to the Deposit currency.
  - Depending on which value is entered as last value, some of the other fields are recalculated.

  - Entered as last value:
    - Debit Note: The Gross Amount in both currencies are recalculated. Because the Gross Amount in the security currency changes, also the Quote price will change (the amount of shares remains the same). The quote is automatically calculated; based upon Debit Note (Value) = Shares * Quote.

## Receiving a dividend

![import-20230526-112018.png](/pp/assets/import-20230526-112018_1685188046491_0.png)