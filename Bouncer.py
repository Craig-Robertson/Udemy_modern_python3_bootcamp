#Ask for age
age = input("How old are you?: ")

##Explicit exclusion for null values entered
#if age != "":

##Null is false so this works with truthy ness
#if age: 
    ##set age = to int since we get it from string enter
#    age = int(age) 
#    if age >= 18 and age < 21:
#        print("you can enter, but need a wristband!")
#    elif age >= 21:
#        print("You are old enough to enter and can drink!")
#    else:
#        print("You are too young to enter!")
#else:
#    print("Please enter an age!")


##more efficient setup
if age: 

    age = int(age) 
    if age >= 21:
        print("You are old enough to enter and can drink!")
    elif age >= 18:
        print("you can enter, but need a wristband!")
    else:
        print("You are too young to enter!")
else:
    print("Please enter an age!")