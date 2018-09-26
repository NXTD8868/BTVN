s = ['a', 'b', 'c', 'LOL', 'd']
s[0] = 'spider man'
print(s)
s[-1] = 'dragon ball'
print(s)
s.remove('LOL')
if 'LOL' not in s:
    print("no")
a = int(input("nhap stt: "))
s.pop(a)
print(s)
b = input("nhap ND: ")
s.remove(b)
print(s)
