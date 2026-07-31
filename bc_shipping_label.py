def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    print()
    if "street" in kwargs or "city" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('city')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('city')} {kwargs.get('poboox')}")
    else:
        print("")

#I can only pass positional arguments before keyword argements. Will not work the other way around
shipping_label("Dr", "Spongebob", "III",
               street = "123 Fake street",
               city = "Lagos")