#questions for practice 
#1) wap for sorting and reverse sorting a list,tuple.

def sorting_list_tuple(mylist):
    mylist.sort()
    print(f'ascending order : {mylist}')
    print(f'reverse order : {mylist[::-1]}')



#2) wap for sorting dictionary based on (a)keys (b) values.

def sort_dict():
    mydic = {
        'a':2,
        'b':1,
        'c':4,
        'd':3
    }

    for key in sorted(mydic.keys(),reverse=True):
        print(f'{key}:{mydic[key]}')


#3) wap to remove duplicate element in a list.

def remove_duplicate(mylist):
    # print(mylist)
    my_set = set(mylist)
    mylist = list(my_set)
    print(mylist)


#4) wap to count frequency of each element occuring in list.

def count_freq(mylist):
    mydict = {}
    for item in mylist:
        if item not in mydict:
            mydict[item] = 1
        else:
            mydict[item]+=1
    print(mydict)


#5) wap to reverse input statment. eg- i/p - 'This is example' && o/p - 'example is This'.

def reverse_str(mystr):
    tmp_list = mystr.split(' ')
    tmp_list.reverse()
    print(' '.join(tmp_list))



if __name__ == '__main__':

    # mylist = [int(i)  for i in input().split(' ')]
    mystr = 'this is a statement.'
    # sorting_list_tuple(mylist)
    # sort_dict()
    # remove_duplicate(mylist)
    # count_freq(mylist)
    reverse_str(mystr)
