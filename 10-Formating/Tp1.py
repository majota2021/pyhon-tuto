'''
s,z = ' python ',' java'
w = ' je code en '+s + "full" +z
c = 'CPP'
print('je code en {},{} et en {}'.format(s,z,c)) # first method in formating
print('je code en {0},{1} et en {2}'.format(s,z,c)) # first method in formating , DEFAULT indexing
print('je code en {2},{0} et en {1}'.format(s,z,c)) # first method in formating, POSITION by indexing

a = 10
b = 20
c = 30
print('notre serie constitue {2} ,{1} et {0}'.format(a,b,c))

a,b,c = 12,23,22
print('je code en {}'.format('python et java start formation 00 '))


print(f'notre serie est constitue {a},{b} et {c}') # 2 eme methode
'''
'''
name = 'ahmed '
age = 23
print('je suis %s et j ai %d' %(name,age))
print('je suis %s '% name)
print('je suis %s '% "achraf")

print('je suis %s et j ai %f' %(name,age))

print('je suis %s et j ai %.3f' %(name,age))

'''

d = 'hello pyton'
print('abdo {}'.format(d[:5]))
print(f'abdo {d[ :5]}')
print('abdo %s'%d)
print('abdo %.5s'%d) # steel method
# and formating