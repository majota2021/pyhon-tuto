'''
a,b = 11,34
if a >10 :
    print('a sup a 10')
else :
    print('a inferieur 10 ')

'''
'''
a,b = 10,15
if a > b :
    print('a > b')
else :
    print('a <= b')
'''
'''
a,b = 19,19
if a == b :
    print('a = b')
elif  a > b :
    print('a>b')
else :
    print('a < b ')
'''
'''

x = '20'
print(x,type(x))
x = int(x)
print(x,type(x))
'''
'''
# tep = 30
tep = input('saisir la temperature de votre region : ')
tep = int (tep)
if tep < 20 :
    print('le fait froid')
elif tep < 30 :
    print('belle')
elif tep < 40 :
    print('chaud')
else:
    print('tres chaud')
'''

#note = 19

note = int (input('saisir vote note : ')) # converir string to numbers

if note < 10 :
    print('non valide')
elif note < 12 :
    print('valide passable')
elif note < 14 :
    print('valide avec monsionne')
elif note < 16 :
    print('bien')
else:
    print('excelent')

