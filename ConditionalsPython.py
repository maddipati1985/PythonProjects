gender=input("Enter your Gender: M")
print('Gender Value from input:',gender)
age=input("ENTER your age:")

# if  gender=='M':
#     print("You are Male")
# elif gender=='F':
#     print("Female")
# else:
#     print("Nor Male or Female")


if gender == 'M':
    age=input('Enter your age')
    if int(age)<=40:
        print("Welcome Young Man")
    else:
        print("Welcome Middle aged Man")
else :
    print('welcome')