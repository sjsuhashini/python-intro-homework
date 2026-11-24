def is_valid_score(score):
    return 0 <= score <= 100

try:
    score=int(input("Enter your score between 0 and 100 :"))
    
    if is_valid_score(score): 
        print("Valid Score")
    else:
        print("Invalid score — must be between 0 and 100.")

except ValueError:
    print("Enter a valid score in numbers from 0 to 100!")