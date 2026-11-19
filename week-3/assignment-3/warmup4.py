try:
    
    userNumber = int(input("Enter a number either a postive or negative number or a 0: "))
    signOfNumber = "Positive"
    ParityOfNumber = "Even"

    if userNumber == 0:
        signOfNumber= "Zero"
        
    elif userNumber > 0:
        if userNumber%2 != 0:   
            ParityOfNumber = "Odd"

    elif userNumber < 0:
        signOfNumber= "Negative"
        if userNumber%2 != 0:   
            ParityOfNumber = "Odd"

    print(f"{userNumber} is {signOfNumber}")
    print(f"{userNumber} is {ParityOfNumber}")

except:
    print("Please enter a number")