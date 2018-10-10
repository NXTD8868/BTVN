#20
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
        'Hit rate' : 5,
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
