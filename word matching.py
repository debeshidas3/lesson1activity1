words=["mom","dad","apple","book","wow"]
count=0
for word in words:
    if len(word)>=2 and word[0]==word[-1]:
       count=count+1
print("number of words with same first and last letter",count)
        