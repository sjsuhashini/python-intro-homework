try:
    
    userAge = int(input("Enter your age: "))

    if userAge>=0 and userAge<=12:
        category= "Child"
        
    elif userAge>12 and userAge<=17:
        category= "Teen"

    elif userAge>18 and userAge<=64:
        category= "Adult"

    else:
        category = "Senior"
    print("You fall under the category: " + category)

except:
    print("Please enter a number between 0 to 130")