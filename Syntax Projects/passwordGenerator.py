import random

# Total database is 32 items
items_database = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','!','@','#','$','%','&']
passwordNumber_list = []
passwordItem_list = []


print('Welcome to the Password Generator 9000')
print('Would you like to know more?')
initial_response = input('Yes or No:')


# 'Yes' response

while initial_response == 'Yes':
    
    print('Fabulous! Let us begin.')

    num_of_items = int(input('Please enter the number of items in your password. Please choose a number betweeen 12-18:'))

    for item in range(num_of_items):
        passwordNumber_list.append(random.randint(0,32))
    
    for num in passwordNumber_list:
        passwordItem_list.append(items_database.index(num))
        print(passwordItem_list)

















# 'No' response
    
while initial_response == 'No':
    print('Well okay, restart the program if you decide you need my help.')

    exit()

if initial_response =='':
    print('No input provided, please restart the program.')
else:
    print('Not a vaild response, please restart the program.')

    exit()



