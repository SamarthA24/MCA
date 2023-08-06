'''Create a LIST with your domain attributes, insert the elements using the append (), insert(), extend()'''
hospitalst = [1001,"Appollo","Hospital","Bangalore","Karnataka",560026]
print("\nThe original List: ",hospitalst)
hospitalst.append("Dr.Nirmal")
print("\nList after Append method: ",hospitalst)
hospitalst.insert(2,"Antony")
print("\nlist After Insert Method: ",hospitalst)
hospitalst.extend(["Nurse","staff"])
print("\nList After Extend Method",hospitalst)

'''Adding the iterables tuple and dictionary'''
hospitallst = [("Nimans","Near christ"),(1023,"hospital id"),{1:"HospitalName",2:"Kims"}]
print("\nList after adding Tuples, Sets and Dictionary to list: ",hospitallst)

'''swaping the elements of list'''
hospitalst = [1001,"Appollo","Hospital","Bangalore","Karnataka",560026,"Dr.Nirmal","Nurse","staff"]
hospitalst[3], hospitalst[-2] = hospitalst[-2], hospitalst[3]
print("\nThe swaped list is: ",hospitalst)

'''find the sum of the digits in a list'''
list1 = [11, 5, 17, 18, 23]
sum = 0
for ele in range(0, len(list1)):
    sum = sum + list1[ele]
print("\nSum of all elements in given list: ", sum)

'''find the smallest element in a list'''
list1 = [11, 5, 17, 18, 23]
print("\nthe minimum value is",min(list1))

#dictionary 
'''creating the dictionary'''
hospitalst = {1:1001,2:"Appollo",3:"Hospital",4:"Bangalore",5:"Karnataka",6:560026}
print("Original Dictionary: ",hospitalst)

'''Sort the dictionaries in ascending order based on the Key of the dictionary'''
hospitalst = {1:1001,4:"Appollo",6:"Hospital",2:"Bangalore",7:"Karnataka",5:560026}
print("\nBefore Sorting: ",hospitalst)
myKeys = list(hospitalst.keys())
myKeys.sort()
sorted_dict = {i: hospitalst[i] for i in myKeys}
print("\nAfter Sorting: ",sorted_dict)

'''Create the dictionary with Numeric as Value in Key – Value pair and find the sum of all the values in the Dictionary'''
dictnory = {'a':10,'b':20,'c':30,'d':40,'e':50,'f':60}
sum = 0
for key in dictnory:
    sum = sum + dictnory[key]
print("\nOriginal Dictionary: ",dictnory)
print("\nSum of All the elements: ",sum)


'''demonstrate the sorting in descending order of values with lambda function'''
dict1 = {'hospitalname':2,'hospitalid':4,'doctorid':1,'doctorname':3,'staffid':5}
print("\nthe original dictionary: ",dict1)
sorted_dict = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
print("\nSorted dictionary is: ",sorted_dict)
