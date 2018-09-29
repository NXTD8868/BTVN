a = []
print("C")
print("R")
print("U")
print("D")
e = input("nhap:")
i = 0
while i < 12:
    if e == "C":
        C = input("whats ur fav:")
        a.append(C)
        print(a)
        i = i +1
    if e == "D":
        for item in a:
            if item ==0:
                print("empty")
                i = i+1
            if item > 0:
                print(item)
                i = i+1

