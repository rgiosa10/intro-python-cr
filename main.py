# 1.) A function called list_sayer() that takes a list as an argument

list_1 = ["Hello", "world", 9, 3.14]
list_2 = []

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

print("Exercise 1:") # to help readability of outputs
true_or_false_check = list_sayer(list_1) # Run the function to see name of item and its index, and capture in variable to print Boolean output
print(true_or_false_check) # Print to see the correct return Boolean in output
true_or_false_check = list_sayer(list_2) # Run the function to see name of item and its index, and capture in variable to print Boolean output
print(true_or_false_check) # Print to see the correct return Boolean in output
print("__________________________________________________________________________") # to help readability of outputs

# 2.) A function called dict_sayer() that takes a dictionary as an argument

dict_1 = {
    "name": "Ruben",
    "age": 36,
    "dog's name": "Messi",
    }

dict_2 = {}

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


print("Exercise 2:") # to help readability of outputs
true_or_false_check_2 = dict_sayer(dict_1) # Run the function to see each key and respective value, and capture in variable to print Boolean output
print(true_or_false_check_2) # Print to see the correct return Boolean in output
true_or_false_check_2 = dict_sayer(dict_2) # Run the function to see each key and respective value, and capture in variable to print Boolean output
print(true_or_false_check_2) # Print to see the correct return Boolean in output
print("__________________________________________________________________________") # to help readability of outputs

# 3.) A function called greatest() that takes as an argument a dictionary that has strings as keys and integers as values

top_wc_winners = {
    "Argentina": 2,
    "Germany": 4,
    "Italy": 4, 
    "France": 2, 
    "Uruguay": 2, 
    "Brazil": 5,
    }

top_wc_winners_hope = {
    "Germany": 4,
    "Italy": 4, 
    "France": 2, 
    "Uruguay": 2, 
    "Brazil": 5,
    "Argentina": 5,
    }

def greatest(top_wc_winners):
    largest_value = 0
    largest_key = None
    container_list = [largest_value, largest_key]
    #check each key, value in dictionary
    for key, value in top_wc_winners.items():
        # find the greatest value in dictionary by comparing against index 0 of container_list
        if value > container_list[0]:
            container_list[0] = value
            container_list[1] = key

    # Counts how many iterances of the greatest value there are
    tied_top_counter = 0
    # Captures each key of the multiple instances of the greatest value
    tied_top_value = []
    
    # Counts if the greatest value occurs multiple times
    for value in top_wc_winners.values():
        if value == container_list[0]:
            tied_top_counter += 1
    
    # If there are multiple keys with the same greatest value it adds it to tied_top_value list
    if tied_top_counter > 1:
        for key, value in top_wc_winners.items():
            if value == container_list[0]:
                tied_top_value.append(key)
        # Sorts list alphabetically to pick greatest value key based on alphabetical order using first letter of the key
        tied_top_value.sort()
        # Add key based on alphabetical order as the greatest value key
        container_list[1] = tied_top_value[0]
  
    # return a tuple with the greatest value and its key
    return tuple(container_list)

print("Exercise 3:") # to help readability of outputs
print(greatest(top_wc_winners)) # print function in order to see return in output
print(greatest(top_wc_winners_hope)) # print function to see return if same greatest value based on alphabetical order
print("__________________________________________________________________________") # to help readability of outputs

# 4.) A function called zipper() that takes two lists as arguments

flavor_list_1 = ["vanilla", "cherry", "strawberry"]
flavor_list_2 = ["cake", "ice_cream", "pistachio"]
flavor_list_3 = ["chocolate"]

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

print("Exercise 4:") # to help readability of outputs
print(zipper(flavor_list_1, flavor_list_2)) # print function in order to see return in output
print(zipper(flavor_list_1, flavor_list_3)) # print function in order to see return in output

