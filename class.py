# class in python
class student:
    # x = 10
    def __init__(self,val):
        self.x = val

    def display(self,val1,val2):
        print(self.x,val1,val2)

# obj = student(13)
# obj.display(2,3)
# create and constructor

#object creation and calling

#method in class

#access specifier
# protected

class parent:
    # _x = 10
    def __init__(self):
        self.y = 10
        # print('parent')

class child(parent):
    def __init__(this):
        super().__init__()
        this.y = 12
        # print('child')
    
    def display(this):
        print(this.y)

obj_child = child()
# obj_child.display()
obj_child.y = 15
del obj_child.y
# print(obj_child.y)
del obj_child
print(obj_child)

#self parameter

#modify and delete obj


#inheritance


