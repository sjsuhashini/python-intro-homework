# Loop from 1 to 30 and print one word per line:

# "FizzBuzz" if the number is divisible by both 3 and 5
# "Fizz" if divisible by 3 only
# "Buzz" if divisible by 5 only
# The number itself otherwise
# Check the combined case first.

for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print(f"FizzBuzz")
    elif i % 3 == 0:
        print(f"Fizz")
    elif i % 5 == 0:
        print(f"Buzz")
    else:
        print(f"{i}")
        