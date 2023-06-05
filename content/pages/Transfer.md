---
tags:
- PP
date: 2023-06-05
title: Transfer
categories:
lastMod: 2023-06-05
---
Suppose that you want to switch (part of) your portfolio from Broker-A to Broker-B.  You have already made 4 transactions in the deposit account Broker-A (EUR): deposit, buy, dividend, and sell.
![image.png](/assets/image_1685995052473_0.png)
*Figure 1: Deposit Account of Broker-A*

The Securities account of Broker-A has the two accompanying transactions (buy and sell).
![image.png](/assets/image_1685994965849_0.png)
*Figure 2: Securities account of Broker-A

You want to transfer the transactions to the Securities and deposit account of Broker-B. These accounts should be present in the portfolio XML. We use the same portfolio XML;  so that we don't need  to transfer the Master securities also; e.g. the security Share-1 already exists in the portfolio XML.

The transfer is a two-step procedure. First, you need to export the transactions; both for the securities account and the deposit accounts. Then, you need to import them in a specific order.

With the menu File > Export, you can select the Broker-A (EUR) Account Transaction, which refers to the deposit account and the Broker-A Securities Account Transactions (refers to the >Securities account).
![image.png](/assets/image_1685995658742_0.png)



This export will give you two CSV-files (Broker-A.csv and Broker-A (EUR).CSV). The content resembles the transactions from figure 1 and 2.

Broker-A.CSV
Date,Type,Value,Transaction Currency,Gross Amount,Currency Gross Amount,Exchange Rate,Fees,Taxes,Shares,ISIN,WKN,Ticker Symbol,Security Name,Note
2020-01-02T00:00,Buy,5.00,EUR,,,,0.00,0.00,1,BE0974258874,,BEKB,share-1,
2022-01-02T00:00,Sell,-8.00,EUR,,,,0.00,0.00,1,BE0974258874,,BEKB,share-1,



Broker-A_(EUR).csv
Date,Type,Value,Transaction Currency,Taxes,Shares,ISIN,WKN,Ticker Symbol,Security Name,Note
2020-01-02T00:00,Buy,-5.00,EUR,,,BE0974258874,,BEKB,share-1,
2022-01-02T00:00,Sell,8.00,EUR,,,BE0974258874,,BEKB,share-1,
2020-01-02T00:00,Deposit,5.00,EUR,,,,,,,
2021-05-01T00:00,Dividend,2.00,EUR,0.00,1,BE0974258874,,BEKB,share-1,

It's better to first import the Securities transactions: File > Import. Select Account Transactions as Type of. The correct fields are matched and in the second step (see figure below), you can notice that both the buy and sell transaction is successfully imported. Don't forget also to select the Broker-B cash and Securities account in step 2. These account should be of course exist or created beforehand.
![image.png](/assets/image_1685996604929_0.png)

Note that this import will also create two transactions in the deposit account. Then you can import the Deposit transactions (broker-_(EUR).CSV. But only two of them (deposit and dividend) will be successful. The buy and sell transactions (in the deposit account) are already created by the previous step.
![image.png](/assets/image_1685997217773_0.png)

Please note the error messages for line 2 and 3 of the CSV-file, which are exactly the buy and sell transactions. The number of shares is indeed missing in this CSV-file; except for the dividend transaction.
