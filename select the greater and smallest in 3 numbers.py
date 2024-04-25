def max_min(a, b, c):
    max_num = max(a, b, c)
    min_num = min(a, b, c)
    return (max_num, min_num)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

max_num, min_num = max_min(a, b, c)

print("The largest of the three numbers is:", max_num)
print("The smallest of the three numbers is:", min_num)
