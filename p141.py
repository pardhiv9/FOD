import pandas as pd
data={'customer_id':[101,102,101,102,101,103,104],
    'product_name':['brush','paste','brush','shoe','pen','shoe','pencil'],
    'customer_age':[22,30,20,40,22,30,22]
      
      }
df=pd.DataFrame(data)
print(df)
a=df['customer_age'].value_counts()
print("frequncy distribution of age" )
print(a)
