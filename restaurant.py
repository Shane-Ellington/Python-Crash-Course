# 9-1 Prompt 

class Restaurant:
    def __init__(self, name, type):
        #
        self.name = name
        self.type = type
    
    def describe_restaurant(self):
        print(f"This restaurant is called: {self.name}.")
        print(f"They are known as a {self.type} restaurant.")

    def open_restaurant(self):
        print(f"{self.name} is currently open!")

my_resturant = Restaurant('Shane\'s Italian Grill', 'Italian')
jims_resturant = Restaurant("Jim's", "Americana")
labrisa_resturant = Restaurant("La Brisa Mexican Restaurant", "Mexican")

my_resturant.describe_restaurant()
my_resturant.open_restaurant() 

jims_resturant.describe_restaurant()
jims_resturant.open_restaurant()

labrisa_resturant.describe_restaurant()
labrisa_resturant.open_restaurant()