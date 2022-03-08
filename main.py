from admin import *
from create_file import *
from total import *
from cases_catgeory import *
from plot import line_graph

#Check if user is an admin or a normal user
print("Welcome!")
admin_or_user = int(input("Are you an Administrator or User?\n1 - Admin\n2 - User\n(1/2): "))

if admin_or_user == 1:
    admin() #This includes admin authentication, updation of data and viewing of graphs

elif admin_or_user == 2:
    choice = input("Would you like to view the graph? (y/n): ").lower()
    
    if choice == "y":
        line_graph(cases_category()) #This includes choosing of categories and viewing the graphs
    
    else:
        print("Exiting the program")
    
