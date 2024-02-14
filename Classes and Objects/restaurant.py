class Resturant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_resturant(self):
        print(f'{self.name} serves {self.cuisine_type} type food.')

    def open_resturant(self):
        print(f'{self.name} is open for business!')

new_resturant = Resturant('FlameOn Habachi', 'Asian Fusion')
new_resturant.describe_resturant()
new_resturant.open_resturant()

old_resturant = Resturant('Total Noodle', 'Pasta')
old_resturant.describe_resturant()
old_resturant.open_resturant()

your_resturant = Resturant('Bagger Daves', 'Burger')
your_resturant.describe_resturant()
your_resturant.open_resturant()

class User:

    def __init__(self, first_name, last_name, age, geolocation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.geolocation = geolocation

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} is {self.age} years old and lives in {self.geolocation}.')

    def greet_user(self):
        print(f'Welcome {self.first_name}! Would you like to play a game?')

christian = User('Christian', 'Stuart', 26, 'North America')
jon = User('Jon', 'Noel', 28, 'Australia')
bobby = User('Robert', 'Wilkens', 24, 'England')

christian.describe_user()
christian.greet_user()