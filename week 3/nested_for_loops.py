sequence = input("Please enter a sequence\n")

marker = input("Please enter the character for the marker\n")
prev_count = 0
count = 0

for char in sequence:
    if char != marker:
        count += 1
    elif char == marker:
        prev_count = count
        count = 0

print(f"The distance between the markers is {prev_count}")
