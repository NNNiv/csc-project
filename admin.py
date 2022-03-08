import json
from cases_catgeory import cases_category
from create_file import update_data,  create_file
from plot import line_graph

def credential_check(): 
    """Checks the credintials of the administrator"""
        
    with open("admins.json", "r") as f:
        data = json.load(f)

    username = input("Enter your username: ").lower()
    password = input("Enter your passoword: ")
    for row in data:
        if row["username"].lower() == username and row["password"] == password:
            return True

def authentication():
    """Authenticates the admin"""

    while True:
        if credential_check():
            print("Login Successful")
            return True
        else:
            print("Failed to login\nPlease check your credentials")
            
            retry = input("Would you like to try authenticating again? (y/n): ").lower()
            if retry == "y":
                continue
            else:
                print("Exiting the program")
                break

def update_data():
    """Updates the data after admin authentication"""
    
    update_choice = input("Would you like to update the data? (y/n): ").lower()
    
    if update_choice == "y":
        create_file() #This function belongs to create_file.py
    else:
        choice = input("Would you like to view the graph? (y/n): ").lower()
        
        if choice == "y":
            line_graph(cases_category())
        else:
            print("Exiting the program")


def admin():
    """Performs all admin operations from above"""
    if authentication():
        update_data()


