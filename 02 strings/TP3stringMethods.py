"""

s = "hello python py px pw py me "
print("is endswith : ",s.endswith("on"))
print("is endswith : ",s.endswith("os"))

print("is startswith : ",s.startswith("he"))
print("is startswith : ",s.startswith("ho"))

print("find : ",s.find("py"))
print("find : ",s.find("w"))

print("r find : ",s.rfind("py"))
print(s[-2])

print("count is " ,s.count("pi"))

"""
"""
s = "hello PYthon py px PW py me "
print(id(s))
print(s.capitalize())
s = s.capitalize()
print(s)
print(id(s))

print(s.title())
print(s.lower())
s = s.replace("me","abdo".upper())
print(s)

"""
"""
s = "    python for world    "
print(len(s))
print(s)
print(len(s.strip()))

s = "pp====== python for world =====pp"
s = s.strip("r")
print(s)

s = s.lstrip("z")
print(s)
s = s.rstrip("p")
print(s)
"""

"""
a = "2"
b = str(22)
c = 222
d = 3434
print(a.zfill(4))
print(b.zfill(6))
a,b,c,d = "2","22","222","3434" #

"""
"""
s = 'python- is- high- level langue -in -progarmmation'
s = s.split("-")
#print(s)
#print(s[0])
#print(s[-1])
#print(s[4])

#print(s[0:2])
s.append("abdo")
#print(s)
"""
txt = """
On sait depuis longtemps que travailler avec du texte 
lisible et contenant du sens est source de distractions, et empêche de se concentrer sur la mise en page elle-même.
 L'avantage du Lorem Ipsum sur un texte générique comme 'Du texte. Du texte. Du texte.'
  est qu'il possède une distribution de lettres plus ou moins normale, et en tout cas comparable avec celle 
  du français standard. De nombreuses suites logicielles de mise en page ou éditeurs de sites Web ont fait du Lorem 
  Ipsum leur faux texte par défaut, et une recherche pour 'Lorem Ipsum' vous conduira vers de nombreux sites qui n'en 
  sont encore qu'à leur phase de construction. Plusieurs versions sont apparues avec le temps, parfois par accident, 
  souvent intentionnellement (histoire d'y rajouter de petits clins d'oeil, voire des phrases embarassantes).
"""
"""
txt = txt.upper()
# print(txt)
txt = txt.title()
# print(txt)
txt = txt.split(",")
#print(txt)

s = 'python- is- high- level langue -in - progarmmation'
#print(s.rsplit("-",3)

s = 'python is high level langue in progarmmation'
print(s.center(50))
print(s.center(len(s)+10))
"""
"""
s = "hello python py px pw py me "
print("is startswith : ",s.startswith("llo",2,8))
print("is startswith : ",s.startswith("py",2,19))
print("is startswith : ",s.startswith(("ello","me","pw")))
print("is endswith 1 : ",s.endswith("llo",2,8))
print("is endswith 2 : ",s.endswith("me",8))
print("is endswith 3 : ",s.endswith("me ",8))
print("is endswith 4 : ",s.endswith("me",27))
print("is endswith 5 : ",s.endswith("me",5,27))
print("is endswith 6 : ",s.endswith("py",0,24))
"""
"""
s = "hello python py px pw py -me "
print("find : 1-where find first  word searching  : ",s.find("o")) # returns index of first occurrence
print("find : 2-where find first  word searching  : ",s.find(" "))
print("find : 3-where find first  word searching  : ",s.find(" WX")) # when we don't have the word in our sentence result is (-1)
print("find : 4-where find first  word searching  : ",s.find("-",23,28))
print("find : 5-where find first  word searching  : ",s.find("-",26,28)) # false because (-) is out of 25 +

print("rfind : 2-where rfind last  word searching  : ",s.rfind("y"))
print("rfind : 2-where rfind last  word searching  : ",s.rfind("xz")) # if not fount ,it returns (-1)
print("rfind : 3-where rfind last  word searching  : ",s.rfind("px"))
print("rfind : 4-where rfind last  word searching  : ",s.rfind("pw"))
print("rfind : 2-where rfind last  word searching  : ",s.rfind("py",4,9))
"""
"""
s = "hello python py px pw py -me " # it's occurrence
print(s.rindex(" ",8,15))  # take result of last occurrence
print(s.index(" ",3,23))   # take result of first occurrence
print(s.rindex("u",8,15))  # if the searching not fount in the occurrence ,  operation not executive 
"""
"""
s = "hello ppppppppiiiiiiiiouuuuuuuuuuuupython py iiiiiiiiiiiiiiiiipx pw py -me " # it's occurrence
print(s.count("python")) #
print(s.count("hello")) # count how many (hello) repet in occurrence
print(s.count("me"))
print(s.count("i"))  # count how many (i) repet in occurrence
print(s.count("p",5,9))  # count how many (p) repet in occurrence + indexing for localisation the searching
"""
"""
s = "ppppppppiiiiiiiiouuuuuuuuuuuupython py iiiiiiiiiiiiiiiiipx pw py -me " # it's occurrence
print(id(s))
print(s.capitalize())
s = s.capitalize() #
print(id(s))
print(s)
"""
"""
s = "hello python py px pw py -me " # it's occurrence
print(" is title  : ",s.title()) # returns a makes capital for all words in occurrence
str = s.upper()
print(str)
str_1 = s.title()
print(str_1)

text_A1 = "i like cold wether,cold wether is my favorite time , when cold wether came in start season of whether," \
          " i buy more umbrula and sokhet wearing ,so cold wether is my part of life    "
rtext = text_A1.replace("cold wether","hot wether")
r1text = rtext.capitalize().lower().upper()
print(r1text)
"""
"""
s = "           hello teacher how are you?          " # it's occurrence
print(len(s)) # permet to count how the letters and spaces , we have in occurrence
print(s.strip()) #  method is used to remove the space from the both side of  the occurrence (left and right)
print(s.lstrip()) #  method is used to remove the space from the left of the occurrence
print("numbers occurrence is : ",len(s),s.rstrip()) #  method is used to remove the space from the right of the occurrence
s_A1 = s.strip("hello")
print(s_A1)
"""
"""
s = "hello teacher how are you?"
print(s.zfill(29))  #  Add the 0 right to left ,that method ussed just by string non integer or float
a = 4
b = 5
c = a+b
print(c)
print(type(c))
print(str(c).zfill(3))
print(type(c))

"""
"""
c = 'first ;way; to; take; python'
print(c.split(" "),id(c),type(c)) # method to creat the classes by space or (; - , :)
"""

a = []
print(type(a))
a.append("ينتلايتنين") # add the value to the occurrence,usually used in the variable the type list
print(a)


g = 'hello python world'
print(g.center(190)) #  centralisation of the occurrence by the value who is put it in center 