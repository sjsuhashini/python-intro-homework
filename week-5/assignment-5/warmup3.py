userNames = ["Wills", "Peter", "Sam", "Lilly", "Olivia", "Luke", "Liam", "Mia"]
target = input("Enter a name to search :")
found = False

#without using function
""" for i, name in enumerate(userNames):
    if target.lower() == name.lower():
        print(f"{target} was found at index: {i}")
        found = True
        break

if not found:
    print(f"{target} was not found") """


#using function
def linear_search(data, target):
    for i in range(len(data)):
        if data[i].lower() == target.lower():
            return i
    return -1


result = linear_search(userNames, target)
if result < 0:
    print(f"{target} was not found")
else:
    print(f"{target} was found at index : {result}")