userNumber = -1
while(userNumber < 0):
    try:
        userNumber = int(input("Enter any positive integer: "))
        if userNumber < 0 :
            print("Please enter a valid positive number. Try again! ")
        else:
            print(f"Your number is : {userNumber}")
            
    except:
        print("Please enter a valid positive number. Not words!")