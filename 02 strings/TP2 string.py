# indexing
s = " hello world"
#    012345678910
# -9-8-7-6-5-4-3-2-1

print(s)
print (s[0]) # elelment de S dont l indice egal a 0
print (s[1])
print (s[2])
print(s[-5])
print(s[-1])
z = "sidi kacem" + " abdo"
print(z)
z = "sidi kacem" + s
print(z + " python")
print(z)
z = s*3
print(z)
# slissing: extrir de sous string

s = "hello world"
print (s[0:-1])
print(s[0:-1])
print(s[2:-4])
print(s[-5:3:-2])
print(s[-1:0]) # ensemble vide non result

print(s[-1:0:-2])
ss = s[-1: :-1]
print(s,ss,sep="\n")

#  string function
s = "helloworld"
print(len(s))
print(max(s))
print(max("djkfa"))
print(min(s))
print(min("opsc"))

# logique operation avec les strings
print("-"*110)
s = "hello world"
print("hello" in s )
print("bnjour" in s )
print("h" in s )
print("hello"not in s )

var_1 = "python"
var_2 = "java"
print(var_1 == var_2)
print("hello"=="hello")
print("hello"=="hey")

print(var_1 >= var_2)
print(var_1 <=var_2)
print("hello">="child")

# strings methods

s = "HELLO"
print("is isalnum : ",s.isalnum())
print("is isalpha : ",s.isalpha())
print("is islower : ",s.islower())
print("is isupper: ",s.isupper())

s = "    "
print("is space : ", s.isspace())