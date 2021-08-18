def sum_1():
    # print(c)
    return [1,2,3]

# a = int(input())
# b = int(input())
# print(type(sum_1(a,b)))
#function syntax

#calling a function

#arguments


#arbitary arguments *args



# def display(a,*b):
    # print(a,b)

# print('hello it works')
# display(1,2,3)
# print('it works also')

#keyword arguments

# def display(a,b,c):
#     print(f'a={a} b={b} c={c}')

# display(2,1,3)
# display(b=2,a=1,c=3)



#default parameter and passing list in argument

# def display(age,name='gautam'):
#     print(f'{name} and {age}')

# display(24,'amit')

#return  and recursion

# def rec_fuc(n):
#     if n == 1:
#         return 1
#     else:
#         return n*rec_fuc(n-1)

# print(rec_fuc(5))

#pass statement
# def display():
#     return None

# print(type(display()))


#lambda expression
name = lambda a : a+10

print(name(5))
#A lambda function is a small anonymous function, can take any number of arguments, but can only have one expression

#syntax

# c = 2*10
# for i in range(5):
#     print(c)
