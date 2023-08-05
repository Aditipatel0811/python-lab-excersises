
a = ''' 
Name- Aditi Patel
Register number- 2347204
class&section- 1st MCA 'B' 2023-25
domain Name- Airline Management
                                              Airline management
Airline  management is the administration of airlines.It includes the activities of setting the strategy of airports to
gather and provide information on airline commercial and operational priorities.It covers a broad overview of the airline management. It is also 
studied as a branch of study that teaches management of airport and airlines.This provides a broad overview of the airline industry and creates 
awareness of the underlying marketing, financial, operational, and other factors influencing airline management.This study provides information 
on airline commercial and operational priorities,along with teaching the key characteristics of aircraft selection and the impact of airport decision-making.

Aviation trends
The global airline industry continues to grow rapidly, but consistent and robust profitability is elusive. Measured by revenue, the industry 
has doubled over the past decade, from US$369 billion in 2004 to a projected $746 billion in 2014, according to the International Air Transport 
Association (IATA).Much of the growth of aviation has been driven by low-cost carriers (LCCs), which now control some 25 percent of the worldwide
market and have been expanding operations rapidly in emerging markets; growth also came from continued gains by carriers in developed markets, 
the IATA reported. Yet profit margins are still low, at less than 3 percent overall.In the commercial aviation sector, just about every group 
in the aviation industry chain—airports, airplane manufacturers, jet engine makers, travel agents, and service companies, to name a few—turns 
a profit. However, airline companies whose primary focus is on passenger flights have great difficulty making a profit.This is due to the complex 
nature of the business, manifested in part by the significant degree of regulation (which minimizes consolidation), and the vulnerability of 
airlines to outside events that happen regularly, such as security concerns and volcanic eruptions. Ongoing price pressure is also a factor; 
the airline industry is one of the few sectors that has seen prices fall for decades. Since the 1950s, airline fares (defined as the average 
fare paid by a passenger per kilometer) have consistently dropped.Given these circumstances, airlines must continue to focus on top-line growth 
because their limited profitability depends almost solely on revenue gains. They must also increase productivity in order to shore up and perhaps 
even increase margins. The way individual commercial airlines react to and navigate several trends playing out across the globe will determine 
carrier performance in the coming years.
'''
print(a) 
# Write a python program to count the frequency of any specific word
text = (a)
words = []
words = text.split()
wfreq=[words.count(w) for w in words]
print(dict(zip(words,wfreq)))

#Write a python program to display all the datatypes of selected specific element in the paragraph.

str1 = "aditi patel"
print(str1, 'is of type', type(str1))
num1 = 5
print(num1, 'is of type', type(num1))
num2 = 2.0
print(num2, 'is of type', type(num2))
num3 = 1+2j
print(num3, 'is of type', type(num3))

student_id = {112, 114, 116, 118, 115}
print(student_id,'is of type',type(student_id))

#Write a python program to count the number of alphabets, numeric and other special symbols in the paragraph.

para = '''The global airline industry continues to grow rapidly, but consistent and robust profitability is elusive. Measured by revenue, the industry has doubled over the past decade, from US$369 billion in 2004 to a projected $746 billion in 2014, according to the International Air Transport Association (IATA).'''
alphabets = digits = special = 0

for i in range(len(para)):
    if(para[i].isalpha()):
        alphabets = alphabets + 1
    elif(para[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
print('\npara is---',para)       
print("Total Number of Alphabets in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", special)

#	Create a Set with elements that consists of various data types (int, float, string, Boolean, etc. from your domain) and perform the functions pop(), clear(), discard() and del. Write the insights as docstring.

def Remove(sets):
    sets.discard(25)
    print (sets)
     
# Driver Code
sets = set(["Flight", 15.9, 25, True, False])
Remove(sets)

sets.pop()
print(sets)

sets.clear()
print(sets)

del sets

"""
    Performs various set operations: pop(), clear(), discard(), del.

    pop() - You can remove the item at the specified position and get its value with pop(). The index starts at 0
    clear() - You can remove all items from a list with clear(), making it empty.
    discard() - Removes a specific element from the set if it exists, otherwise does nothing.
    del - you can remove elements from a list using the del statement.Specify the item to be deleted by index. The first index is 0, and the last is -1.
"""    

#Update the Set with minimum 5 string attributes of your domain and arrange the Set in descending order.

sets = set(["Flight", 15.9, 25, True, False])

sets.update(["Flight276", "Passenger", "Ticket", "Reservation", "Crew"])

sorted_set = sorted(map(str, sets), reverse=True)
print("Updated Set:", sets)
print("Sorted Set:", sorted_set)

"""
The sorted() function returns a sorted list of the specified iterable object.
You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.
The reverse=True parameter specifies that the sorting should be done in descending order.
"""

#Create a Tuple and Execute the packing and unpacking operations of tuples using the attributes of your domain.

passenger_info = ("Aditi Patel", "5", "20A", "04-08-2023")

name, gate_number, seat_number, departure_date = passenger_info

# Printing the unpacked values
print("Passenger Name:", name)
print("Gate Number:", gate_number)
print("Seat Number:", seat_number)
print("Departure Date:", departure_date)

"""
The packing operation takes multiple values and packs them into a single tuple.
The unpacking operation takes a tuple and unpacks it into multiple values.
"""

# Count Numbers
my_tuple = ("A", "i", "r", "l", "i", "n", "e", "M", "a", "n", "a", "g", "e", "m", "e", "n", "t")
count = my_tuple.count("r")
print("Occurrences of 'r':", count)

# Slicing and negative indexing
second_last_character = my_tuple[-2]
last_three_characters = my_tuple[-3:]
reversed_tuple = my_tuple[::-1]
first_three_characters = my_tuple[:3]
middle_four_characters = my_tuple[6:10]

print("Second Last Character:", second_last_character)
print("Last Three Characters:", last_three_characters)
print("Reversed Tuple:", reversed_tuple)
print("First Three Characters:", first_three_characters)
print("Middle Four Characters:", middle_four_characters)

"""
The slicing operation takes a start index and an end index, and returns a substring of the string.
The start index can be negative, which means that it counts from the end of the string.
The end index can be omitted, which means that the slicing operation will go to the end of the string.
"""



      

     