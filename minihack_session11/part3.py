#11
money = {
    'HP' : 600,
    'DELL' : 650,
    'MACBOOK' : 12000,
    'ASUS' : 400,
    'ACER' : 350,
    'TOSHIBA' : 600,
    'FUJISU' : 900,
    'ALIENWARE' : 1000
}
#12
print('gia cua 1 may hang ASUS:', money['ASUS'])
#13
x = input('nhap ten hang:')
print('gia cua 1 may o hang', x,':', money[x])
#14
print('gia cua 5 may ASUS la:', 5*money['ASUS'])
#15
a = input('chon hang:')
y = int(input('so may muon mua:'))
print('gia cua', y, "may hang", a, "la:", y*money[a])
#16
com = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30,
    'FUJISU' : 15,
    'ALIENWARE' : 5,
}
com[a] -= y
print(com)
for k,v in com.items():
    print(k,':',v)

