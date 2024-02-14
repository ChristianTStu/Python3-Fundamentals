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