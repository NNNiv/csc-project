import os
import time
import csv

path = "./covid data/"

months = [
    ["01-Jan", 31],
    ["02-Feb", 28],
    ["03-Mar", 31],
    ["04-Apr", 30],
    ["05-May", 31],
    ["06-Jun", 30],
    ["07-Jul", 31],
    ["08-Aug", 31],
    ["09-Sep", 30],
    ["10-Oct", 31],
    ["11-Nov", 30],
    ["12-Dec", 31]
]


def update_data(new_file):
    """Updates the data as per the template csv file"""

    with open('template.csv', 'r') as template:
        reader = csv.reader(template)
        writer = csv.writer(new_file)
        row_count = 0
        for row in reader:
            if row_count == 0:
                writer.writerow(row)
                row_count += 1
            else:
                print(f"Enter today's data for {row[0]}\n")
                confirmed = int(input("Confirmed cases: "))
                deaths = int(input("Total deaths: "))
                recovered = int(input("Total recovered: "))
                active = int(input("Active cases: "))
                writer.writerow([row[0], row[1], confirmed, deaths, recovered, active])
    print("Data updated successfully")

def create_file():
    """Creates the new file for the next day
       along with a new folder for the next month
       if the current month is over"""

    folders = []
    for folder in sorted(os.listdir(path)):
        days = sorted(os.listdir(path+folder))
        folders.append([folder, len(days)])
    
    for month in months:
        if folders[len(folders)-1][0] == month[0]:
            if folders[len(folders)-1][1] == month[1]:
                next_month = len(folders) + 1
                folder_path = f"{path}0{next_month}-{months[len(folders)][0][3:]}" 
                if next_month < 10:                        
                    os.mkdir(folder_path)
                    print("Folder created successfully")
                    time.sleep(3)   
                    with open(f"{folder_path}/01-0{next_month}-2021.csv", "w") as new_file:
                        print("File Created successfully\n")
                        update_data(new_file)
                        
            else:
                current_folder_path = f"{path}{folders[len(folders)-1][0]}/"
                list_of_days = sorted(os.listdir(current_folder_path))
                current_month = int(list_of_days[len(list_of_days)-1][3:5])
                next_day = int(list_of_days[len(list_of_days)-1][:2]) + 1
                
                if next_day < 10:
                    if current_month < 10:
                        with open(f"{current_folder_path}0{next_day}-0{current_month}-2021.csv", "w") as new_file:
                            print("File Created Successfully\n")
                            update_data(new_file)


                    else:
                        with open(f"{current_folder_path}{next_day}-{current_month}-2021.csv", "w") as new_file:
                            print("File Created Successfully\n")
                            update_data(new_file)
                            

                else:
                    if current_month < 10:
                        with open(f"{current_folder_path}{next_day}-0{current_month}-2021.csv", "w") as new_file:
                            print("File Created Successfully\n")
                            update_data(new_file)

                    else:
                        with open(f"{current_folder_path}{next_day}-{current_month}-2021.csv", "w") as new_file:
                            print("File Created Successfully\n")
                            update_data(new_file)
                            
