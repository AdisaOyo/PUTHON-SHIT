import time
my_time = input("Enter the time in seconds: ")
is_int = my_time.isdecimal()
is_alpha = my_time.isalpha()
while True:
    if is_int == False or is_alpha == True:
        my_time = input("Invalid input! Re-enter!: ")
        is_int = my_time.isdecimal()
        is_alpha = my_time.isalpha()
    elif is_int == True and is_alpha == False:
        for x in range(int(my_time),0,-1):
            seconds = x % 60
            minutes = int(x/60) % 60
            hours = int(x/3600) % 60
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            time.sleep(1)
        break

print("TIME'S UP!!!")
'''
USED THIS TO CHECK AND MAKE SURE I CAN LOOP PROPERLY BECAUSE OF USER INPUT


my_time = input ("How long do I wait?: ")
is_int = my_time.isdecimal()
is_alpha = my_time.isalpha()


while True:
    if is_int == False or is_alpha == True:
        my_time = input("Invalid input! Re-enter!: ")
        is_int = my_time.isdecimal()
        is_alpha = my_time.isalpha()
    elif is_int == True and is_alpha == False:
        for x in range(int(my_time),0,-1):
            print(x)
            time.sleep(1)
        for x in range(0,int(my_time)):
            print(x)
            time.sleep(1)
        print("WAKE UP!!!")
        break
    else:
        break

'''
#print(is_int)