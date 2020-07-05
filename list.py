fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
 lst.append(line.rstrip().split(" "))
a=[]
for i in lst:
 a = a+i

a.sort()
newlist=[]
for i in a:
 if i not in newlist:
  newlist.append(i)

print(newlist)
