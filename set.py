# set in python
#1. A set is a collection which is both unordered and unindexed
#2. do not allow duplicate values
#heterogenous 

myset = {'a','b','c','c'}

# print(myset)

#access item in set
# for item in myset:
#     print(item)


#add item in set


#add() method
myset.add('d')
# print(myset)

#update() method
myset1 = {'1','2'}
myset2 = {'3','4'}
mylist = ['3','4','5']
mydic = {'c':4,'d':3}
myset1.update(mydic.items())
# print(myset1)

#remove  item from set

#remove() method and discard() and pop()

myset = {'gautam','amit','ashutosh','verma'}

# myset.remove('gauta')
# print(myset)

# myset.discard('verm')
# print(myset)

a = myset.pop()
# print(a)
# print(myset)

# to remove duplicate from list
mylist=[1,1,1,1,2,3,3,3,4]
myset = set(mylist)
mylist = list(myset)
# print(mylist)


myset1 = {'a','b','c'}
myset2 = {'a','d','e'}
myset1.union(myset2)
print(myset1.union(myset2))
