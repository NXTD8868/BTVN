com = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30,
    'FUJISU' : 15,
    'ALIENWARE' : 5,
}
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
for v in com.values and money.values:
    print(v*v)

