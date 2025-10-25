L=[1,2,3,4,5,6,7,8,9,10]
print("original list",L)
count=0
for i in L:
    count+=i
avg=count/len(L)
print("sum is",count)
print("average is",avg)
print("smallest element is",L[0])
print("largest element is",L[-1])    