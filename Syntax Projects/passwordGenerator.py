import random

# Total database is 58 items
items_database = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','!','@','#','$','%','&']
passwordNumber_list = []
passwordItem_list = []
completed_password = ''


print('Welcome to the Password Generator 9000')
print('Would you like to know more?')
initial_response = input('Yes or No:')

if initial_response =='':
    print('No input provided, please restart the program.')

    exit()

elif initial_response.lower() =='yes':
    pass

elif initial_response.lower() =='no':
    print('Well okay! Please restart the program if you would like to use me later!')

    exit()

else:
    print('Not a vaild response, please restart the program.')

    exit()


# 'Yes' response

while initial_response.lower() == 'yes':
    
    print('Fabulous! Let us begin.')

    num_of_items = int(input('Please enter the number of items in your password. Please choose a number betweeen 12-18:'))

    for item in range(num_of_items):
        passwordNumber_list.append(random.randint(0,57))
    
    for num in passwordNumber_list:
        passwordItem_list.append(items_database[num])

    for x in passwordItem_list:
        completed_password = completed_password+ x

    break

print(f'Here is your completed password:{completed_password}')



