---
tags:
- PP
date: 2023-05-24
title: Importing
categories:
lastMod: 2023-05-30
---
# Importing a CSV-file

In PP you can enter your transactions (buy, sell, dividends, … ) manually. You can also *import* those transactions from a CSV file (comma-separated values) or from a PDF document. Not all brokers, however, provide the format that PP needs. So, how should this CSV-file look? Suppose, you want to import the following transaction.

![transaction-20230525-134306_1685198802956_0.png](/pp/assets/transaction-20230525-134306_1685198802956_0_1685361637474_0.png)


  + 

  + The following PP fields are  used: Security Name (share-2), the implied currency (USD), Securities Account (Broker-A), Deposit Account (Broker-A (EUR), Date & time, number of Shares (10), buying quote (5 USD), Gross Amount in USD (50), Exchange Rate (1.0785 EUR/USD), Gross Amount in EUR(46.36), Fees USD and EUR), Taxes (USD and EUR), Value or Debit Note (55.21), and a note (My Note).

  + You don't have to provide all fields in the CSV-file; some of them aren't even possible e.g. implied currency and fess /taxes in the foreign currency.



With the menu `File > Import > CSV files (comma-separated values)` you can import all kind of transactions . A CSV file is simply a text file. The first line contains the names of the fields (columns); separated with commas. The second and following lines contain the data, also separated by commas. For example, the following print-out of a CSV-file contains three fields or columns and two lines of data.

```
Name,Type,Date,Value
Share-1,dividend,2023-05-21,1500
Share-2,buy,2023-06-01, 20
```

PP distinguishes between 5 types of import: Account Transactions, Portfolio Transactions, Securities, Historical Quotes, and Securities Account (see figure 3). To correctly use a type and import the data into PP, the CSV file must contain specific fields. Depending on the type of account, there are other required and optional fields.

![import-20230526-200824.png](/pp/assets/import-20230526-200824_1685189908735_0.png)
*Import dialog window with the 5 types*

The difference between each type is rather nebulous and not very good documented. The following definitions are tentative.

  + Account Transactions: will be used to register transactions within one account; for example the payment of a dividend (?)

  + Portfolio Transactions: for transactions between accounts. For example, the buying of a share involves adding shares to the Securities account and reducing the associated deposit account with money.

  + Securities: you can use this type to create securities in the All Securities account without also adding a transaction.

  + Historical Quotes: to create a table of historical quotes for a security.

  + Securities Account: with this type, you can create new securities within the All Securities account and at the same time a buy transaction in the All Transactions account.

Each type has required and optional fields. For example, the Historical Quotes type only needs the Date and the Quote. Instead of repeating the name of the share again and again for each date, you can select the security in the next pop-up window. The Account Transactions type has two required Fields: Value and Date. The Portfolio Transactions has three required fields: Value, Date, and Shares (see figure 4).

![import-20230526-202852.png](/pp/assets/import-20230526-202852_1685189893944_0.png)
*Required and optional fields for the 5 types of import*

## Importing buy/sell transactions
  + An easy way to discover what info/fields you need to import a buy transaction, should be to export the transaction. After selecting the transaction in All Transactions, click the Export button at the top-right of the window (up-pointing arrow). Choose “Selected transactions (CSV)”. If you should open this CSV-file with a text editor, it will look something like this:
```
Date,Type,Security,Shares,Quote,Amount,Fees,Taxes,Net Transaction Value,Cash Account,Offset Account,Note,Source
2023-05-25 00:00:00,Buy,share-2,10,5.50,55.00,4.10,6.20,65.30,Broker-A,Broker-A (EUR),My Note,
``` 
The first line contains the field names, separated by a comma. The second line contains the value of those fields. Notice that there is no value for the field Source. *Unfortunately*, the field names do not match with the required field names for the import nor with the labels used in the dialog box (e.g. Name vs Security Name, Net Transaction Value vs Value). A new field is added (Type) but worse, a necessary field (Exchange Rate) is missing. Also, USD and EUR fees and taxes are added into a total amount in EUR.

  + This means that if you should try to import this transaction again (after deleting the original one); the import will fail.

  + In order to recreate the transaction of figure (Buying a USD security ...), you need at least the following fields. Restoring the split between USD and EUR fees and taxes seems to be impossible.

```
Date,Type,Security Name,Shares,Fees,Taxes,Value,Exchange Rate
2023-05-25 0:00,Buy,share-2,10,4.1,6.2,65.30,0.9091
```

    + Date, Security Name and Shares (see figure Required and optional fields).

    + Fees and taxes: both in the currency of the Cash (Deposit) account; e.g. EUR.

    + Value: this is the Net Transaction Value in EUR (from exported CSV above) or the Debit Note from figure Buying a USD share above.

    + Exchange Rate

    + Cash Account and Securities Account: optional because you can specify them in the next step of the Import Wizard. Of course, they become required and should be specified in the CSV-file, if they change between transactions (e.g. when you mix transactions in foreign and reference currency).

  + The following internal calculation is probably made:

    + The Gross Amount (in EUR) is calculated from the (net transaction) value, fees and taxes.

    + The Gross Amount in USD is calculated from the exchange rate and the gross amount in EUR.

    + The quote price is calculated from the number of shares and the gross amount in USD.

    + Import the following CSV-file.  The field "Quote" is not required because it will be calculated from the amount of shares and the Gross AmountPlease note that there is a field: Exchange Rate

    + Use the Portfolio Transactions type

  + ## Importing dividends

![import-20230526-112018.png](/pp/assets/import-20230526-112018_1685188046491_0.png)


Suppose that your broker can deliver a CSV-file with all the dividend payments from a past period. Of course, you would like to import this file in stead of entering manually all these dividend payments. The file content looks something like this (see figure 1 below).

![import-csv-file-content.png](/pp/assets/import-csv-file-content_1685190460525_0.png)
*CSV-file from broker about dividends paid*

    + BE0974258874

    + US5949181045

    + Unfortunately, this is not enough information to use the Import CSV-function. First, from the three available columns of the CSV-file, two of them are recognized by PP: ISIN and Date. For the column Payment, you have to map this field to one of the PP fields. Because, it is a dividend you need to use the import type Account transactions. A dividend payment is a simple deposit transaction, which has no implications on the securities account.

    + According to the pop-up message, there are two required fields: Date and Value, of which the last one is unmapped. This is because the name that your broker uses (Payment) is different from the required name (Value). You can however, double click on the Payment column to choose the correct field name.

![import-panel.png](/pp/assets/import-panel_1685190543058_0.png)
*Importing dividends from a CSV-file*

    + But how can PP recreate a dividend payment with only these two fields (date, value). It can't! You can only use this import to create a deposit in a Security and Cash account. If you want to create a dividend, you should also specify a type: Dividend. Or, specifying a number of shares or fees/taxes will also do the job.

    + Of course, PP does also need the name of the Cash and Securities account. You can enter this in the next step of the wizard or you can specify it in the CSV-file.

    + Let's take a simplified example (EUR-dividend in a EUR-cash account. The minimal info to register this dividend is:

```
type, Date, ISIN, Value
dividend, 2022-01-01, BE0974258874, 40
```

    + This will result in the following "dividend" transaction.

![image.png](/pp/assets/image_1685381641370_0.png)
*Dividend transaction with minimal info specified*

    + Adding Fees and Taxes will calculate the Gross Amount. You cannot specify the Gross Amount in itself. Adding the number of Shares will calculate the dividend payment/share. It is also not possible to specify this in itself. So, a typical CSV-file for a dividend payment in the currency of the Cash account will look like:
```
Type, Date, ISIN, Value, fees, taxes, shares
dividend, 2022-01-01, BE0974258874, 200, 3, 2, 25
```
The Gross Value (205 EUR) and dividend payment/share (8.2 EUR) will be calculated.

    + It becomes much more complicated if the cash account (e.g. EUR) is different from the share currency (e.g. USD). Of course, you need a Exchange Rate.

    + If Shares, Gross Amount and Value is specified, then the two transactions are performed of Type Dividend and Security. A new security is created in All Securities and the dividend is allocated to that new security? Why ???? Apparently, because I have two securities with the same name (forgotten to rename them).

    + Adding the field Value and shares, together with Gross Amount is redundant. The Gross Amount is not taken into account. When editing afterwards this transaction, the Gross Amount get the value of the Value field. –> so, is ignored. The Gross Amount is always calculated from Value + Fees + Taxes.

BUT, because Value is a required field, one cannot specify the Gross Amount or maybe you should also specify taxes and fees (they are not filled in but presumably seen as zero)

OK. When the necessary fields shares, Gross Amount, Fees, Taxes, Value are specified, PP will calculate the dividend payment per share correctly. If the numbers don't match up (value + fees + taxes <> Gross Amount) then the Gross Amount and the dividend payment per share are recalculated.


