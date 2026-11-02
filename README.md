# Expense Tracker

## About it :

The expense Tracker is a tool to lets you keep track of your expenses and manage them when you need it

---

## Features

-  The user can add an expense
- The user can modify a specific expense
- The user can remove a specific expense
- The user can view the whole list of expenses
- The user can view the assessment (Total amount, smallest amount, biggest amount, average expenditure)
- The user can view the expenses per category
- The user can quit the program when he is done

---

## Requirements

- Python 3.14

---

## Installation

1. Clone the repository by using the `git clone repo` command and replacing "repo" by the repository URL
2. Create a virtual environment by using the `python -m venv` command.
3. Activate the virtual environment with the `source .venv/bin/activate` command.

---

## Usage

To run the tool, you simply need to use the `python3 main.py` command

```bash
python3 main.py
```




- Once ran, the banner is going to pop up and a welcoming message is gonna follow it:

```
    _   _   _   _   _   _   _     _   _   _   _   _   _  _   _
  / \\ / \\ / \\ / \\ / \\ / \\ / \\   / \\ / \\ / \\ / \\ / \\
 ( E | x | p | e | n | s | e ) ( T | r | a | c | k | e | r | 💵 )
 \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/\\ _/ \\_/ \\_/ \\_/ \\_/ \\_/
 |-------------------------------------------------------------------------------------------------------------|
|Hi, you succesfully got into the Expense Tracker 💵🖲️📜 program! Here is the menu below of things you can do |
|--------------------------------------------------------------------------------------------------------------|
```

- With the menu below of different things you can to manage your expenses:

```
                                                            |
                                                            |
                                                            |
                                                           ⬇️
                                                          𝐦𝐞𝐧𝐮
               |-------------------------------------------------------------------------------------------|
               |                                                                                           |
               |--> [1] Add an expense 💵 (description 📜, amount 💳 and category🏢)                     |
               |                                                                                           |
               |--> [2] Modify an expense from the list                                                    |
               |                                                                                           |
               |--> [3] Remove an expense from the list                                                    |
               |                                                                                           |
               |--> [4] View all the expenses                                                              |
               |                                                                                           |
               |--> [5] View the assessment 📜🟰                                                          |
               |                                                                                           |
               |--> [6] View the expenses per category  🏢💵                                              |
               |                                                                                           |
               |--> [7]  Quit 👍                                                                           |
               |                                                                                           |
               |-------------------------------------------------------------------------------------------|

                       Note: This tool allows you to keep track of your expenses if you need it!
 
 
Choose your action (1-7)

┌───(user)~[Expense Tracker 📜💵]
└─> 
```

- You can select your action by choosing the number corresponding to the action (for instance, you choose 1 because you wanted to add a task)



## Examples:

​     **Important Note**: If you did not add any expenses (If you never chose option 1), and you choose one of the options between 2 to 6, there is gonna be no output and the program is going to let you know and gonna bring you back to the menu.

- To view the whole list of expenses, you simply type 4 and press Enter to see it and it is going to ask you to confirm your view so it brings you back to the menu.

>  Visual version:

```

┌───(user)~[Expense Tracker 📜💵]
└─> 4
  
  
  
  
                                                ====== Expenses ======
                                                
                                                
                                                
                                                    _____________

Expense 1:

                                                    Description: Jewerly
                                                    Amount: 800.0$
                                                    Category: Luxury

                                                    _____________

Expense 2:

                                                    Description: GTA6
                                                    Amount: 80.0$
                                                    Category: Games

                                                    _____________

Expense 3:

                                                    Description: college
                                                    Amount: 450.0$
                                                    Category: Education

Finished viewing the expenses? (Press Enter to confirm)


┌───(user)~[Expense Tracker 📜💵]
└─>
```



- To modify a specific expense, you would have to type 2 and press Enter. It will show all the expenses in order and you would have to choose which expense to modify (Note: you have to choose enter its corresponding number to choose it). If you are not sure which expense to modify, type 0 and press Enter

Visual version example:

```
┌───(user)~[expense-tracker]
└─> 2



Which of the following expense do you want to modify?
                                                    _____________

Expense 1:

Description: Jewerly, Amount: 800.0$, Category: Luxury


                                                    _____________

Expense 2:

Description: GTA6, Amount: 80.0$, Category: Games


                                                    _____________

Expense 3:

Description: college, Amount: 450.0$, Category: Education




Have you decided which expense modify ?
---> If not, you can simply type 0 and press enter.
---> If you did, you can select which expense by selecting its number
 Quick Example: if you want to modify the 'Jewerly' expense which is the 1st expense if you check in the list its description, you can simply type 1 and press enter


┌───(user)~[Expense Tracker 📜💵]
└─>
```

Then once you select the expense, it will ask you which information (description, amount or category) do you want to modify:

For instance, if I choose the expense 3 (the third expense that you can see above which has "college" as the description), this is how it would look like:

```
┌───(user)~[expense-tracker]
└─> 3
Here are the informations about the expense you chose

[1] Description: college

[2] Amount: 450.0$

[3] Category: Education



Which information about the expense do you want to modify ? (1/3)


┌───(user)~[Expense Tracker 📜💵]
└─>
```

Then, I type 2 to modify its category, and I change it to 600 $, it is going to update it as 450 $ before to 600 $:

```
┌───(user)~[Expense Tracker 📜💵]
└─> 2
Enter your new amount below:



┌───(user)~[Expense Tracker 📜💵]
└─> 600


[*] Updated the amount as 450.0$ to 600.0$
```



## Project Structure

```
expense-tracker/
├── README.md
├── docs
│    └── PROJET_04_EXPENSE_TRACKER.md
├── main.py
├── plan.md
├── spendings.json
└── testing.py
```



### Author

```
Created by ecalexandre
```



