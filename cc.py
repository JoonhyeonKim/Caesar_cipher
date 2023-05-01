n = int(input('Enter the key: '))
s = str(input('What do you wanna encode? '))
l = [] 

for i in s:
    if i.isupper() == True:
        l.append(chr(((ord(i))-64 + n) % 26 + 64))
    elif i.islower() == True:
        l.append(chr(((ord(i))-96 + n) % 26 + 96))
    else:
        l.append(i)

ns = ''.join(l)
print(ns)
