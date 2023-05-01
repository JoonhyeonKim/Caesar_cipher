n = int(input('Type the key for encoding: '))
d = []
st = str(input('Type the encoded string: '))
for i in st:
    if i.isupper() == True:
        d.append(chr((ord(i)-64-n)%26+64))
    else:
        d.append(chr((ord(i)-96-n)%26+96))

ds =''.join(d)
print(ds)
