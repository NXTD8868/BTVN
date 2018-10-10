#4
a = {
  "name" : "minh duc",
  "status" : "kha chac la doc than",
  "age" : "ko bt",
}
print(a)
#5
a["country"] = "vietnam"
print(a)
#6
b = input("nhap ten nd muon them:")
c = input("nhap nd:")
a[b] = c
print(a)
#7
print(a["name"])
print(a["status"])
#8
x = input("nhap key:")
print(a[x])