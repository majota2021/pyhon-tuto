'''
infos = {'name':'karim',
           'age':33,
           'adress':'kenitra'
           }
# indixing with dict
print(infos['name'])
print(infos['age'])
print(infos['adress'])

# modify dict
infos['name'] = 'idress' # modify name karim ; dict are mutable object
print(infos) # print dict
print(infos['name']) # indixing
infos['job'] ='student' # add new key and value
print(infos)
'''


infos = {'name':'karim',
           'age':33,
           'adress':'kenitra'
           }
print(infos['name']) # indexing method 1 (list method)
print(infos.get('name'))  # indexing method 2 (dict method)
# print(infos['driver']) # KeyError: 'driver'
print(infos.get('job')) # return none if key not exist
print(infos.get('job','not found')) # custom default argument for get method


