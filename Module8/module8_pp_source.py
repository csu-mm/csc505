# Python Program: 
# CSC505: Principles of Software Development
# Module 8: Portfolio Project
# Professor: Dr. Bingdong Li 
# Created by Mukul Mondal
# Friday, Sept 5, 2025

'''
Problem statement:
-- Stepwise Refinement Approach --

Write a Python Script that will print all the steps in sequence for all 
the operations at the teller machine as shown in your diagram(s)
'''


from os import system, name


# This is just a helper function to clear the screen
# This is not required, per problem statement.
def clearScreen():
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    print("")
    return


# Sequence Diagram, Step details
def execute_module8_pp_Print_Sequential_Steps():
    print("=== Teller machine : ATM ===")
    print("=== Assumption: Customer does single operation: Cash Withdraw ===")
    print("=== ATM is running and ready for customer use ===")
    print("=== Objects in the Sequence diagram: Customer, ATM, Bank ===")
    print("=== Sequential Triggered Steps in the Sequence Diagram ===")    
    print("\t: Customer: Insert Card in ATM")
    print("\t: ATM: Validates Card with Bank")
    print("\t: Result from Bank has two options: Card valid, Card Invalid")
    print("\t: ATM: If Card is Invalid: Eject Card to the Customer")
    print("\t: ATM: If Card is Valid: ATM asks Customer to Enter PIN")
    print("\t: Customer: Enter Card PIN")
    print("\t: ATM: Verify PIN with Bank")
    print("\t: Result from Bank has two options: PIN valid, PIN Invalid")
    print("\t: Bank: Invalid PIN")
    print("\t: Customer gets 3 chances to Enter Valid PIN")
    print("\t: If still Invalid PIN then")
    print("\t: ATM: Eject Card to the Customer")
    print("\t: If Valid PIN then")
    print("\t: ATM: Request Customer to Enter withdraw Amount")
    print("\t: Customer: Enter Winthdraw Amount")
    print("\t: ATM: Checks for Enough Balanace with the Bank")
    print("\t: Result from Bank has two options: True, False")
    print("\t: If Enough Balance is False then")
    print("\t: ATM: Informs the Customer")
    print("\t: ATM: Eject Card to the Customer")
    print("\t: If Enough Balance is True then")
    print("\t: ATM: Dispense Cash to the Customer")
    print("\t: ATM: Print Receipt")
    print("\t: ATM: Sends Update Balance request to the Bank")    
    print("\t: ATM: Eject Card to the Customer")
    return


if __name__ == "__main__":
    clearScreen()
    print("=== Module 8: Portfolio Project ===")
    print("=== Print all the steps in sequence for 'withdrawing money' operation at the teller machine ===")
    execute_module8_pp_Print_Sequential_Steps()
