''' simple if

if condition:
    statement

'''
charger=int(input("enter the chageing"))
if charger <=20:
    print("the chageing is low go and charge")




'''product discount'''


p={1:{'name':'bread','discount':4},
   2:{'name':'sugar','discount':3},
   3:{'name':'bread2','discount':0}
   }
print(p)
index=int(input("enter the discount"))
if p[index]['discount']:
    print(f'{p[index]["name"]}has discount')



'''best seller'''
s={1:{'name':'ramu','bestseller':True},
   2:{'name':'sai','bestseller':False},
   3:{'name':'ramsai','bestseller':True}
   }
index=int(input("enter the bestseller"))
if s[index]['bestseller']:
    print(f'{s[index]["name"]}is bestseller')
