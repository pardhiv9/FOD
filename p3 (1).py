import numpy as np
beds=np.array([2,3,4,5,6])
sf=np.array([23,34,45,56,67])
sp=np.array([200,300,400,500,600])
average_sp=sp[beds>4]
average_price=np.mean(average_sp)
print(average_price)
