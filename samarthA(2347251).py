''' Write a paragraph about introducing you and your selected domain (include Full Name, domain name, register number, year …….). Write a python program to count the frequency of any specific word (in your domain) in the paragraph.'''
hospitalmanage = "Myself Samarth A, I have Choosed Hospital Management System, 2347251, 2023"
'''Convert the paragraph to lowercase to make the search case-insensitive'''
hospitalmanage_lower = hospitalmanage.lower()
'''define the word to be counted'''
word_to_count = "hospital"
'''Split the paragraph into words'''
words =hospitalmanage_lower.split()
'''initialize a variable to store the count'''
word_count = 0
'''loop through the words and count the occurrences of the specific word'''
for word in words:
    if word == word_to_count:
        word_count += 1
print("The number of times word repeated is: ",word_count)

#program to display all the datatypes of selected specific elements in the paragraph.
def get_data_types_in_list(input_list):
    # Create an empty set to store the data types of elements in the list
    data_types = set()
    # # Iterating through each element in the input_list through each element item in the input_list
    for item in input_list:
        '''The type() function returns the type of an object as a class object. The __name__ attribute of the class object gives the name of the type as a string.'''
        data_types.add(type(item).__name__)
    return data_types
hospital_lst = ["Myself Samarth A, I have Choosed Hospital Management System, 2347251, 2023",{1:"Doctorid, 2:doctorname"},("doctorname","doctorid")]
# Calling the get_data_types_in_list function
result = get_data_types_in_list(hospital_lst)
print(result)

'''Write a python program to count the number of alphabets, numeric and other special symbols in the paragraph'''
alpha = 0
hospitalmanage = "fortiesbangalore1234567"
for i in hospitalmanage:
    if (i.isalpha()):
        alpha +=1
print("Number of Digits: ",len(hospitalmanage)-alpha)
print("Number of Alphabets is: ",alpha)

#creating a set
hospital = {"hospitals","hospitalname","Fortis","Medicine","doctorname","doctorid","nurseid","nursename","staffid","staffid","patientid","patientname",76.65,75000.00,90,1001,1002,True,False}
print(hospital)
'''remove method
performing the remove() so that we can remove the elements in set that we are desired to remove the from the set'''
hospital.remove("Fortis")
print("After removing the elements from set:",hospital)
'''performing pop() operation where it will remove the elements of set randomly'''
hospital.pop()
print("After pop elements from set:",hospital)
'''discard method
performing the discard() it works same as remove()'''
hospital.discard("hospitalname")
print("After discard elements from set: ",hospital)
'''clear method 
performing the clear() so it works i sense that it will remove element from set and make set as empty'''
hospital.clear()
print("After removing the elements from set:",hospital)

'''Update() Updating the set by merging the two sets by using update() so that it is easy for merging two sets in one set'''
hospital = {"hospitals","hospitalname","Fortis","Medicine","doctorname","doctorid","nurseid","nursename","staffid","staffid","patientid","patientname",76.65,75000.00,90,1001,1002,True,False}
hospital1={"departments","Ambulance","Lab Technician", "Receptionist","Nurse"}
hospital.update(hospital1)
print(hospital)

# Define a set
hospital_set = {"hospitalname", "hospitalid", "Doctorname", "doctorid", "nurseid"}
# Sorting the set and convert it to a list
sorted_list = sorted(hospital_set,reverse=True)
print(sorted_list)

#tuple
'''creating a tuple with packing tuple values'''
hospitaltuple=(10000,"Fortis","Bangalore","Dr.Nirmal","Antony")
'''creating a tuple with unpacking tuple values'''
(id,hospitalname,place,doctorname,nursename) = hospitaltuple
'''printing the values of unpacking tuple values'''
print(id)
print(hospitalname)
print(place)
print(doctorname)
print(nursename)

'''counting the characters that are repeated'''
hospitaltuple1=("f","o","r","t","i","s","b","a","n","g","a","l","u","r","u")
char_count = {}
'''Looping through the hospitaltuple1 and count the characters that are repeated'''
for char in hospitaltuple1:
    char_count[char] = char_count.get(char, 0) + 1
'''Printing the characters repeated characters count'''
for char, count in char_count.items():
    print(f"count of '{char}' = {count}")
'''slicing the index of the hospitaltuple1 using the seperate word format'''
hospitaltuple1=("f","o","r","t","i","s","b","a","n","g","a","l","u","r","u","D","r","N","i","r","m","a","l")
print(hospitaltuple1[0:1])
print(hospitaltuple1[:10])
print(hospitaltuple1[5:9])
print(hospitaltuple1[8:])
print(hospitaltuple1[-1::-10])
print(hospitaltuple1[-5::-7])
'''slicing the index of the hospitaltuple1 in the word format '''
hospitaltuple1=("fortis","bangalore","Dr.Nirmal","Antonny")
print(hospitaltuple1[0:4])
print(hospitaltuple1[0:])
print(hospitaltuple1[:5])
print(hospitaltuple1[0:5])
print(hospitaltuple1[::-4])
print(hospitaltuple1[::-1])



