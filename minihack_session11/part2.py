#7
com = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30,
}
for k, v in com.items():
    print(k,':',v)
#8
t = 0
for v in com.values():
    t += v
print('tong so may:', t)
#9
com['FUJISU'] = 15
com['ALIENWARE']= 5
print(com)
#10s
for v in com.values():
    t += v
print('tong so may:', t)