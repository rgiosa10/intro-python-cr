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
true_or_false_check = list_sayer(list_1)
print(true_or_false_check)

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
true_or_false_check_2 = dict_sayer(dict_1)
print(true_or_false_check_2)

#__________________________________________________________________________

# Exercise number 3:

top_wc_winners = {"Argentina": 2, "Brazil": 5, "Germany": 4, "Italy": 4, "France": 2, "Uruguay": 2}

def greatest(top_wc_winners):
    container_list = [0, None]
    for key, value in top_wc_winners.items():
        if value > container_list[0]: 
            container_list[0] = value
            container_list[1] = key
    return tuple(container_list)

print(greatest(top_wc_winners))


