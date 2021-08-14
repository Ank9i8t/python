#tuple 
# 1. represented by () 2. Allow duplicate 3. Unchangeable 4. Heterogenous 5. tuple constructor.
mylist = [1,2,3,4]
# print(mylist)
mytuple= tuple(mylist)
# print(mytuple)

#access item 
# print(mytuple[3])

#add item in tuple
mytuple = (1,2,3,4)
# print(mytuple)
mylist = list(mytuple)
mylist.append(5)
mytuple = tuple(mylist)
# print(mytuple)

#unpacking
# mylist = [name,roll]
mylist = [1,2,3]
[a,*b,c] = mylist
# print(a,b,c)
#for and while loop to access tuple item

# for item in mytuple:
#     print(item)

# for i in range(len(mytuple)):
#     print(mytuple[i])
# i=0

# while i<len(mytuple):
#     print(mytuple[i])
#     i+=1

#tuple join
mytuple2 = ('1','2')
mytuple = mytuple+mytuple2
mytuple = mytuple*2
# print(mytuple)
# mytuple.pop()
print(mytuple)

#method only 2



