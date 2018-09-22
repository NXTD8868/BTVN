import re
print("dang ky tai khoan d-mail:")
x = input("ten dang nhap:")
z = input("email:")
while "@" not in z or "." not in z :
    z = input("nhap lai email:")
y = input("mat khau:")
while len(y) > 8 or (bool(re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', 'y')))  :
    y = input("mat khau yeu sinh ly nhu anh duc:")
    
a = input("nhap lai mat khau:")
while a != y:
    a = input("nhap lai mat khau:")


    