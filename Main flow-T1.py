#Creating a List
my_list=['apple','orange','grape','gauva']

#Adding an elementto the list
my_list.append('kiwi')

#Removing an element from the list
my_list.remove('grape')

#modifying an elememt in the list
my_list[0]='banana'

print("Updated list:",my_list)

#Creatimg a dictionary
my_dict={'name':'John','age':25,'city': 'Dehli' }

#Adding an element
my_dict['gender']='Male'

#Removing
del my_dict['age']

#Modifying
my_dict['city']='Mumbai'

print("Updated Dictionary:",my_dict)

#Creating a Set
my_set={1,2,3,4,5}

#Adding 
my_set.add(6)

#Removing
my_set.remove(3)

#Modifying
my_set.discard(1)
my_set.add(10)

print("Upadated Set:",my_set)
