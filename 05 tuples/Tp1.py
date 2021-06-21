t1 = (1,3,4,56,65)
print(t1)
print(type(t1))
t2 = ()
print(t2,type(t2))
t3 = tuple()
print(t3)
t11 = tuple([1,3,4,56,65])
print(t11)
print(t1[2])
print(t1[-2])
# t1[2] = 44 # tuple is imutable object
x = t1[0 : 3] # slicing in tuple
print(x)
s = (23,'fr',['python','prg'],67)
print(s[2])
s2 = 1,
print(s2,type(s2))
s3 = 4,43,21,12,43.43
print(s3,type(s3))
print(max(s3))
print(min(s3))
print(len(s3))
print(21 in s3)
print(33 in s3)
print(sum(s3))
x = list(s3)
z = []
for i in s3 :
    z.append(i+1)
print(z)