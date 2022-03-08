import os
import csv

path = './covid data/'

def confirmed_total():
    """Returns the total number of confirmed cases"""
    
    month = []
    cases = []
    months = sorted(os.listdir(path))
    for folder in months:
        monthly_cases = 0
        days = sorted(os.listdir(path+folder))
        file_name = path + folder + '/' + days[len(days)-1]
        with open(file_name, "r") as file:
            row_count = 0
            data = csv.reader(file)
            for row in data:
                if row_count == 0:
                    row_count += 1
                else:
                    monthly_cases += int(row[2])
        
        month.append(folder[3:6])
        cases.append(monthly_cases)

    return month, cases, "Confirmed Cases"    

def deaths_total():
    """Returns the total number of deaths"""
    
    month = []
    deaths = []
    months = sorted(os.listdir(path))
    for folder in months:
        monthly_deaths = 0
        days = sorted(os.listdir(path+folder))
        file_name = path + folder + '/' + days[len(days)-1]
        with open(file_name, "r") as file:
            row_count = 0
            data = csv.reader(file)
            for row in data:
                if row_count == 0:
                    row_count += 1
                else:
                    monthly_deaths += int(row[3])
        
        month.append(folder[3:6])
        deaths.append(monthly_deaths)

    return month, deaths, "Deaths"    

def recovered_total():
    """Returns the total number of recovered cases"""

    month = []
    recovered = []
    months = sorted(os.listdir(path))
    for folder in months:
        monthly_recovered = 0
        days = sorted(os.listdir(path+folder))
        file_name = path + folder + '/' + days[len(days)-1]
        with open(file_name, "r") as file:
            row_count = 0
            data = csv.reader(file)
            for row in data:
                if row_count == 0:
                    row_count += 1
                else:
                    monthly_recovered+= int(row[4])
        
        month.append(folder[3:6])
        recovered.append(monthly_recovered)

    return month, recovered, "Recovered" 

def active_total():
    """Returns the total number of active cases"""

    month = []
    active = []
    months = sorted(os.listdir(path))
    for folder in months:
        monthly_active = 0
        days = sorted(os.listdir(path+folder))
        file_name = path + folder + '/' + days[len(days)-1]
        with open(file_name, "r") as file:
            row_count = 0
            data = csv.reader(file)
            for row in data:
                if row_count == 0:
                    row_count += 1
                else:
                    monthly_active += int(row[5])
        
        month.append(folder[3:6])
        active.append(monthly_active)

    return month, active, "Active Cases"
    

choices = {
    1 : confirmed_total,
    2 : deaths_total,
    3 : recovered_total,
    4 : active_total
}
