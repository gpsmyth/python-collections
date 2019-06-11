count = 0
lst = []
d = {}

l =[1, 2, 2, 4, 3, 1, 2, 5, 3, 4, 6, 1]

print ("Original list - ", l)
for (k,v) in enumerate (l):
    if v not in lst:
        lst.append(v)

print (lst)
for item in lst:
    # pdb
    # if item in l:
    for (k,v) in enumerate (l):
        if item == v:
            count +=1
    # d['number', 'count'] = item, count 
    d[item] = count 
    # print( type(item), type(count))
    count = 0
print (d)
#for k in d.keys() :
    #if k.values() % 2:
        #print (k.keys())
        
for (k,v) in d.items():
    if v % 2:
        print ( "Value of {0} has occurred {1}".format(k, v) )
