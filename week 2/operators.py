odd_even = ""
number = int(input("Please enter a whole number \n"))
if number % 2 == 1:
    odd_even = "odd"
elif number % 2 == 0:
    odd_even = "even"
else:
    print("sorry enter a valid number")
    exit()
print(f"The number {number} is an {odd_even} number")
