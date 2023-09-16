a={1,2,4,5,1,2}#elements that are repeated are not printed in  sets
print(type(a))
print(a)
b=set()#creating empty set
b.add(4)
b.add(5)
b.add((2,4,7))#cannot add dictionary and list as they are updatable
print(b)
#methods in set
b.remove(5)
print(b)
print(len(b))