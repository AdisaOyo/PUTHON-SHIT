## Principal interest calc

principal = 0
rate = 0
time = 0
"""
while principal <= 0:
    principal = float(
        input ("What is your principal amount?: ")
        )
    if principal <= 0:
        print("Principal can't be less than or equal to zero")
while rate <= 0:
    rate = float(
        input ("What is your interest rate?: ")
        )
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")
while time <= 0 or not time.is_integer():
    time = float(
         input ("What is your time in years?: ")
         )
    if time <= 0:
        print("Time can't be less than or equal to zero! Reenter!")
    elif not time.is_integer():
        print ("Time can't be a decimal! Re-enter!")

total = principal * pow((1 + rate/100), time)
print (f"Balance afer {time} year/s: ${total:.2f}")
#my_total = principal * pow((1 + (rate/100)), time)
#print (f"{principal:.2f}")
#print (f"{rate:.2f}")
#print (round(time))
#print (total)
"""
## using else statement with ehile True statement is versitile. e.g

while True:
    principal = float(
        input ("What is your principal amount?: ")
        )
    if principal < 0:
        print("Principal can't be less than zero")
    else: break
while True:
    rate = float(
        input ("What is your interest rate?: ")
        )
    if rate < 0:
        print("Interest rate can't be less than zero")
    else: break
while True:
    time = float(
         input ("What is your time in years?: ")
         )
    if time < 0 or not time.is_integer():
        print("Time can't be less than zero! Reenter!")
    elif not time.is_integer():
        print ("Time can't be a decimal! Re-enter!")
    else: break

total = principal * pow((1 + rate/100), time)
print (f"Balance afer {time} year/s: ${total:.2f}")