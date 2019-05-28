import numpy as np

a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b=np.reshape(a,(1,-1,3))
c=a.reshape(2,3,-1)
print ('b=\n',b)
print ('c=',c)
#reshape(行,列)
#reshape(個,行,列)