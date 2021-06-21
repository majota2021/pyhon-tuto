'''
#  dict eterable object
s = {
    'div':'python',
     'network':'java',
     'disgn':'css'
     }
print(s)
for i in s :
    print(i,' : ' ,s[i]) # s['div'] indixing

# test logique
d1 = {'mat': 19,'phys':20}
d2 = {'ing':12,'fr':13}
d11 = {'mat': 19,'phys':20}
d1 == d2 # test
print(d1==d11) # test d'egalite
print(d1 != d2) # no egale
print(d1 != d11)
print('fr' in d2)
print('ar' in d2)

'''

k = {'id':1234,
     'matr':12,
     'ville':'kenitra'}
print(k)
k['job']= 'driver'
print(k)
for i in k :
     print(i,' : ',k[i])

