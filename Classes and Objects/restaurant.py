class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.customer_count = 0

    def describe_restaurant(self):
        print(f'{self.name} serves {self.cuisine_type} type food.')

    def open_restaurant(self):
        print(f'{self.name} is open for business!')
    
    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

    def display_number_served(self):
        print(f'This restaurant has served {self.number_served} customers.')


class User:

    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f'User: {self.first_name} {self.last_name}')
        print(f'Username: {self.username}')
        print(f'Email: {self.email}')

    def greet_user(self):
        print(f'Welcome {self.first_name}! Would you like to play a game?')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# Testing Restaurant class
restaurant = Restaurant('FlameOn Habachi', 'Asian Fusion')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Setting and displaying number served
restaurant.set_number_served(50)
restaurant.display_number_served()

# Incrementing number served and displaying again
restaurant.increment_number_served(20)
restaurant.display_number_served()

# Testing User class
user = User('John', 'Doe', 'johndoe', 'john@example.com')

# Incrementing login attempts
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Displaying login attempts
print(f'Login attempts: {user.login_attempts}')

# Resetting login attempts
user.reset_login_attempts()

# Displaying login attempts after reset
print(f'Login attempts after reset: {user.login_attempts}')
