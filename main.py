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

#__________________________________________________________________________

# Exercise number 2:

dict_1 = {"name": "Ruben", "age": 36, "dog's name": "Messi"}

def dict_sayer(dict_1):
    if len(dict_1) > 0:
        for key, value in dict_1.items():
            print(f"The name of key is '{key}' with a value '{value}'")
        return True
    else: 
        print("The dictionary is empty")
        return False


dict_sayer(dict_1)

#__________________________________________________________________________

# Exercise number 3:

