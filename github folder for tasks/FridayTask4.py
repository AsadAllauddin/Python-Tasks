Task = "write a method which can create a multi die-mention array by getting number of values of first list and number of values for the associative list, display the list as value in table formate"
print(Task)
import random
rows = int(input("Enter the table rows: "))
columns = int(input("Enter the table columns: "))
for i in range(rows):
    for j in range(columns):
        a = random.randint(1, 9)
        print(a, end=" ")
    print(" ")