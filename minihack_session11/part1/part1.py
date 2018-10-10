#1
com = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30,
}
#2
print('so MACBOOK co trong kho:', com['MACBOOK'])
#3
x = input("may tinh muon tim:")
print('so', x,'co trong kho la:', com[x])
#4
com['TOSHIBA'] = 10
#5
a = input('loai may moi:')
a = a.upper()
b = int(input('so luong:'))
com[a] = b
print(com)
com['DELL'] += 10
com['MACBOOK'] = 2
print(com)
