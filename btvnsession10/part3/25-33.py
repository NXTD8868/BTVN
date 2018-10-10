#25
sach = {
    'name' : 'one puch man',
    'character' : ['main character', 'extra characters', ' random shit'],
    'dia diem ban' : ['cua hang', 'hieu sach'],
}
print(sach) 

#26
sach['nuoc ban'] = ['nhat ban', 'vietnam', 'somewhere']
print(sach)
#27
for k ,v in sach.items():
     print(k, "-", v)
#28

sach['character'] = ['a', 'b', 'c']
print(sach)
#29
sach['character'].append('d')
print(sach)
#30
sach['character'].pop(0)
print(sach)
#31

print(sach['character'][1])
#32
for a in sach['character']:
    print(a)

#33
for k,v in sach.items():
    print(k ,v)
