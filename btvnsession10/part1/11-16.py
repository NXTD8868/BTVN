a = {
  "name" : "minh duc",
  "status" : "kha chac la doc than",
  "age" : "ko bt",
}
print(a)
#11
del a["age"]
print(a)
#12
x = input("thich xoa gi:")
del a[x]
print(a)
#13 kt ton tai
if 'name' in a:
  print("name exists in dic")
if 'nationality' not in a:\
  print('eror 404 Na not found')
#14 tu dien
dic = {
  'hello' : 'Здравствуйте',
  'comrade' : 'товарищ',
  'minh duc' : 'fa'
}
re = input("tu can tra:")
if re not in dic:
  print("suka blyat")
else:
  print(dic[re])
#15,16
while True:
  dic2 = {
  'raichu' : '''
   raichu has a regional variant that is Electric/Psychic.
   It evolves from Pikachu when exposed to a Thunder Stone.
   All Pikachu in Alola will evolve into this form regardless of their origin.''',
  'onix' : '''Onix resembles a giant chain of gray boulders that become smaller towards the tail.
   It has a rocky spine on its head and a pair of black eyes right beneath it.
    This Pokémon has a magnet in its brain.'''
}
  r = input("nhap ten pokemon:")
  r = r.lower()
  if r not in dic2:
    print("suka blyat")
  else:
    print(dic2[r])