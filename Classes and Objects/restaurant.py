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