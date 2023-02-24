Task = "Write a method with fixed length of list 5. if user enter more then 5th value in the list bottom value should be removed and new value should be added at the top of list."
print(Task)


def add_to_list(my_list):

    if len(my_list) == 5:
        my_list.pop(4)


    new_value = input("Enter a new value: ")


    my_list.insert(0, new_value)



my_list = []

while True:
    add_to_list(my_list)
    print(my_list)
