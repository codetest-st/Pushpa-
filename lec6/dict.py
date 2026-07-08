name={"raj":55,"ram":66,}#dictonary
print(name)
print(type(name))#type
print(name.get("raj"))#give output by index
name["khana"]=77#add in dictonary
print(name)
name["raj"]=88#change value 
print(name)
del name ["raj"]#delete from dictonary
print(name)
print(name.keys())#show keys
print(name.values())#show values
#multi dimesnion dictonary
d1={"name":"Steve","age":25,"marks":60}
d2={"name":"Anil","age":23,"marks":75}
d3={"name":"Asha","age":20,"marks":70}
std={1:d1,2:d2,3:d3}
print(std)
print(len(name))#give size
print(max(name))#gives largest value
print(min(name))#gives smallest value
print(name.pop("ram"))#pops ram
print(name)
print(name.items())
