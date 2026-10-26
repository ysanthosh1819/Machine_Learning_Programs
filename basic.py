day = int(input("Enter a day number (1-5): "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Invalid day")

w = 97
x = 98
y = 99
z = 20
data = w+x+y+z
print("Total:", data)
if data > 400:
    print("pass")
else:
    print("fail")

    