import pandas as pd
import numpy as np
arr=pd.read_csv("C:/Users/ambar/Documents/Book3.csv")
avg_score=np.mean(arr,axis=0)
print(avg_score)
h_s=np.argmax(avg_score)
sub=['Maths','Science','english','histroy']
print(sub[h_s],'=',max(avg_score))
