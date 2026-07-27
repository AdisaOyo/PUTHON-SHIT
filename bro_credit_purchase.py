access = "1234-5678-9012-3456"
cr_num_input = input ("What is your credit card number?: ")
cr_num = cr_num_input
is_digit = cr_num.isdigit()
display_cr = (cr_num[:4]+"-") + (cr_num[4:8]+"-") + (cr_num[8:12]+"-") + (cr_num[12:16])
cr_len = len(cr_num)

print(display_cr)
while is_digit != True or len(cr_num_input) != 16 or display_cr != access:
        print("Invalid card number")
        #update inputs and variables here
        cr_num_input = input("Invalid card number! Reenter: ")
        cr_num = cr_num_input
        is_digit = cr_num.isdigit()
        display_cr = (cr_num[:4]+"-") + (cr_num[4:8]+"-") + (cr_num[8:12]+"-") + (cr_num[12:16])
        #update input data here
        print(display_cr)
else:
      print(f"XXXX-XXXX-XXXX-{cr_num[-4:]}")


## when using while statement always re enter variables needed for reevaluation. I know there is a leaner way of doing this and I will find it inshallah or make it myself lol
#you also dont need else statemen when using while statement but it does not hurt
## I can use if statement inside while!!!!! This opens up so much!!!!!