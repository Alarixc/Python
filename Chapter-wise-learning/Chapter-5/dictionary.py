myDict={
    "Harry": "A coder",
     1: {2.4:5.6},
     23.56:56.44,
     False:True

}
print(myDict[1][2.4])
# print(myDict.get(234).get(123))
print(myDict.get(234, {}).get(123)) #-->Returns a None type
# print(myDict.get(234, {234:{123:111}}.get(123))) #-->The only key in this dictionary is 234 as when you
#call get on a dictionary,it only looks at the top level keys so this will return a None type
print(myDict.get(234, {234:{123:111}})) #-->This is valid though






