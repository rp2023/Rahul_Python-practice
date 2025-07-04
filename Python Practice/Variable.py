#variables in python

first_name = 'Rahul'
last_name = 'Patil'
country = 'India'
city = 'Jalgaon'
age = 31
is_married = True
skills = ['HTML', 'Linux','AWS','Ansible','Github','Jenkins cicd','python']
person_info = {
    'first_name':'Rahul',
    'lastname':'Patil',
    'country':'India',
    'city':'Jalgaon'
}
#Printing the values stored in the  variable

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name:', last_name)
print('Last name length:', len(last_name))
print('Country:', country)
print('Age:', age)
print('Married:', is_married)
print('Skills:', skills)
print('Person information:', person_info)

#Declaring multiple variable in one line

first_name, last_name, country, age, is_married = 'Rahul', 'Patil', 'India', '31', 'True'

print(first_name, last_name, country, age, is_married )
print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('Age:', age)
print('Married:', is_married)
