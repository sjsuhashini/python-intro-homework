userName= input("Enter your name: ")
userAge= input("Enter your age: ")
print("Welcome : "+ userName + "!")
print("You will be " + str(int(userAge) + 10) + " years old after 10 years!")

#Error 1
# """ Enter your name: Wills
# Enter your age45
# Traceback (most recent call last):
#   File "D:\codeTheDream\python_class\python-intro-homework\week-2\assignment-2\warmup4.py", line 3, in <module>
#     print("Welcome : "+ userNam + "!")
#                         ^^^^^^^
# NameError: name 'userNam' is not defined. Did you mean: 'userName'? """
    #Fix: Change userNam to userName in line 3

#Error 2
# Enter your name: Peter
# Enter your age: 33
# Welcome : Peter!
# You are 33 years old!
# PS D:\codeTheDream\python_class\python-intro-homework\week-2\assignment-2> python warmup4.py
# Enter your name: Peter
# Enter your age: 33
# Welcome : Peter!
# Traceback (most recent call last):
#   File "D:\codeTheDream\python_class\python-intro-homework\week-2\assignment-2\warmup4.py", line 4, in <module>
#     print("You will be " + userAge + 10 + " years old after 10 years!")
#           ~~~~~~~~~~~~~~~~~~~~~~~~~^~~~
# TypeError: can only concatenate str (not "int") to str
    #Fix: in Line 4 print("You will be " + str(int(userAge) + 10) + " years old after 10 years!") Converting string age into int to add with 10 
    #then converting the result integer into string to concatenate in the print function



