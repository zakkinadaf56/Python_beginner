# mydict={
#     "Fact": "In a quick",
#     "Zakki": "A coder",
#     "Marks": [1,2,3,5],
#     "Another": {'Zakki': 'Player'},
#     1:2
# }
# print(mydict['Fact'])
# #Dictionary methods
# print(list(mydict.keys()))#prints the keys of the dictionary
# print(list(mydict.values()))#print values values of the key
# print(list(mydict.items()))#print keys with their value of all items
# updatedict={
#     "lovish": "Friend"        #adds new items to the dictionary
# }
# mydict.update(updatedict)
# print(mydict)
# print(mydict.get("Zakki2"))#Returns none as zakki2 not present
# print(mydict["Zakki2"])#throws error as zakki2 is not present

nums=[1,2,3,1]
rep={}
rep[1]=1
rep[2]=23
print(rep)