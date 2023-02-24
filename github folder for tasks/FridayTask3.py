Task ='write a method with list of random numbers, when user add new value method will check if the value already exist in list return message value already in the list other wise add the value in the list and display back the list till that value.'
print(Task)


def add_to_list(new_value, my_list):

    if new_value in my_list:
        print("Value already exists in the list")
        return


    my_list.append(new_value)


    new_index = my_list.index(new_value)
    print(my_list[:new_index + 1])



my_list = []

while len(my_list) < 5:
    new_value = int(input("Enter a value to add to the list: "))
    add_to_list(new_value, my_list)
