# Python weigth converter

weight = float(
    input("What is your weight?: ")
)
unit = input("What unit is this measured in? [Kg or Lbs]: ")

if unit == "Kg":
    weight = round(
        weight * 2.205, 2
    )
    print(f"Your weight is {weight}Lbs")
elif unit == "Lbs":
    weight = round(
        weight/2.205, 2
    )
    print(f"Your weight is {weight}Kg")
else: print(f"{unit} was not valid")

