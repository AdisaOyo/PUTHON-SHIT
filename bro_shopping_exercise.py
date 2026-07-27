print (' """CODE TO CALCULATE SHOPPING""" ')

item = input( "What do you want to buy? " )
price = float(
    input( "The price is? " )
)
quantity = int(
    input( "How many will you be buying? " )
)

print (f"You are buying {quantity} x {item}")
price = round (price*quantity,2)
print (f"It costs ${price}")