class Car:
    #condtructor
    def __init__(self, model, year, colour, for_sale): #__init__ is to initialise. 'def __init__(self):' is a constructor method needed to construct objects
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale
# use __init__ when setting up attributes (variables). __init__ is not used for methods (functions), you can omit it 
    def drive(self):
        print(f"You drive the {self.model}")
    def stop(self):
        print(f"You stop the {self.model}")
    def describe(self):
        print(f"{self.year} {self.colour} {self.model}")