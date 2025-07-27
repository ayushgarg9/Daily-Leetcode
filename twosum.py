list1 = [9,5,7,1,4,3]
target = 13
n = len(list1)
#logic(optimal approach)
for i in range(n):
    for j in range(i+1,n):
        if target - list1[j] == list1[i]:
            print([i,j])
    
    