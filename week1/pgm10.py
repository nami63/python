a = int(input("Enter the age of person A: "))
b = int(input("Enter the age of person B: "))
c = int(input("Enter the age of person C: "))

if a > b and b > c:
    print(f"Person A, aged {a}, is the oldest, and Person C, aged {c}, is the youngest.")
elif b > a and a > c:
    print(f"Person B, aged {b}, is the oldest, and Person C, aged {c}, is the youngest.")
elif c > a and a > b:
    print(f"Person C, aged {c}, is the oldest, and Person B, aged {b}, is the youngest.")
elif c > b and b > a:
    print(f"Person C, aged {c}, is the oldest, and Person A, aged {a}, is the youngest.")
else:
    print("There is a tie or some ages are equal.")
