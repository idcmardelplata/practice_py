condition = 0

while condition < 100:
    condition += 1
    if condition % 3 == 0 and condition % 5 == 0:
        print(f"{condition} fizzbuzz")
    elif condition % 3 == 0:
        print(f"{condition} fizz")
    elif condition % 5 == 0:
        print(f"{condition} buzz")
    else:
        print(condition)
    print(" ")

my_condition = 15

#print(35 // 3)
#print(type(35 // 3))
