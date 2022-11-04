print("Exercise 1:") # to help readability of outputs

list_1 = ["Hello", "world", 9, 3.14]

def list_sayer(list_1):
    # If the list isn't empty (i.e. there's one or more items in it)
    if len(list_1) > 0:
        for index in range(len(list_1)):
            # print a string for each item saying the name of the item and its index
            print(f"The name of item is {list_1[index]} at index {index}")
        # return the Boolean True
        return True
    # If the list is empty
    else:
        # print a string saying that the list is empty
        print("The list is empty")
        # return the Boolean False
        return False

#list_sayer(list_1)
true_or_false_check = list_sayer(list_1) # Run the function to see name of item and its index, and capture in variable to print Boolean output
print(true_or_false_check) # Print to see the correct return Boolean in output

print("__________________________________________________________________________") # to help readability of outputs

print("Exercise 2:") # to help readability of outputs

dict_1 = {"name": "Ruben", "age": 36, "dog's name": "Messi"}

def dict_sayer(dict_1):
    # If the dictionary isn't empty (i.e. there's one or more items in it)
    if len(dict_1) > 0:
        # print a string for each item saying the name of each key and its value
        for key, value in dict_1.items():
            print(f"The name of key is '{key}' with a value '{value}'")
        # return the Boolean True
        return True
    # If the dictionary is empty
    else: 
        # print a string saying that the dictionary is empty
        print("The dictionary is empty")
        # return the Boolean False
        return False


#dict_sayer(dict_1)
true_or_false_check_2 = dict_sayer(dict_1) # Run the function to see each key and respective value, and capture in variable to print Boolean output
print(true_or_false_check_2) # Print to see the correct return Boolean in output

print("__________________________________________________________________________") # to help readability of outputs

print("Exercise 3:") # to help readability of outputs

top_wc_winners = {"Argentina": 2, "Brazil": 5, "Germany": 4, "Italy": 4, "France": 2, "Uruguay": 2}

def greatest(top_wc_winners):
    container_list = [0, None]
    #check each key, value in dictionary
    for key, value in top_wc_winners.items():
        # find the greatest value in dictionary by comparing against index 0 of container_list
        if value > container_list[0]:
            container_list[0] = value
            container_list[1] = key
    # return a tuple with the greatest value and its key
    return tuple(container_list)

print(greatest(top_wc_winners)) # print function in order to see return in output

print("__________________________________________________________________________") # to help readability of outputs

print("Exercise 4:") # to help readability of outputs

flavor_list_1 = ["vanilla", "cherry"]
flavor_list_2 = ["cake", "ice_cream", "pistachio"]

def zipper(flavor_list_1, flavor_list_2):
    same_len_output = {}
    diff_len_output_list = []

    # If the lists are the same length
    if len(flavor_list_1) == len(flavor_list_2):
        # Add each key and value to dictionary 
        for i in range(len(flavor_list_1)):
            same_len_output[flavor_list_1[i]] = flavor_list_2[i]
        # return a dictionary that uses items from first list as keys, and each item in the same index in the second list as the value
        return same_len_output
    # If the lists are different lengths
    elif len(flavor_list_1) != len(flavor_list_2):
        diff_len_output_list.append(flavor_list_1)
        diff_len_output_list.append(len(flavor_list_1))
        diff_len_output_list.append(flavor_list_2)
        diff_len_output_list.append(len(flavor_list_2))
        # return a tuple with each list and its length
        return tuple(diff_len_output_list)

print(zipper(flavor_list_1, flavor_list_2)) # print function in order to see return in output

