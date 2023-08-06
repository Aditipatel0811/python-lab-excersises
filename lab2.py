def list_example():

    my_list = []

    my_list.append("12345")          
    my_list.append("Ritu")              
    my_list.append("ullu")               
    my_list.append("password")  
    my_list.append("Admin")             
    my_list.append("9876543210")        
    my_list.append(30)                 
    my_list.append("aditi.patel@gmail.com")
    my_list.append("Female")             

    print("List:", my_list)

    
    my_list.insert(5, "Aditi Patel")       
    my_list.insert(8, "Hello")         

    print("List:", my_list)

    dic = {
        'address': '123 Main Rd',
        'city': 'New Delhi',
        'zipcode': '110001'
    }

    my_list.extend(['INDIA', 'User'])     
    my_list.extend(list(dic.keys()))   

    print("List:", my_list)

if __name__ == "__main__":
    list_example()



# Create a list with numeric and perform the following operations.
#     Write a program to swap the first and last elements in a list.
#     Write a program to find the sum of the digits in a list.
#     Write a program to find the smallest element in a list


my_list = [13, 2, 63, 46, 59]


first_element = my_list[0]
last_element = my_list[-1]
my_list[0] = last_element
my_list[-1] = first_element
print(my_list)


def sum_of_digits(list_of_numbers):
  sum_of_digits = 0
  for number in list_of_numbers:
    sum_of_digits += number
  return sum_of_digits

print(sum_of_digits(my_list))


def smallest_element(list_of_numbers):
  smallest_element = list_of_numbers[0]
  for number in list_of_numbers:
    if number < smallest_element:
      smallest_element = number
  return smallest_element

print(smallest_element(my_list))




# Sort the dictionaries in ascending order based on the Key of the dictionary.
#  Create the dictionary with Numeric as Value in Key – Value pair and find the sum of all the values in the Dictionary.
#  Write a Python code to demonstrate the sorting in descending order of values with lambda function



my_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
sorted_dict = sorted(my_dict.items(), key=lambda x: x[0])
print("Dictionary sorted in ascending order based on keys:", sorted_dict)


my_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}

sum_of_values = sum(my_dict.values())
print(" Sum of all values in the dictionary:", sum_of_values)



my_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
sorted_dict_descending = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_dict_descending)