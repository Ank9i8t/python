#code


size = int(input())

myList = [int(x) for x in input().split(' ')]

# for i in range(size):
#     myList.append(int(input()))

print(myList)    

for i in range(size):
    for j in range(size-i-1):
        if myList[j] > myList[j+1]:
            myList[j],myList[j+1]=myList[j+1],myList[j]
            
            
print(myList)   
            
