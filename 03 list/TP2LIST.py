"""
n = [2,4,56,78,90]
print(type(n))
print(n)
print(len(n))
print(n[2])# indexing
print(n[1:]) # slicing
n2 = n[1:3] #  slicing
print(n2)

"""

"""
n = [2,4,56,78,90] # [2, 4, 56, 78, 90, 10]
n.append(10)
print(n) # all elements
print(n[-3]) # indexiing
print(n[1: ]) #  slicing
print("slicing with step equal 2 :",n[1: :2]) # slicing with step equal 2
print("slicing with step equal 2 :",n[: :2]) # slicing with step equal 2
print(n[ : ]) # print all elments with slicing with default step : 1
print(n[ :  : 1])  # print all elments with slicing with step equql 1
print(n[ 2:-1])  # Slicing
print(n[-1:2])  # Empty list
print(n[-1:2:-2])
print(n[ : :-1])
n_revers = n[: :-1] # how to revers list with second convention (-1)
print(n_revers)
n = [2, 4, 56, 78, 90, 10]
n.reverse() # revers list with builting function with revers method
print(n) 
"""
"""
#list are mutable object in python 
n = [2, 4, 56, 78, 90, 10]
print(n[0])
n[0]=22
print(n[0])
"""
"""
s_1 = ['geomat','statistique','matt','inglish']
s_2 = ['arabic','francais']
print(s_1,s_2,sep='\n')
s_3 = s_1+s_2 # concatinate two  lists
print(s_3)
#s_1.append('physique')
print(s_1)
#s_1.insert(1,'sig')
print(s_1)
#s_2.insert(2,s_1) #
print(s_2)
s_2.extend(s_1) #
print(s_2)
"""
"""
s_1 = ['geomat','stqtistiaue','matt','inglish']
# s_1.remove('geomat') # remove by string no by value
# print(s_1)
print(s_1.pop())
print(s_1)
"""
"""
s_1 = ['geomat','stqtistiaue','matt','inglish']
s_1.sort() # order croisssant  pour les alphqbet
print(s_1)
"""
"""
s_2= [111,45,6,667,876]
#s_2.sort() # order croisssant  pour les nombers
#print(s_2)
#s_2.reverse()
#print(s_2)
s_2.sort(reverse = False )
print(s_2)
s_2.sort(reverse = True )
print(s_2)
"""
"""
list1 = ['fr','ing','org','int']
print(list1.index('org'))
print(list1.index('ing'))
print(list1.index('fn')) # ValueError: 'fn' is not in list
"""
"""
# list with for loop
l = ['python',34,48,"hello",10,22]
#print(l[0])
#print(l[1])
#print(l[2])
#print(l[3])
#print(l[4])
#print(l[5])
for ele in l: 
    print(ele) # our logique or stitement 
    
print('fin de programme')   
"""
'''
s_12 ='python'
for i in s_12 :
    print(i)
'''
"""
abdo = ['id','cin','Nt','adress','30']
abdo.pop()
print(abdo)
abdo.pop(2)
print(abdo)
print(abdo[1])
print(abdo)
majo = abdo.pop(1)
print(majo)
print(abdo)

print(abdo,majo)
abdo.extend([12,33,23,222,11]) # used like append to add str or numbers to occurrence
print('extend ',abdo,majo)
"""
"""
abdo = ['id', 'adress', 12, 33, 23, 222, 11]
abdo.insert(0,'hello world') # insert qn item and given a position
print(abdo)
abdo.insert(3,'hello world') # that permit to insert 'hello world' in value 3 in occurrence [abdo]
print(abdo)
# abdo.insert([4]) # TypeError: insert expected 2 arguments, got 1
abdo.insert(-1,'python') # when we use -1 for string should take it last value !?????
print(abdo)
print(len(abdo))
abdo.insert(len(abdo),'fd') # this sytax work like [append] so add the string in last occurrence
print(abdo)
abdo.insert(0,'google')
print(abdo)
"""
"""
s = [34,43,222,343,221,5555]
s.sort()  # sort items of the list in place
print(s)
"""
'''
u = "morrocoo is LAST COUNTRY IN PRODACTION IM EDUCATION "
q = u.capitalize()
print(q)
'''
abdo = ['id', 'adress', 12, 33, 23, 222, 11]
abdo.insert(-1,'python') # when we use -1 for string should take it last value !?????
print(abdo)
abdo.insert(1,'python2')
print(abdo)