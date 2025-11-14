class pizza:
    def __init__(self, size, crustType, toppings = None):
        self.size = size
        self.crustType = crustType
        self.toppings = toppings if toppings else []
        
    def addTopping(self, topping):
        self.toppings.append(topping)
        
    def removeTopping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)
        else:
            print(f'{topping} is not on your pizza')
            
    def describePizza(self):
        print(f'\n 🍕  YOUR PIZZAAA  🍕')        
        print(f'Size: {self.size.title()}')
        print(f'Crust: {self.crustType.title()}')
        if self.toppings:
            print("Toppings")
            for topping in self.toppings:
                print(f'- {topping.title()}')
        else:
            print("No Toppings added yet")
            
myPizaa = pizza("large", "thin")
myPizaa.addTopping("Mushrooms")
myPizaa.addTopping("Caramelised Onions")
myPizaa.addTopping("Goat Cheese")
myPizaa.addTopping("Chicken")
myPizaa.addTopping("Chili Flakes")
myPizaa.describePizza()
myPizaa.removeTopping("Chicken")
myPizaa.describePizza()

