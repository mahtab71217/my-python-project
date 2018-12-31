#final project
import numpy as np
import matplotlib.pyplot as pl
arry=np.round(np.random.rand(30,30)*9+1)
arry=np.array(arry)
#print(arry)
counter=[]
for i in range(1,11):
    y=np.where(arry==i)
    b=np.size(y[0])
    counter.append(b)

print(counter)
print( type(counter))
pl.bar(range(1,11), counter, align='center', alpha=0.5)
for j in range(0,11):
    value=counter[j]
    pl.text(j+1,counter[j],value)
