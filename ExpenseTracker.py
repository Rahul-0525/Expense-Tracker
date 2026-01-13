'''
ToDo:


2. different MonthlyExpenseList object are created for different months automatically to part different months
3. Where the class allow adding, removing expenses, or edit any expenses amount, date or category by serial number
4. initially get current date and create a dictionary which holds the expenselist object as value and month and year as the key

changes: expenselist now will recieve a dictionary which will be a single month data and will have a method to return it which a function
named save will receive add it in the universal dictionary which is dictionary of dictionaries of month and update it 
and dump it and when this universal dictionary is loaded the dictionary of required month is created or taken from it and 
created into a expenselist object there exists only one object at a time action happen on it and then it get replaced by other 
expense list of another month
'''

#accessing the current date
from datetime import date
import datetime
import time
import json
# today = str(date.today()).split('-')
# print(today)
currentMonth = date.today().strftime('%m')
currentYear = date.today().strftime('%Y')
currentDay = date.today().strftime('%d')
currentDate = date.today().strftime('%d.%m.%Y')
# print(currentDate)




#definig specific exceptions for the system

class NegativeSpend(Exception):
    """Error shown when expense or spend input is negative"""
    def __init__(self,amt):
        super().__init__(f"Negative spending is not possible:{amt} Enter a valid input.")

#defining ExpenseList and its all methods 

class ExpenseList():
    '''
    Defines and handle all the methods of the Expense list which represent expenses of a single month only
    '''

    def __init__(self,monthlist:dict):
        self._expenses = monthlist
        try:
            self.sno = max(list(map(int,monthlist.keys())))+1
        except ValueError:
            self.sno = 1
        

    def add(self,amount:float, category:str, date:str = currentDate):
        """Adds the details of expense in the expense list taking amt, cat and date as argument"""
        self._expenses[self.sno] = [amount, category,date]
        self.sno +=1
        print('\nExpense Added')
    
    def remove(self,serialNo:int):
        """Removes any of the expense with serial number as argument"""
        try:
            self._expenses.pop(str(serialNo))
            print('\nData removed')
        except KeyError:
            print('Enter a valid input. Try again')
    
    def replace(self,serialNo:int,amt:float, category:str, date:str = currentDate):
        """takes the serial number and the new data and replace the data entry of that serial number"""
        self._expenses[serialNo] = [amt, category,date]
        print('\nData Edited')

    def display(self):
        """Display all the _expenses in pretty manner"""
        if self._expenses:
            print()
            for sno in self._expenses:
                print(f"{sno}".center(4," "),f"{self._expenses[sno][0]}".center(16,' '),
                      f"{self._expenses[sno][2]}".center(16,' '),
                      f"{self._expenses[sno][1]}".center(16,' '),sep="")
            print(allExpenses)
            print()

        else:
                print('\nNo Data\n')

    def getLastsno(self) -> int:
        return self.sno
    
    def getMonthlydata(self):
        return self._expenses




#Below is the userinterface for all the operations of  the expense list


print('--- Expense Tracker: One stop solution to track and manage all your expeneses all in one place ;) ---')
print()

#defining the function that handle the loading and saving of the allExpenses dictionary that stor all the month wise data


def save():
        
    with open('data.json','w') as file:
        json.dump(allExpenses,file,indent=4)
        print("--- File Saved ---")

def load():
    try:
        with open('data.json','r') as file:
            return json.load(file)
    except Exception:
        return {}



allExpenses = load()#this is the dictionary with month+year as key and the expenses as the value that is all the data and dict dict

DontExit = True
while DontExit:
    currentMonthKey = (currentMonth+currentYear)
    if currentMonthKey not in allExpenses:
        allExpenses[currentMonthKey] = {}
    currentDict  = allExpenses[currentMonthKey] #this access the current month data from the allExpenses
    currentExpenseList = ExpenseList(currentDict) #and this create object of that dictionary
    (currentExpenseList.display())

    print("--- What you wanna do? ---\n")
    print('1. Add New Expense data')
    print('2. Remove any Expense data')
    print('3. Edit any Expense data')
    print('4. Display your all Expense data')
    print('5. Exit')
    print()

    userinp = input('Enter (1/2/3/4/5): ')
    print()
    match userinp:
        case '1':
            NotDone = True
            while NotDone:
                try:
                    amt = float(input("Enter the amount of the Expense: "))
                    if amt<0:
                        raise NegativeSpend(amt)
                    NotDone = False
                except ValueError:
                    print('Enter a valid input. Try again')
                except NegativeSpend as err:
                    print(err)

            NotDone = True
            while NotDone:
                categories = [
                                "Housing",
                                "Utilities",
                                "Food & Dining",
                                "Transport",
                                "Health",
                                "Entertainment",
                                "Shopping",
                                "Debt & Loans",
                                "Education",
                                "Gifts & Donations",
                                "Insurance",
                                "Miscellaneous"
                            ]
                print('\n--- Choose the Category of the expense ---')
                print('1. Housing: Rent/Mortgage, property tax, home insurance.')
                print('2. Utilities: Electricity, water, gas, internet, phone bill.')
                print('3. Food & Dining: Groceries, restaurants, coffee shops, takeout.')
                print('4. Transport: Fuel, public transit, car maintenance, Uber/Lyft.')
                print('5. Health: Health insurance, pharmacy, doctor visits, gym.')
                print('6. Entertainment: Streaming services, movies, hobbies, gaming.')
                print('7. Shopping: Clothes, electronics, home decor, personal care.')
                print('8. Debt & Loans: Credit card payments, student loans, personal loans.')
                print('9. Education: Books, online courses, tuition, certifications.')
                print('10. Gifts & Donations: Birthdays, holiday gifts, charity, tithes.')
                print('11. Insurance: Car, life, or disability insurance (if not in Housing).')
                print('12. Miscellaneous: Emergency costs, repairs, or one-off expenses.\n')

                cat = (input("Enter the Category of the Expenses: "))
                if cat.strip() in list(map(str,list(range(1,13)))):
                    category = categories[int(cat)-1]
                    NotDone = False
                else:
                    print("Enter a valid input. Try again.")

            

            def isdatecorrect(date:str) -> bool:
                try:
                    datetime.datetime.strptime(date, '%d.%m.%Y')
                    return True
                except ValueError:
                    return False
            
            def iscurrentmonth(date:str) -> bool:
                
                d = datetime.datetime.strptime(date,'%d.%m.%Y')
                month = d.strftime('%m')
                if str(currentMonth) == str(month):
                    return True
                else:
                    return False
            
            def getMonthkey(date:str) -> str:
                d = datetime.datetime.strptime(date,'%d.%m.%Y')
                month = d.strftime('%m')
                year = d.strftime('%Y')
                return str(month)+str(year)

                


                
            NotDone = True   
            while NotDone:
                print('\n--- If the expense is of today Press Enter/ Otherwise Enter the date (dd.mm.yyyy) ---')
                ofToday = input('Press Enter/ dd.mm.yyyy: ')
                if not ofToday:
                    currentExpenseList.add(amt,category)
                    NotDone = False
                
                else:
                    if isdatecorrect(ofToday):
                        if iscurrentmonth(ofToday):
                            currentExpenseList.add(amt,category,ofToday)
                        else:
                            currentMonthKey= getMonthkey(ofToday)
                            if currentMonthKey not in allExpenses:
                                allExpenses[currentMonthKey] = {}
                            currentDict = allExpenses[currentMonthKey]
                            currentExpenseList = ExpenseList(currentDict)
                            currentExpenseList.add(amt,category,ofToday)
                            currentExpenseList.display()

                        NotDone = False
                    
                    else:
                        print('Enter Valid date in correct format dd.mm.yyyy. Try again')
                
        case '2' :
            print('--- Enter the serial number to remove or 0 to exit ---')
            NotDone = True
            while NotDone:
                try: 
                    serialNum = int(input(f'Enter Serial Number(1-{currentExpenseList.getLastsno()-1}):'))
                    
                    if serialNum >= 1 and serialNum < currentExpenseList.getLastsno():
                        currentExpenseList.remove(serialNum)
                        NotDone = False
                    elif serialNum == 0:
                        print('Nothing changed.')
                        NotDone = False
                    else:
                        raise ValueError('Invalid input')
                
                except ValueError:
                    print('Enter a valid input. Try again')

        case '4':
            print("--- Your This month's Expenses ---""")
        

        case '5':
            print("--- Saving Your Data ---")
            save()
            time.sleep(5)
            DontExit = False

        



    

