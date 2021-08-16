

# dictionary in python
#1. store key:val pair 2. changable 3. don't allow duplicate keys 4. ordered hain.

mylist = [1,2,3,4]
mylist[0]

mydic = {
    'name':'gautam',
    'age':24,
    'age':25,
    'place':'sre'
}
# print(mydic['age'])

#access dictionary
# print(mydic.get('age'))
# print(mydic.keys())
# print(mydic.values())
# for item in mydic.values():
#     print(item)

# for key,val in mydic.items():
#     print(f'{key}:{val}')


# if 'gautam' in mydic.values():
#     print('yes')

#change value in dict

mydic['name'] = 'amit'

# print(mydic.get('name'))

#add item

mydic.update({'age':'26'})
# print(mydic)
mydic.update({'phone':'8983489384'})
# print(mydic)


#delete item
item = mydic.popitem()

# print(type(item))
# print(mydic)

item = mydic.pop('age')
# print(item)
# print(mydic)

#loop in dict

for item in mydic:
    print(mydic[item])

# for item in mydic.values():
#     print(item)


# for key,val in mydic.items():
#     print(f'{key}:{val}')

#dictionary methods
