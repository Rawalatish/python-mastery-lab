# s1 = {4,9,5,7,3,1,6, 's', 'p', 'a', 'r','k'}

s1 ={1,2,3,4}
s2 = {'a','b','c','d', 4}

x = "this is the april month"

xx = {}

for i in x:
    if i in xx.keys():
        xx[i] = xx[i] + 1
    else:
        xx[i] = 1
print(xx)

y = sorted(xx)
print(y)

yy = dict(sorted(xx.items(), key = lambda v:v[1]))
print(yy)
