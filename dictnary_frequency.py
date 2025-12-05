test_dic = {'codignal':2,'is':2,'best':2,'for':2,'coding':1}
print("the original dictionary:" + str(test_dic))
K = 2
res = 0
for key in test_dic:
    if test_dic[key]==K:
       res = res + 1
print("frequency of K is:" + str(res))