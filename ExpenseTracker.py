'''
ToDo:

1. Create MonthlyExpenseList class: which will initialise the expense list which is basically a dictionary with serial 
number as the key and list of expense, category and date(default date is of today)
2. different MonthlyExpenseList object are created for different months automatically to part different months
3. Where the class allow adding, removing expenses, or edit any expenses amount, date or category by serial number
4. initially get current date and create a dictionary which holds the expenselist object as value and month and year as the key

'''

#accessing the current date
from datetime import date

today = str(date.today()).split('-')
print(today)

currentMonth = today[1]
currentYear = today[0]
currentDay = today[2]

currentDate = f"{currentDay}.{currentMonth}.{currentYear}"
print(currentDate)

allExpenses = {} #store expense list month wise

#defining ExpenseList and its all methods 

class ExpenseList():
    '''
    Defines and handle all the methods of the Expense list
    '''

    def __init__(self):
        self.expenses = {}
        self.sno = 1

    def __add(self,amount:float, category:str, date:str = currentDate):
        

