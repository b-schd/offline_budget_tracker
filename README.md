# Offline Budget Tracker

The "transactions.xlsx" worksheet is a simple, offline interface for tracking expenses with responsive monthly goal adjustment. 

For years I used online budget trackers. However I found the advertisements to be a nuisance and was increasingly uncomfortable with giving financial transaction information to third parties. This transactions sheet is a breeze to set up, and exhibits all the functionality and flexibility that I ever wanted or needed in budget tracking without unnecessary bells and whistles.

## How To Use
The workbook is organized into 13 sheets-- the master budget worksheet followed by transaction sheets for each of the 12 months. The master sheet will be used to set up your budget, track your categorical spending for the year at a glance, and to view adjusted budget category limits based on spending. 

### Budget Set-Up
1. On the master worksheet, find the "Budget Setup" section. Here you can enter your monthly income, amount of tax withholding, and savings goal. The spreadsheet will automatically calculate how much you have left to budget with. 
<img src="https://github.com/b-schd/offline_budget_tracker/blob/master/figures/budget_planner.png" width="300">

2. Next, find the budget column in the main panel for budget tracking. Enter budget limits for your fixed and variable expense categories, and note that the savings field should be automatically populated based on your savings goal. Your budget will be completely balanced once you have allocated the full spending amount into the expense categories. The "Net Balance" and "Left to Budget With" fields should be zero. 

<img src="https://github.com/b-schd/offline_budget_tracker/blob/master/figures/budget_view.png" width="300">

### Adding Transaction Data
1. Download transaction data each month from your online financial accounts. Yes, I know this is inconvenient, but it is a small price to pay for having complete control over your data. 
2. Add your transactions to the spreadsheet for a given month. Note that the values in the debit and credit columns are both _positive_. 
3. Type the category names for each transaction. This usually goes pretty quickly, especially once autocomplete kicks in for the category names. The category color should automatically match the category color on the master sheet, and the net spending amount for a given category will also automatically appear on the master sheet. 

<img src="https://github.com/b-schd/offline_budget_tracker/blob/master/figures/Month_view.png">

### Track Goals
Once you have at least a month of transaction history, you can track whether you are meeting your budget goals. Use this information to guide your spending habits or to adjust your budget limits. 

In the "Track your budget goals" panel, click on the yellow box to select a budget category for viewing. The table will automatically update with the monthly spending on that category, and the chart will display spending along with the budget line for each month. The budget line will change based on your current spending, and represents the new monthly budget limit that you would need to meet in order to stay balanced for the year.

In our example below, the original budget was set to $200/month for groceries, which comes out to $2,400/year. But because $250 was spent on groceries in the first month, the budget is now set to $195.45/month so that total yearly spending is still $2,400. If we had spent only $150 on groceries, we would see a new budget level of $204.55/month since the money we didn’t spend would be rolled over and distributed among the remaining months. 

<img src="https://github.com/b-schd/offline_budget_tracker/blob/master/figures/track_goals.png">

## Authors

* **Brittany Scheid**

## License

This project is free for public use. 

## Questions? Comments?

Feel free to contact me with any suggestions or questions, I hope you find this to be helpful and easy to use!


