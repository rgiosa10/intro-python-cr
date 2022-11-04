# Exercise number 1:

list_1 = ["hello", "world", 9]

def list_sayer(list_1):
    if len(list_1) > 0:
        for index in range(len(list_1)):
            print(f"The name of item is {list_1[index]} at index {index}")
        return True
    else: 
        print("The list is empty")
        return False

list_sayer(list_1)

# Exercise number 2:


