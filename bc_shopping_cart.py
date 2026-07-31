## Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("What food would you like to add to your cart? (Type 'q' when finished): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"What is the price of {food}?: $"))
        foods.append(food)
        prices.append(price)
print("---------- Your Cart ----------")
for food, price in zip(foods, prices):
    print(f"{food}: ${price:2f}")
for price in prices:
    total += price
print("-------------------------------")
print(f"Total: ${total:.2f}")    
    
'''
price = float(input(f"What is the price of {food}?: "))
foods.append(food)
prices.append(price)
total += price
'''