1#
#a
for i in range(20):
    print("* ",end = "")
print()
#b
a = int(input("nhap so ngoi sao:"))
for i in range(a):
    print('* ',end ="")
print()
#c
for i in range(1,10):
    if i%2 == 1:
        print("x ",end = "")
    if i%2 == 0:
        print("* ",end = "") 
print()
#d
x = int(input('so ngoi sao:'))
for i in range(x):
    if i%2 == 0:
        print("x ",end = "")
    if i%2 == 1:
        print("* ",end = "")
    
print()
#c
for i in range(4):
    print('x * ',end = "")
print('x')
#f
for i in range(3):
    for a in range(7):
        print('* ',end ="")
    print()
#g
r = int(input("nhap n:"))
h = int(input('nhap m:'))

for i in range(h):
    for a in range(r):
        print('* ',end ="")
    print()
print()
#h
tdx = int(input('nhap toa do x:'))
tdy = int(input('nhap toa do y:'))
for i in range(5):
    for a in range(6):
        if i == tdy - 1 and a == tdx -1:
            print('X ',end = "")
        else:
            print('* ',end = "")
    print()

#i
w = int(input('nhap do rong:'))
h = int(input('nhap do cao:'))
tdx = int(input('nhap toa do x:'))
tdy = int(input('nhap toa do y:'))
for i in range(h):
    for a in range(w):
        if i == tdy - 1 and a == tdx -1:
            print('X ',end = "")
        else:
            print('* ',end = "")
    print()