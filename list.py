# operators
# import math
# print(math.floor(3//2))
#exponent

#floor division



#pyton list 
# 1.mutuable hain 2.heterogeneous and allow duplicate 3.index starts from [0]  4.length calculate  5.list constructor
# mylist = [1,2,'s',1.2,True,[1,2,3]]
# mylist = [1,2,1,1,1]
# mytuple=list((1,2,3,4))
# print(type(mytuple))

#accessing list
mylist= [1,2,3,4,5]
# print(mylist[2])

#change list item
mylist[2]=6
# print(mylist)
#add/remove item
mylist.append(7)
# print(mylist)
mylist.insert(2,'3')
# print(mylist)

mylist2 = ['1','2']

mylist.extend(mylist2)
# print(mylist)

a = mylist.pop()
# print(a)
# print(mylist)
mylist.remove(5)
# print(mylist)

common_list = [2,1,2,1]
common_list.remove(1)
# print(common_list)
mylist =[1,2,3,4,5]
a = mylist.pop(-5)
# print(a)
# print(mylist)
#loop item in list
# for item in mylist:
    # print(item)
#list comprehensions
mylist = [1,2,3,4,5]

mylist = [item for item in mylist if item%2==1]

# for item in mylist:
#     if item%2==1:
#         print(item)

# print(mylist)

#sort/copy list
Mylist= [1,2,3,4]
mylist = [-1,0,5,4,3,-2]
# mylist.sort()
# print(mylist)
# print(mylist[::-1])
# print(Mylist)
#join list
# newlist = mylist.copy()
newlist = list(mylist)
mylist[2] = 10
print(newlist)
print(mylist)
#list methods
