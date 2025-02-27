#Function Activity
def odd(x):
    x = eval(input("Enter a number: "))
    X = x % 2
    if X == 0:
        print(f"{x} is an even number")
    else:
        print(f"{x} is an odd number")
odd(1)