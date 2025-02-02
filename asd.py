a= open('perepis.txt','r')
q=0
for i in a:
    e=i
    g=e.split('.')
    if int(g[2]) < 1978:
        l=e.split(' ')
        print(l[0])
        q+=1
print(q)
a.close()

