#Single lists for different meals throughout the day

breakfast = ['Egg Sandwich', 'Bagel', 'Coffee']
lunch = ['BLT', 'PB&J', 'Turkey Sandwich']
dinner = ['Soup', 'Salad', 'Spaghetti', 'Taco']

#One big list that contains all meals

menus = [['Egg Sandwich', 'Bagel', 'Coffee'],
         ['BLT', 'PB&J', 'Turkey Sandwich'],
         ['Soup', 'Salad', 'Spaghetti', 'Taco'] ]

print('Breakfast Menu:\t', menus[0])
print('Lunch Menu:\t', menus[1])
print('Dinner Menu:\t', menus[2])

#Lets grab the Bagel item from the first list

print(menus[0][1])

#Lets put this all into a Dictionary of Lists

menus_dictionary = {'Breakfast' : ['Egg Sandwich', 'Bagel', 'Coffee'],
                    'Lunch' : ['BLT', 'PB&J', 'Turkey Sandwich'],
                    'Dinner' : ['Soup', 'Salad', 'Spaghetti', 'Taco']}

print('Breakfast Menu:\t', menus_dictionary['Breakfast'])
print('Lunch Menu:\t', menus_dictionary['Lunch'])
print('Dinner Menu:\t', menus_dictionary['Dinner'])

# Is there a better way to do this without having to manually type each line out?

menus_dictionary_forLoop = {'Breakfast' : ['Egg Sandwich', 'Bagel', 'Coffee'],
                            'Lunch' : ['BLT', 'PB&J', 'Turkey Sandwich'],
                            'Dinner' : ['Soup', 'Salad', 'Spaghetti', 'Taco'] }

for name, menus_dictionary_forLoop in menus_dictionary_forLoop.items():
    print(f'{name} : {menus_dictionary_forLoop}')