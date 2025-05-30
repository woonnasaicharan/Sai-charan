a = list(input("Enter five numbers "))
print(a)
key = input()
for item in a:
    if key in a:
        print("found")
else:
    print("not found")
    