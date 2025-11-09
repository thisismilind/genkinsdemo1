import pandas as pd 

print("extract Data")

data ={
    'Id':[101,102,103],
    'NAme':['Ram','Raj','Raja'],
    'Age':[29,34,42]
}
df=pd.DataFrame(data)
print(df)

