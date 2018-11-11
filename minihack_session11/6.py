from random import randint
p = {
    'Name' : 'Light',
    'Age' : 17,
    'Strength' : 8,
    'Defence' : 10,
    'HP' : 100,
    'Backpack' : ['Shield', 'Bread Loaf'],
    'Gold' : 100,
    'Level' : 2,
}
print(p)
#21
p['Gold'] += 50
#22
p['Backpack'].append('FlintStone')
#23
p['Pocket'] = ['MonsterDex', 'Flashlight']
print(p)
#24
p['Skill'] = [
    {
        'skill 1' : 'Tackle',
        'Minimum level' : 1,
        'Damage' : 5,
        'Hit rate' : 0.3,
    },
    {
        'Skill 2' : 'Quick attack',
        'Minimum level' : 2,
        'Damage' : 3,
        'Hit rate' : 0.5,
    },
    {
        'Skill 3' : 'Strong kick',
        'Minimum level' : 4,
        'Damage' : 7,
        'Hit rate' : 0.2,
    },
]
print(p)
#25
print(p['Skill'])
#26
for items in p['Skill']:
    for k,v in items.items():
        print(k,':',v)
ability = {
    '1.' : 'Tackcle',
    '2.' : 'Quick attack',
    '3.' : 'Strong kick',
    '4.' : 'skip'
}
for i in range(5):
    print()
print('a wild boar appears')
boar = {
    'enemy' : 'Boar',
    'Hp' : 150,
    'attack' : 5,
}
for k,v in boar.items():
    print(k,':',v)

while True:
    for k,v in ability.items():
        print(k,v)
    do = input('pick a skill to use:')
    if do =='1':
        print('light uses Tackle')
        chance = randint(1,10)
        if chance < 3:
            print('miss')
            print('Boar HP:', boar['Hp'])
        if chance >= 3:
            print('HIT!')
            boar['Hp'] -= 5
            print('Boar HP:', boar['Hp'])
    if do =='2':
        print('light uses Quick attack')
        chance = randint(1,10)
        if chance < 5:
            print('miss')
            print('Boar HP:', boar['Hp'])
        if chance >= 5:
            print('HIT!')
            boar['Hp'] -= 3
            print('Boar HP:', boar['Hp'])
    if do =='3':
        print('light uses Strong kick')
        chance = randint(1,10)
        if chance < 2:
            print('miss')
            print('Boar HP:', boar['Hp'])
        if chance >= 2:
            print('HIT!')
            boar['Hp'] -= 7
            print('Boar HP:', boar['Hp'])
    if do == '4':
        print('turned skipped')
    print('turn ended')
    print('boar uses headbutt')
    atk = randint(1,10)
    if atk <= 5: 
        print('HIT!')
        p['HP'] -= 5
        print('Light HP:', p['HP'])
        print('Boar HP:', boar['Hp'])
    if atk > 5:
        print('boar misses')
        print('Light HP:', p['HP'])
        print('Boar HP:', boar['Hp'])
    print()
    print()
        
    if boar['Hp'] <= 0:
        print('boar is defeated')
        break
    if p['HP'] <= 0:
        print('Light is knocked out')
        break




