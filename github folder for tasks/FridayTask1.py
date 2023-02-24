Task = "Write a method with take key, value from the user and add that value in the list.. if key is already filled should return message to user to chose another key. length of list will be 10"
print(Task)

def add_key_value(key_list, value_list):
    if len(key_list) >= 10:
        print("The key list full, can't add more keys.")
        return
    key = input("enter a key: ")

    if key in key_list:
        print("The key is already in the list. Please choose another key.")
        return

    value = input("Enter a value: ")

    key_list.append(key)
    value_list.append(value)
    print("Key-value pair added successfully.")

key_list=[]
value_list=[]

while len(key_list) < 10:
    add_key_value(key_list,value_list)
    for i in range(len(key_list)):
        print(f"{key_list[i]}:{value_list[i]}")