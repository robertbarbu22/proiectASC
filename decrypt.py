a = "00000011"
b = "b"
#a = ord(a)
b = ord(b)
#print(b)
#a=bin(a)
b=bin(b)

#a = a[2:]
b = b[2:]

# if(len(a)<8):
#     a = (8-len(a))*"0" + a
if(len(b)<8):
    b = (8-len(b))*"0" + b

a1 = []
for i in a:
    a1 =a1 + [i]
a = a1

b = list(b)

ct = 0
for i in a:
    a[ct] = int(a[ct])
    b[ct] = int(b[ct])
    a[ct] = a[ct]^b[ct]
   # print(a[ct],end="")
    ct += 1

sum = 0
p = 0
ct = 0
a.reverse()

for i in a:
    if a[ct]==1:
        sum = sum + 2**p
    p += 1
    ct += 1

#print()
print(chr(sum))
