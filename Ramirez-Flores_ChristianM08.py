# Program Name: Ramirez-Flores_Christian_M08
#Author: Christian Ramirez-Flores
#Date: December 14, 2025
#Version: 4.0
#Summary: This program collects employee names and salaries, calculates the average salary, and displays employees whose salaries are within $5000 of the average.
#Variables:
# names (list)
# salaries (list)
# total (float)
# name (string)
# salary (float)
# avg (float)
# diff (float)


names = []
salaries = []
total = 0

name = input("Enter employee name or quit to stop: ")
while name.lower() != "quit":
    salary = float(input("Enter employee salary: "))
    names.append(name)
    salaries.append(salary)
    total = total + salary
    name = input("Enter employee name or quit to stop: ")

if len(salaries) == 0:
    print("No employees were entered.")
else:
    avg = total/len(salaries)
    
    print("\nAll Employees:")
    for i in range (len(names)):
        print("Name:", names[i])
        print("Salary:", salaries[i])

    print("\Average Salary:")
    print(avg)

    print("\nEmployees within 5000 of the average:")
    for i in range(len(names)):
        diff = salaries[i] - avg
        if diff <= 5000 and diff >= -5000:
            print("Name:", names[i])
            print("Salary:", salaries[i])