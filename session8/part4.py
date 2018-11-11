t = 0
quiz = {
    '' : "how many legs does an octopus has?",
    '1.' : 'one leg',
    '2.' :'two legs',
    '3.' : 'four legs',
    '4.': 'eight legs'
}

for k, v in quiz.items():
    print(k,v)
x = input('your answer:')
if x == "4" :
    print("correct")
    t = t+1
else:
    print('u succ')

quiz1 = {
    '' : "is duc dumb?",
    '1.' : 'no',
    '2.' :'extremely dumb',
    '3.' : 'yes',
    '4.': 'i dont know'
}


for k, v in quiz1.items():
    print(k,v)
x = input('your answer:')
if x == "2" :
    print("correct")
    t = t+1
else:
    print('u succ')

quiz2 = {
    '' : "1+1 =?",
    '1.' : '2',
    '2.' :'69',
    '3.' : 'XDDD',
    '4.': 'i dont know'
}

for k, v in quiz2.items():
    print(k,v)
x = input('your answer:')
if x == "1" :
    print("correct")
    t = t+1
else:
    print('u succ')
print('correct question:', t,"/",3)
print((t/3)*100,"%")