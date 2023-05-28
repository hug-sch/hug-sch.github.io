---
tags:
- PP
title: Importing
categories:
date: 2023-05-27
lastMod: 2023-05-27
---
# Import a CSV-file

In PP you can enter your transactions (buy, sell, dividends, … ) manually. You can also *import* those transactions from a CSV file (comma-separated values) or from a PDF document. Not all brokers, however, provide the format that PP needs. So, how should this CSV-file look? Suppose, you want to import the following two transactions.

  + Buy a USD security with your EUR deposit account

  + Receive a USD dividend into the same EUR deposit account
buy transaction

![import-20230526-111942.png](/assets/import-20230526-111942_1685187761338_0.png)
Figure 1: Manual input of a buy-transaction (two different accounts)

![import-20230526-112018.png](/assets/import-20230526-112018_1685188046491_0.png)
Figure 2: Manual input of a dividend-transaction (two different accounts)

With the menu `File > Import > CSV files (comma-separated values)` you can import all kind of transactions . A CSV file is simply a text file. The first line contains the names of the fields (columns); separated with commas. The second and following lines contain the data, also separated by commas. For example, the following print-out of a CSV-file contains three fields or columns and two lines of data.

```
Name,Type,Date,Value
Share-1,dividend,2023-05-21,1500
Share-2,buy,2023-06-01, 20
```

PP distinguishes between 5 types of import: Account Transactions, Portfolio Transactions, Securities, Historical Quotes, and Securities Account (see figure 3). To correctly use a type and import the data into PP, the CSV file must contain specific fields. Depending on the type of account, there are other required and optional fields.

![import-20230526-200824.png](/assets/import-20230526-200824_1685189908735_0.png)
Figure 3: Import dialog window with the 5 types

The difference between each type is rather nebulous and not very good documented. The following definitions are tentative.

  + - Account Transactions: will be used to register transactions within one account; for example the payment of a dividend (?)

  + - Portfolio Transactions: for transactions between accounts. For example, the buying of a share involves adding shares to the Securities account and reducing the associated deposit account with money.

  + - Securities: you can use this type to create securities in the All Securities account without also adding a transactions. You need Securities Account type for that.

  + - Historical Quotes: to create a table of historical quotes for a security.

  + - Securities Account: with this type, you can create new securities within the All Securities account and at the same time a buy transaction in the All Transactions account.



1. ten eersts



-ten tweede





Each type has different required and optional fields. For example, the Historical Quotes type only needs the Date and the Quote. Instead of repeating the name of the share again and again for each historical quote in the CSV file, you can select the security in the next pop-up window. The Account Transactions type has two required Fields: Value and Date. The Portfolio Transactions has three required fields: Value, Date, and Shares (see figure 4).

![import-20230526-202852.png](/assets/import-20230526-202852_1685189893944_0.png)
Figure 4: Required and optional fields for the 5 types of import

Import buy/sell transaction

  + An easy way to discover what info/fields you need to import a buy transaction, is to export it first. After selecting the transaction in All Transactions, click the Export button at the top-right of the window (up-pointing arrow). Choose “Selected transactions (CSV)”. The result looks something like Table 1.

Table 1: CSV-file from export of transaction in figure 1
Date	Type	Security	Shares	Quote	Amount	Fees	Taxes	Net Transaction Value	Cash Account	Offset Account	Note	Source
2023-05-25	Buy	share-2	10	4.66	46.58	3.93	5.86	56.37	Broker-A	Broker-A (EUR)	My

  + If you should open this CSV-file with a text editor (e.g. Notepad), it will look something like this:

Date,Type,Security,Shares,Quote,Amount,Fees,Taxes,Net Transaction Value,Cash Account,Offset Account,Note,Source 2023-05-25,Buy,share-2,10,4.66,46.58,3.93,5.86,56.37,Broker-A,Broker-A (USD),My Note,

  + The first line contains the field names, separated by a comma. The second line contains the value of those fields. Notice that there is no value for the field Source. Unfortunately, the field names does not match with the required field names for the import. For example, the name Net Transaction Value should be simply Value and the name Security on the other hand should be Security Name. So, when you should import this file back into PP, you have to map those fields. However, even if you do that, the import will not succeed.

  + Import dividends

Suppose that your broker can provide you with a CSV-file with all the dividend payments from the past period. Of course, you would like to import this file in stead of entering manually all these dividend payments. The file content looks something like this (see figure 1 below).

![import-csv-file-content.png](/assets/import-csv-file-content_1685190460525_0.png)

    + Trying to import this file with the menu File > Import > CSV-files (comma-separated values ) or CTRL, I + C will show the following pop-up window (see figure 2).

    + From the three available columns of the CSV-file, two of them are recognized by PP: ISIN and Date. According to the pop-up message, there are two required fields: Date and Value, of which the last one is unmapped. This is because the name that your broker uses (Payment) is different from the required name (Value). You can however, double click on the Payment column to choose the correct field name.

    + There are only two required fields: Date and Value. But how, does PP know on which security this dividend should be paid? Which Cash account should be used? It doesn't!

    + After clicking Next, you could select the correct Cash Account and Securities Account. This assumes of course that all (dividend) transactions from the this CSV-file are to be done against these accounts. But worse, because there is no Type (of transaction) specified! The resulting transaction is a simple Deposit with the Amount from the CSV-file. Not a dividend!

    + When a Type is specified, one has also to specify the security. This could be done by Security Name, ISIN, WKN, or Ticker Symbol. If there are multiple securities with that name or ISIN, … an error is thrown. Two identical names with different ISIN will be no problem (ISIN has higher priority).

    + So, a few more fields should be entered in the CSV-file. Remember to use the correct (PP) names; otherwise you have to map each column (see figure 3).

![import-panel.png](/assets/import-panel_1685190543058_0.png)

      + 

    + Because you can only specify one Cash Account and one Securities Account in this second panel, both dividends will be registered against this Cash Account. For the USD-share with currency USD, this is not possible. So, it will be omitted (strike-through). You should also specify the Cash Account.

    + In order to get it correct, you need to add two fields: Cash Account and Transaction Currency. The second one is a bit redundant because PP could deduce the used currency from the Cash Account. Probably, it has to do with the following. You have a dividend, payable in a USD but your broker or yourself want to book it in a EUR cash deposit. Therefore, you need an offset account and an Exchange Rate; eventually a Currency Gross Amount.

    + The relationship between Value, Cash Account, Transaction Currency, Offset Account, … is rather nebulous. The dividend transaction of fig xx is created with the CSV of figure xx.

    + 

![import-csv-file-content-offset-account.png](/assets/import-csv-file-content-offset-account_1685190594012_0.png)

![import-csv-file-content-offset-account-result.png](/assets/import-csv-file-content-offset-account-result_1685190601160_0.png)

    + If Shares, Gross Amount and Value is specified, then the two transactions are performed of Type Dividend and Security. A new security is created in All Securities and the dividend is allocated to that new security? Why ???? Apparently, because I have two securities with the same name (forgotten to rename them).

    + Adding the field Value and shares, together with Gross Amount is redundant. The Gross Amount is not taken into account. When editing afterwards this transaction, the Gross Amount get the value of the Value field. –> so, is ignored. The Gross Amount is always calculated from Value + Fees + Taxes.

BUT, because Value is a required field, one cannot specify the Gross Amount or maybe you should also specify taxes and fees (they are not filled in but presumably seen as zero)

OK. When the necessary fields shares, Gross Amount, Fees, Taxes, Value are specified, PP will calculate the dividend payment per share correctly. If the numbers don't match up (value + fees + taxes <> Gross Amount) then the Gross Amount and the dividend payment per share are recalculated.

Manual transaction Manually, when a security is selected, the dividend will be done against this security and the correct number of shares is calculated, according to the specified date.
