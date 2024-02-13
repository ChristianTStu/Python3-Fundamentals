
print('Welcome to the Password Generator 9000')
print('Would you like to know more?')
initial_response = input('Yes or No:')

if initial_response == 'Yes':
    print('Fabulous! Let us begin.')
elif initial_response == 'No':
    print('Well okay, restart the program if you decide you need my help.')\
    
    exit()
elif initial_response =='':
    print('No input provided')
else:
    print('Not a vaild response, please restart the program.')

num_of_items = input()