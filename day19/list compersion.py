'''
res=[]
for i in range(1,11):
    res.append(i)
print(res)




res=[i for i in range(1,11)]
print(res)


res=[i*3 for i in range(1,11)]
print(res)

res=[i+10 for i in range(1,11)]
print(res)



res=[i  for i in range(1 ,11) if i%2==0]
print(res)


res=[i if i%2==0 else 0 for i in range(1 ,11)]
print(res)


s='python'
v='aeiouAEIOU'
res=['*' if i in v else i for i in s]
print(res)

s='python'
v='aeiouAEIOU'
res=['*' if i in v else i for i in s]
print(' '.join(res))




res={i  for  i in range(1,17)}
print(res)

'''








