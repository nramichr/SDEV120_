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