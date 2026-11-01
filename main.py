''' expense-tracker/main.py '''

# This source code file is the file among all the files for this program that you have run to be able to use the expense tracker tool

# ---------Imported Modules/librairies📚------------- #
import time
import json
# --------------------------------------------------- #

# ============== Text Colors 🖼️ and Text Styles 📜============
GREEN = "\033[32m"
DARK_GRAY = "\033[1;30m"
CREAM_YELLOW = "\033[38;2;255;253;208m"
BROWN = "\033[0;33m"
LIGHT_BLUE = "\033[38;2;173;216;230m"
YELLOW = "\033[1;33m"
UNDERLINE = "\033[4m"  
RESET_COLOR = "\033[0m"
# =============================================================


# --------------------------------------------------------------------- Core Functions ⚙️ --------------------------------------------------------------------------------- #
def display_chars_one_by_one(delay: float|int, sequence_of_chars: str) -> None:
  for char in sequence_of_chars:
    print(char, end='', flush=True)
    time.sleep(delay)
  print()

def check_values(variable_name) -> str|float:
    ''' Checks value of user input for each information about the expense ''' 
    global CREAM_BLUE
    global LIGHT_BLUE
    global BROWN
    global RESET_COLOR
    
    description : str = "N/A"
    amount : str = "N/A"
    category : str = "N/A"

    match variable_name:
        
        case variable if variable == "description" :           
           while True:
               choice = input("└─> ")
                
               match len(choice):
                case value if value > 0:
                    description = choice
                    break
                
                case _:    
                   display_chars_one_by_one(0.01,f"\n\n\n{BROWN}Error ❌: '{choice}' is not a valid description, it has to contain at least 1 word, try again")
                   print(f"\n\n\n{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")        
       
        case variable if variable == "amount":
            while True:
                choice = input("└─> ")
                
                try:
                    num = int(choice)
                    match num:
                        case value if value > 0:
                            amount = num
                            break
                            
                        case _:
                            display_chars_one_by_one(0.01,f"\n\n\n{BROWN}Error ❌: '{num}' is not a valid amount, try again")
                            print(f"\n\n\n{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")
                            
                            
                except ValueError:
                   display_chars_one_by_one(0.01,f"\n\n\n{BROWN}Error ❌: '{choice}' is not a valid amount, try again")
                   print(f"\n\n\n{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")
            
        case variable if variable == "category":
           while True:
               choice = input("└─> ")
                    
               match len(choice):
                case value if value > 0:
                    category = choice
                    break
                       
                case _:
                   display_chars_one_by_one(0.01,f"\n\n\n{BROWN}Error ❌: '{choice}' is not a valid category, try again")
                   print(f"\n\n\n{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]") 
                     
    match variable_name:
        case "description": return description
        case "amount": return amount
        case "category": return category

def load_data_from_(file) -> list:
    ''' Loads json data from spendings.json '''
    file_opened = open(file, "r")
    loaded_file = json.load(file_opened)
    
    return loaded_file

def write_in_(file, text) -> None:
    '''Overwrites the spendings.json file into the dumped loaded json data'''
    with open(file, "w") as file:
        file.write(text)
  
# Option 1: Add an expense      
def add_expense() -> None:
    ''' Allows user to add expenses (description, amount, category) to the spendings.json list '''
    global CREAM_BLUE
    global LIGHT_BLUE
    global RESET_COLOR
    
    loaded_data : list = load_data_from_("spendings.json")
    
    print("\n\n\n"); display_chars_one_by_one(0.03, f"{CREAM_YELLOW}Enter your description below:\n\n\n");  print(f"{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")
    description : str = check_values("description")
    
    print("\n\n"); display_chars_one_by_one(0.03, f"{CREAM_YELLOW}Enter the amount here below:\n\n\n"); print(f"{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")
    amount : float = float(check_values("amount"))
    
    print("\n\n"); display_chars_one_by_one(0.03, f"{CREAM_YELLOW}Enter the category below:\n\n\n"); print(f"{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")
    category : str = check_values("category")
    
    expense_infos : dict = {"description": description,
                           "amount": amount,
                           "category": category
    }
    
    loaded_data.append(expense_infos)
    
    loaded_data_dumped = json.dumps(loaded_data, indent=4)
    write_in_("spendings.json", loaded_data_dumped)
    
    print("\n\n")
    for index, info in enumerate(expense_infos, start=1):
        display_chars_one_by_one(0.03, f"{CREAM_YELLOW}[{index}] {info.title()}:  {LIGHT_BLUE if info == "amount" else ""}{expense_infos[info]}{RESET_COLOR if info == "amount" else ""}{"$" if info == "amount" else ""}{RESET_COLOR}")
     
    display_chars_one_by_one(0.03, f"\n\n{GREEN}[+] Added your expense to the list of all your expenses!{RESET_COLOR}\n\n"); print("\n")

# 2: Modify an expense
def modify_and_update_expense(expense_selected, selected_data_index) -> None:
    global CREAM_YELLOW
    global LIGHT_BLUE
    global BROWN
    global RESET_COLOR
    
    loaded_data : list = load_data_from_("spendings.json")
    
    display_chars_one_by_one(0.03, f"{CREAM_YELLOW}Here are the informations about the expense you chose\n")
    for index, info in enumerate(expense_selected, start=1):
        display_chars_one_by_one(0.04, f"[{index}] {info.title()}: {LIGHT_BLUE if info == "amount" else ""}{expense_selected[info]}{RESET_COLOR if info == "amount" else ""}{"$" if info == "amount" else ""}\n")
    
    display_chars_one_by_one(0.03, f"\n\nWhich information about the expense do you want to modify ? (1/3)\n---> If you are not sure, enter 0\n\n")
    print(f"\n\n\n{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")
    while True:
        user_information_choice = input(f"└─> ")
        try:
            user_information_choice_num = int(user_information_choice)
            match user_information_choice_num:
                
                case value if value == 1: # Description
                    display_chars_one_by_one(0.03, f"\n\n\n{CREAM_YELLOW}Enter your new description below:"); print("\n\n\n")
                    print(f"{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")
                    
                    new_description : str = check_values("description")
                    loaded_data[selected_data_index]["description"] = new_description
                    new_dumped_loaded_data = json.dumps(loaded_data, indent=4)
                    write_in_("spendings.json", new_dumped_loaded_data)
                    
                    print("\n"); display_chars_one_by_one(0.03, f"{YELLOW}[*] Updated the description as {expense_selected["description"]} to {new_description}{RESET_COLOR}"); print("\n\n")
                
                    break
                
                case value if value == 2: # Amount
                    display_chars_one_by_one(0.03, f"\n\n\n{CREAM_YELLOW}Enter your new amount below:"); print("\n\n\n")
                    print(f"{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")
                    
                    new_amount : float = float(check_values("amount"))
                    loaded_data[selected_data_index]["amount"] = new_amount
                    new_dumped_loaded_data = json.dumps(loaded_data, indent=4)
                    write_in_("spendings.json", new_dumped_loaded_data)
                    
                    print("\n"); display_chars_one_by_one(0.03, f"{YELLOW}[*] Updated the amount as {LIGHT_BLUE}{expense_selected["amount"]}{RESET_COLOR}$ {YELLOW}to {LIGHT_BLUE}{new_amount}{RESET_COLOR}$"); print("\n\n")
                
                    break

                case value if value == 3: # category
                    display_chars_one_by_one(0.03, f"\n\n\n{CREAM_YELLOW}Enter your new category below:"); print("\n\n\n")
                    print(f"{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")
                    
                    new_category : str = check_values("category")
                    loaded_data[selected_data_index]["category"] = new_category
                    new_dumped_loaded_data = json.dumps(loaded_data, indent=4)
                    write_in_("spendings.json", new_dumped_loaded_data)
                    
                    print("\n"); display_chars_one_by_one(0.03, f"{YELLOW}[*] Updated the category as {expense_selected["category"]} to {new_category}{RESET_COLOR}"); print("\n\n")
                
                    break

                case 0:
                    display_chars_one_by_one(0.02, f"{CREAM_YELLOW}Got it! Come back when you're sure!"); print("\n\n\n")
                    break

                case _:
                    display_chars_one_by_one(0.03, f"\n\n\n{BROWN}Error ❌: '{user_information_choice_num}' isn't among the possible choices here, try again"); print(f"\n\n\n{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")
        
        except ValueError:
        	display_chars_one_by_one(0.03, f"\n\n\n{BROWN}Error ❌: '{user_information_choice}' isn't among the possible choices here, try again\n"); print(f"\n\n\n{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")
                    
# 3: Remove an expense
def confirm_expense_deletion(expense_selected, selected_data_index) -> None:
    global CREAM_YELLOW
    global LIGHT_BLUE
    global BROWN
    global RESET_COLOR
    
    loaded_data = load_data_from_("spendings.json")
    
    display_chars_one_by_one(0.02, f"{CREAM_YELLOW}Are you sure you want to delete this expense from the list of expenses you added ?(Y/n):"); print("\n")
    
    for index, info in enumerate(expense_selected, start=1):
        display_chars_one_by_one(0.007, f"[{index}] {info.title()}: {LIGHT_BLUE if info == "amount" else ""}{expense_selected[info]}{RESET_COLOR if info == "amount" else ""}{"$" if info == "amount" else ""}\n")
    print(f"{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")
        
    while True:
        choice = input(f"└─> ")
        match choice.upper():
            
            case answer if answer == "Y":
                loaded_data.pop(selected_data_index)
                new_dumped_loaded_data = json.dumps(loaded_data, indent=4)
                write_in_("spendings.json", new_dumped_loaded_data)
                
                print("\n"); display_chars_one_by_one(0.03, f"{DARK_GRAY}[-] Removed 1 expense from the list{RESET_COLOR}"); print("\n\n")
                break
                
            case answer if answer == "N":
                display_chars_one_by_one(0.01, f"{CREAM_YELLOW}Canceled deletion{RESET_COLOR}"); print("\n\n")
                break
            
            case _:
                display_chars_one_by_one(0.03, f"\n\n\n{BROWN}Error ❌: This isn't a valid answer, try again"); print(f"\n\n\n{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")

# For options 2 and 3: modify/remove an expense
def select_and_update_or_remove_expense(function) -> None:
    global CREAM_YELLOW
    global LIGHT_BLUE
    global BROWN
    global RESET_COLOR
    
    expense_number : int = 1
    loaded_data : list = load_data_from_("spendings.json")
     
    match len(loaded_data):

        case length if length > 0: # If the list has more than 0 elements, it will make him decide which expense to delete/modify
            print("\n\n\n\n")
            display_chars_one_by_one(0.02, f"{CREAM_YELLOW} Which of the following expense do you want to {function}?")
            for expense in loaded_data:
                print(f"{' '*52}_____________\n\nExpense {expense_number}:\n")
                display_chars_one_by_one(0.007,f"Description: {expense["description"]}, Amount: {LIGHT_BLUE}{expense["amount"]}{RESET_COLOR}$, {CREAM_YELLOW}Category: {expense["category"]}\n\n")
                expense_number += 1

            display_chars_one_by_one(0.006, f"\n\nHave you decided which expense {function} ?\n---> If not, you can simply enter 0.\n---> If you did, you can select which expense by selecting its number\n Quick Example: if you want to {function} the '{loaded_data[0]["description"]}' expense which is the 1st expense if you check in the list its description, you can simply type 1 and press enter\n\n"); print(f"{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")   
            while True:
                 user_expense_choice = input("└─> ")
                 try:
                    user_expense_choice_num = int(user_expense_choice)
                    match user_expense_choice_num:
                       case  value if value not in [expense_index+1 for expense_index in range(len(loaded_data))] and value != 0:
                            display_chars_one_by_one(0.02, f"\n{BROWN}Error: '{user_expense_choice_num}' is not among all the possible choices in the list, choose a valid number to choose your expense\n"); print(f"{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")
                       case 0:
                           display_chars_one_by_one(0.03, f"{CREAM_YELLOW}Understood. Come back next time when you know which expense to {function} :){RESET_COLOR}\n\n")
                           break
                       case value if value in [expense_index+1 for expense_index in range(len(loaded_data))]:
                           for expense_number in [expense_index+1 for expense_index in range(len(loaded_data))]:
                            if value == expense_number:
                                data_index = expense_number - 1
                                expense_selected = loaded_data[data_index]
                                
                                match function:
                                    case func if func == "modify":
                                        modify_and_update_expense(expense_selected, data_index)
                                        break
                                        

                                    case func if func == "delete":
                                        confirm_expense_deletion(expense_selected, data_index)
                                        break
                           break
                                                
                 except ValueError:
                    display_chars_one_by_one(0.01, f"\n{BROWN}Error ❌: '{user_expense_choice}' is not a valid choice, try again")
                    print(f"\n\n\n{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")
                    
        case 0: # If the list has 0 elements, it will bring him back to the menu
             display_chars_one_by_one(0.03, f"\n\n\n{BROWN}Error ❌: There was no expenses added here. Add some to be able to {function}{RESET_COLOR}")
             print("\n\n\n")

# Option 4: View all the expenses
def view_expenses() -> None:
    global CREAM_BLUE
    global LIGHT_BLUE
    global BROWN
    global RESET_COLOR
    
    expense_number : int = 1
    loaded_data : list = load_data_from_("spendings.json")
        
    match len(loaded_data):  
        case value if value > 0:
            print("\n\n\n\n"); print(f"{' '*48}====== Expenses ======")
            for expense in loaded_data:
                print(f"{' '*52}_____________\n\n{CREAM_YELLOW}Expense {expense_number}:\n")
                display_chars_one_by_one(0.006,f"{' '*52}{CREAM_YELLOW}Description: {expense["description"]}")
                display_chars_one_by_one(0.006,f"{' '*52}Amount: {RESET_COLOR}{LIGHT_BLUE}{expense["amount"]}{RESET_COLOR}$")
                display_chars_one_by_one(0.006,f"{' '*52}{CREAM_YELLOW}Category: {expense["category"]}{RESET_COLOR}\n")
                expense_number += 1

            display_chars_one_by_one(0.03, f"\nFinished viewing the expenses? (Press Enter to confirm)\n\n")
            print(f"{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]"); press_enter = input(f"└─> {RESET_COLOR}"); print("\n")
                      
        case 0: # If the list has 0 elements, it will bring him back to the menu
             display_chars_one_by_one(0.03, f"\n\n\n{BROWN}Error ❌: There was no expenses added here. Add some to view them{RESET_COLOR}")
             print("\n\n\n")

# Option 5: View the Assessment
def view_the_overview_of_the_expense() -> None:
    global CREAM_YELLOW
    global LIGHT_BLUE
    global BROWN
    global RESET_COLOR
    
    loaded_data : list = load_data_from_("spendings.json")

    match len(loaded_data):  
        case value if value > 0:
            
            expense_number : int = 1
            total_amount : int = 0
            average_expenditure : int = 0
    
            list_of_amounts : list = [expense["amount"] for expense in loaded_data]
    
            smallest_amount : float = min(set(list_of_amounts))
            biggest_amount : float = max(set(list_of_amounts))
            
            print("\n\n\n\n")
            for expense in loaded_data:
                display_chars_one_by_one(0.006,f"{' '*52}{RESET_COLOR}_____________\n\n{CREAM_YELLOW}Expense {expense_number}:{RESET_COLOR}\n")
                display_chars_one_by_one(0.006,f"{' '*52}{CREAM_YELLOW}Description: {expense["description"]}\n")
                display_chars_one_by_one(0.006,f"{' '*52}Amount: {RESET_COLOR}{LIGHT_BLUE}{expense["amount"]}{RESET_COLOR}$\n")
                display_chars_one_by_one(0.006,f"{' '*52}{CREAM_YELLOW}Category: {expense["category"]}{RESET_COLOR}\n\n")
               
                # operations
                expense_number += 1
                total_amount += expense["amount"]
                average_expenditure += expense["amount"]
              
            average_expenditure /= len(loaded_data)
                      
            display_chars_one_by_one(0.007, f"\n{' '*52}{CREAM_YELLOW}Total amount:{RESET_COLOR} {LIGHT_BLUE}{total_amount}{RESET_COLOR}$\n{' '*52}{CREAM_YELLOW}Average expenditure: {LIGHT_BLUE}{round(average_expenditure)}{RESET_COLOR}$\n{' '*52}{CREAM_YELLOW}Smallest amount: {LIGHT_BLUE}{smallest_amount}{RESET_COLOR}$\n{' '*52}{CREAM_YELLOW}Largest amount:{LIGHT_BLUE}{biggest_amount}{RESET_COLOR}$")
            display_chars_one_by_one(0.03, f"\n{CREAM_YELLOW}Finished viewing the assessment? (Press Enter to confirm){RESET_COLOR}\n\n")
            
            print(f"{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]"); press_enter = input(f"└─> {RESET_COLOR}"); print("\n")
                      
        case 0: # If the list has 0 elements, it will bring him back to the menu
             display_chars_one_by_one(0.03, f"\n\n\n{BROWN}Error ❌: There was no expenses added here. Add some to view the assessment{RESET_COLOR}")
             print("\n\n\n")


# Option 6: View each expenses per category
def view_expenses_per_category() -> None:
    global CREAM_YELLOW
    global LIGHT_BLUE
    global BROWN
    global UNDERLINE
    global GREEN
    global RESET_COLOR

    loaded_data: list = load_data_from_("spendings.json")
    list_of_categories: set = set([expense["category"].upper() for expense in loaded_data])
    
    
    match len(loaded_data):
       
        case value if value > 0:
            print("\n\n\n\n")
            display_chars_one_by_one(0.04, f"{CREAM_YELLOW}Here is all the expenses per category ----------{RESET_COLOR}")
            print(f"{' '* 47}↓\n\n\n")
            for category in list_of_categories:
               display_chars_one_by_one(0.02,f"\n\n{UNDERLINE}Category: {GREEN}{category.title()}{RESET_COLOR}")
               
               for expense in loaded_data:
                if expense["category"].upper() == category.upper():
                    display_chars_one_by_one(0.006,f"\n'Description: {expense["description"]}, Amount: {LIGHT_BLUE}{expense["amount"]}{RESET_COLOR}$'\n\n")
            
            display_chars_one_by_one(0.03, f"\n\n{CREAM_YELLOW}Finished viewing the expenses per category? (Press Enter to confirm)\n\n{RESET_COLOR}")
            print(f"{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]"); press_enter = input(f"└─> {RESET_COLOR}"); print("\n")

        case 0: # If the list has 0 elements, it will bring him back to the menu
            display_chars_one_by_one(0.03, f"\n\n\n{BROWN}Error ❌: There was no expenses added here. Add some to view them{RESET_COLOR}")
            print("\n\n\n")


def print_expense_tracker_menu() -> None:
    
    '''This shows the menu of the possible actions the user can do for his/her expenses'''

    list_of_options : list = ["Add an expense 💵 (description 📜, amount 💳 and category🏢)",
                         "Modify an expense from the list ",
                         "Remove an expense from the list ",
                         "View all the expenses",
                         "View the assessment 📜🟰 ",
                         "View the expenses per category  🏢💵",
                         " Quit 👍"]
    
    print(f"{" "*58}𝐦𝐞𝐧𝐮"); print(f"{" "*15}|{"-"*91}|"); print(f"{" "*15}|{" "*91}|"); print(f"{" "*15}|--> [{LIGHT_BLUE}1{RESET_COLOR}] {list_of_options[0]}{" "*23}|\n{" "*15}|{" "*91}|")
    print(f"{" "*15}|--> [{LIGHT_BLUE}2{RESET_COLOR}] {list_of_options[1]}{" "*51}|\n{" "*15}|{" "*91}|"); print(f"{" "*15}|--> [{LIGHT_BLUE}3{RESET_COLOR}] {list_of_options[2]}{" "*51}|\n{" "*15}|{" "*91}|")
    print(f"{" "*15}|--> [{LIGHT_BLUE}4{RESET_COLOR}] {list_of_options[3]}{" "*62}|\n{" "*15}|{" "*91}|"); print(f"{" "*15}|--> [{LIGHT_BLUE}5{RESET_COLOR}] {list_of_options[4]}{" "*58}|\n{" "*15}|{" "*91}|")
    print(f"{" "*15}|--> [{LIGHT_BLUE}6{RESET_COLOR}] {list_of_options[5]}{" "*47}|\n{" "*15}|{" "*91}|"); print(f"{" "*15}|--> [{LIGHT_BLUE}7{RESET_COLOR}] {list_of_options[6]}{" "*75}|\n{" "*15}|{" "*91}|")
    print(f"{" "*15}|{"-"*91}|"); print(f"\n{" "*23}Note: This tool allows you to keep track of your expenses if you need it!")
    display_chars_one_by_one(0.02, f"\n\n{CREAM_YELLOW}Choose your action (1-7)\n"); print(f"{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #


# ------------------------------------ Main function 💪 -------------------------------------------------------- #
def main() -> None:
    global CREAM_YELLOW
    global LIGHT_BLUE
    global BROWN
    global RESET_COLOR

    expense_tracker_running : bool = True

    display_chars_one_by_one(0.003, r"""
    _   _   _   _   _   _   _     _   _   _   _   _   _  _   _
  / \\ / \\ / \\ / \\ / \\ / \\ / \\   / \\ / \\ / \\ / \\ / \\ 
 ( E | x | p | e | n | s | e ) ( T | r | a | c | k | e | r | 💵 )
 \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/\\ _/ \\_/ \\_/ \\_/ \\_/ \\_/ 
    """)
    print("|-------------------------------------------------------------------------------------------------------------|")
    display_chars_one_by_one(0.02,"|Hi, you succesfully got into the Expense Tracker 💵🖲📜 program! Here is the menu below of things you can do  |")
    print("|-------------------------------------------------------------------------------------------------------------|")
    print(r"""                                                            |
                                                            |
                                                            |
                                                            ⬇️""")
    print_expense_tracker_menu()
    while expense_tracker_running:
     users_menu_choice = input("└─> ")
     try:
       user_number = int(users_menu_choice)
       match user_number:

       	case 1: add_expense(); print_expense_tracker_menu() # If the user chooses 1, the add_expense() function will make him add a new expense
        
        case 2: select_and_update_or_remove_expense("modify"); print_expense_tracker_menu() # If the user chooses 2, the select_and_update_or_remove_expense("modify") function will make him modify an expense if he actually desires
        
        case 3: select_and_update_or_remove_expense("delete"); print_expense_tracker_menu() # If the user chooses 3, the select_and_update_or_remove_expense("delete") function will make him delete an expense if he actually desires
        
        case 4: view_expenses(); print_expense_tracker_menu() # If the user chooses number 4, the view_expense() function will make him view all the added expenses
        
        case 5: view_the_overview_of_the_expense(); print_expense_tracker_menu() # If the user chooses number 5, the view_the_overview_of_the_expense() function will make him view the overview of the expenses
        
        case 6: view_expenses_per_category(); print_expense_tracker_menu() # If the user chooses number 6, the view_expenses_per_category() function will make him viewthe expenses of each category
        
        case 7: # If user chooses 7, the main program terminates
        	display_chars_one_by_one(0.02, f"\n\n{CREAM_YELLOW}Come back next time! :){RESET_COLOR}\n"); time.sleep(0.5)
        	expense_tracker_running = False
        	
            
        case _: # If user puts a wrong number, the user will have to answer again until he chooses a valid option
          display_chars_one_by_one(0.01,f"\n\n\n{BROWN}Error ❌: #{user_number} is not among the possible choices here, try again")
          print(f"\n\n\n{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")
     
     except ValueError: # If user puts a wrong input value, the user will have to answer again until he chooses a valid option
       display_chars_one_by_one(0.01,f"\n\n\n{BROWN}Error ❌: '{users_menu_choice}' is not a valid choice, try again{RESET_COLOR}")
       print(f"\n\n\n{LIGHT_BLUE}┌───(user)~[Expense Tracker 📜💵]")

# ------------------------------------------------------------------------------------------------------- #


# Running 🏃‍♂️ the main function (the program 🤖)
# ------------------------------------------- #
if __name__ == "__main__":
   main()
# ------------------------------------------- #