# for i in eterobj :
# logique
'''
l=[1,2,3]
for i in l :
    print(i)
for i in [4,5,6,7] :
    print(i)


sq= 'python'
for i in sq :
    print(i)
for i in 'javaa' :
    print(i)

t=(12,'df',45)
for i in t :
    print(i)

dic={'name':'ahmed','age':12}
for i in dic :
    print(i,':',dic[i]) #simple indexing with dict , dict.get(i)
for i in '1000' :
    print(i)


# while true condition :
#  logique
x = 10
while x <= 20 :
    print('abdo',x)
    x = x+2         #     x += 1

d = [1,2,3,4,5,6,7,8,9,10]
for i in d :
    if i %2 == 1 :
        print(i)

# range function
#gerer un serie cuit des nombers
print(range(10))
for i in range(10) : # started from 0 to 9
    print(i)
'''
'''
for i in range(12) :
    if i %2 == 0 :
       print(i)
'''
'''
for i in range(0,12,2) :
    print(i)
l = list(range(5))
print(l)
l2 = list(range(1,12,3))
print(l2)
'''
'''
x = 10
while x < 20 :
    x += 1 # x = x+1  , x *= 2 , x = x*2
    print(x)
'''
''' 
x = 10
while x < 20 :
    x += 1 # x = x+1  , x *= 2 , x = x*2
    if x == 15 :
        break  # break while loop
    print(x)
  '''
'''
x = 10
while x < 20 :
    x += 1 # x = x+1  , x *= 2 , x = x*2
    if x == 15 :
        continue # break current condition
    print(x)
 '''
'''
x = 0
while x < 20 :
    x += 1 # x = x+1  , x *= 2 , x = x*2
    if x %2 == 0 :
        continue # break current condition
    print(x)
'''
'''
for i in range(21) :
    if i == 15 :
        break
    print(i)
'''
for i in range(21) :
    if i %2 == 0 :
        continue
    print(i)

