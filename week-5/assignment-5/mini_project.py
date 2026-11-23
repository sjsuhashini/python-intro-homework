# === Number Cruncher ===
# 1. Find minimum
# 2. Find maximum
# 3. Search for a number -- linear search
# 4. Sort the list -- bubble sort
# 5. Quit
# Choose an option (1-5):

numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def printOptions():
    print(" \n=======================Number Cruncher====================")
    print("1. Find minimum  |  2. Find maximum  |  3. Search for a number")
    print("4. Sort the list |  5. Quit")
    print(" Choose an option (1-5) \n")

def findMin(numbers):
    minNum = numbers[0]
    for i in numbers:
        if i < minNum:
            minNum = i
    return minNum

def findMax(numbers):
    maxNum = numbers[0]
    for i in numbers:
        if i > maxNum:
            maxNum = i
    return maxNum

def searchNumber(numbers,target):
    for i, num in enumerate(numbers):
        if num == int(target):
            return i
    return -1

def sortList(numbers):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
    return numbers


def main():
   
    print("Number cruncher")
   

    while True:
        printOptions()
        userchoice = input("Enter a number from 1 to 5 :")
        if userchoice == "1":
            minNum = findMin(numbers)
            print(f"Smallest number in the List is : {minNum}")
        elif userchoice == "2":
            maxNum = findMax(numbers)
            print(f"Largest number in the List is : {maxNum}")
        elif userchoice == "3":
            target =input("Enter a number to search : ")
            result = searchNumber(numbers,target)
            if result < 0:
                print(f"{target} was not found")
            else:
                print(f"{target} was found at index : {result}")
        elif userchoice == "4":
            sortedList= sortList(numbers)
            print(f"Sorted List : {sortedList} ")
            
        elif userchoice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
            

if __name__ == "__main__":
    main()
