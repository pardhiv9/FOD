import pandas as pd
data={'customer_id':[101,102,101,102,101,103,104],
    'product_name':['brush','paste','brush','shoe','pen','shoe','pencil'],
    'customer_review':['good','bad','great','super','good','bad','bad']
      
      }
df=pd.DataFrame(data)
print(df)
a=df['customer_review'].value_counts()
print("frequncy distribution of customer review" )
print(a)
