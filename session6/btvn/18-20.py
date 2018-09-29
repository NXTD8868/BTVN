s = ['a', 'b', 'c', 'LOL', 'd', 'netflix','interne']
s.append("sport")
s.append("AB")
s.append("CE")
for item in s:
    print(item)
for item in s:
    print(item.upper())
i = 1
for item in s:
    print(i,". ", item)
    i = i+1
       