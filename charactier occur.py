text=input("enter a word")
ch=input("enter the character to count")
count=0
for c in text:
    if c==ch:
       count+=1
print("the character",ch,"appears",count)        