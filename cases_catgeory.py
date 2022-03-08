from total import *

def cases_category():
    """Returns the categories for which the user wants the see the graphs of"""
    
    categories = []

    while True:
        choice = int(input("Which category would you like to view?\n1 - Total Cases\n2 - Total Deaths\n3 - Total Recovered\n4 - Total Active Cases\n(1/2/3/4): "))

        for category in choices:  # choices is a part of total.py
            if choice == category:
                if choices[category] not in categories:
                    categories.append(choices[category])
                else:
                    print("Category either does not exist or has already been chosen")
        
        another_category = input("Would you like to add another category?\n(y/n): ")

        if another_category.lower() == "n":
            break

    return categories




