---
tags:
- PP
title: Transaction
categories:
date: 2023-05-27
lastMod: 2023-05-27
---
# Transaction

## Buying or selling securities

![transaction-20230525-134306.png](/assets/transaction-20230525-134306_1685198802956_0.png)

The minimum info that you need for a buying or selling transaction is:

  + Security: you can choose the security from the drop-down. If a particular security was already selected before the start op the transaction, this info is already filled in. Please note that the currency is automatically set because each security has a currency associated with it.

  + Securities Account: choose with drop-down or already filled in, if you started from the Securities account.

  + Deposit Account: choose with drop-down or already filled in with the  [account]({{< ref "/pages/account" >}}) of the security. If the currency of the deposit account is different from the security currency, then the Gross Amount and eventually Fees and Taxes (in the Security currency) have to be converted. So, you also need an Exchange Rate.

  + Date of transaction: you can choose it from a calendar or enter it manually.

  + Number of securities (shares): this can be a decimal number.

  + Quote: the price of the security; always in the currency of the security.

  + Debit Note: this is the amount that you have to pay or receive as a result of this transaction. Other names are: Value or Net Value.

Optional fields are: the Gross Amount (shares * Quote); Fees and Taxes; both in the deposit currency and Security currency. The fees and taxes in the securities currency however are converted to the Deposit currency.

Depending on which value is entered as last value, some of the other fields are recalculated.

Entered as last value:

  + Debit Note: The Gross Amount in both currencies are recalculated. Because the Gross Amount in the security currency changes, also the Quote price will change (the amount of shares remains the same). The quote is automatically calculated; based upon Debit Note (Value) = Shares * Quote.
