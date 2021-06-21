'''
student = {'name':'hamza','age':22,'coures':['mat','info']}
print(student,len(student))

l= ['python','java']
l[1]
student['name']
print(student['name'])
#print(student['ad'])
print(student.get('coures','not found here'))
student['name']='karim' # modify value in occurrence
print(student)
student['q1'] = 'v1' # creat new element
print(student)

'''
#dict method


student = {'name':'hamza','age':22,'coures':['mat','info'],'ad':'casa'}
#del student['coures']
#print(student)
#print(student.popitem())
print(student)
#student.clear() # empty dict
print(student)
print(student.keys())
print(student.values())
print(student.pop('name'))
print(student)
student['name']='simo'
student['age'] = 40
print(student) # {'age': 40, 'coures': ['mat', 'info'], 'ad': 'casa', 'name': 'simo'}
student.update({'name':'abdo','ad':'tanger','pays':'maroc'})
print(student)
# dict with for loop
print(student.keys())
for i in student :
    print(i,'; ',student[i])


print(student.items())
for i,j in  student.items() :
    print(i,j)
l=[1,2,3,5]
l.append(6)
print(l)
l.insert(0,10)
print(l)
l.insert(len(l),13)
print(l)
l.insert(-8,11)
print(l)
