#ListExample
a2=[10,20,'devi',20,30,45,'prasanth']
print(type(a2))
print(type(a2[2]))
a2.append(.20)
print(a2)
print(type(a2[7]))
a2.extend(a2)
print(a2)
print(a2.index(10))
print(a2.index(10,1))
print('testing ',a2.index(20,0,4))
#TupleExple
t1=(15,25,'hi')
print(type(t1))
print(t1.index('hi'))
#SetExample
s2={13,23,42,24,13,"hello"}
print(s2)
print(type(s2))
print(s2)
s2.add(21)
print(s2)
s2.pop()
print(s2)
s2.remove(13)
print(s2)
#DictionaryExample
d2={100 :'abc',200 :'bcd',300 :'dbc'}
print(d2)
d2[100]='xyz'
print(d2)
print(d2.keys())
print(d2.values())

a=10
b=10
print(a==b)



