---
title: account
tags:
categories:
date: 2023-05-30
lastMod: 2023-05-30
---
# Account

An account is a collection of [transactions](http://localhost:8800/doku.php?id=pp:transaction): buy and sell transactions of securities (shares, …) for a Securities account; withdrawal and deposit transactions of money for a Deposit account. Each account has a default [currency]()attached. As part of the installation procedure, you should already have created at least one Securities account and one Deposit account.

PP has two main type accounts: Securities and Deposit accounts. They are rather well described in the [Guide on getting started]([https://forum.portfolio-performance.info/t/guide-on-getting-started/5390#accounts-6]) of Thomas (Contributor). Unfortunately, the internal bookmark to the Accounts section doesn't work; you have to scroll quite a bit down.

Other related types are “Investment Plans”, “All Transactions”, “Reference account” and “Offset account”. Sometimes a Deposit Account is called a Cash Account.

Deposit account

![account-types-deposit.png](/pp/assets/account-types-deposit_1685198463475_0.png)

In Figure above, there are two deposit accounts; named EUR and USD (in column Cash Account). They will be used for deposits and withdrawals in EUR or USD. It's a bit redundant to call them “EUR” and “USD” because you also have to specify the currency that the account will use (see third column in figure). Then, for example, when you want to book a dividend in EUR, you will get the following dialog. The cash account can can be selected from a drop-down and the correct currency is automatically added.

![account-dividend-booking.png](/pp/assets/account-dividend-booking_1685198677334_0.png)

According to your needs, you can use other names. For example, if you want to collect all of your dividends or taxes in a separate account, you could name them “Dividends” and “Taxes” in stead of EUR and USD. Of course, you also have to decide which currency that will be used for them. And, if you receive dividends in EUR and USD then you need two deposit account with the name “Dividends” but with different currencies.

  + 

Another possibility is to call the deposit accounts with the name of the bank or broker they belong to; e.g. BNPPF, Deutsche Bank, …

A deposit account is used to transfer or receive money as the result of a transaction. In figure [1](http://localhost:8800/doku.php?id=pp:account&do=edit#deposit-account), 4 buy/sell transactions result in a negative balance (-2210 EUR). Good practice however required probably that you first did a deposit of a large enough sum to cover the subsequent buy transactions; just as you should do with a real broker.

## Securities account

A security account will hold your securities and will be used if you buy or sell securities. A security account is most of the time named after the broker or bank that you use to buy or sell.

![account-20230524-110805.png](/pp/assets/account-20230524-110805_1685198579909_0.png)

## Reference account

A security account always has always a deposit account associated. This is the deposit account that will used (if no other is assigned) for any buy or sell transaction on that securities account. This deposit account is called Reference Account. In figure security-account, the Broker-A security has a reference account Broker-A (EUR) while the Broker-B security account has a USD-deposit account (Broker-B (USD). Probably, you use Broker A mostly for your EUR transactions and Broker B for the USD transactions.

## Offset account
