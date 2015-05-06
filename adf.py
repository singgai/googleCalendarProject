f1=open("C:\\home\\file1.txt").read().split("\n")
f2=open("C:\\home\\file2.txt").read().split("\n")

res=open("C:\\home\\resultfile1file2",'w')

for i in range(len(f1)-1):
    dif= float(f1[i])-float(f2[i])
    if abs(dif)>1:
        res.write("Line "+str(i+1)+str(dif)) 
        res.write("\n")
    #print f1[i]
