import pandas as pd
filename = 'data'+'2020-12-15'
df = pd.read_csv(filename+'.csv',encoding='utf-8')
df['country'] = df['country'].str.replace('\'','')
df['country'] = df['country'].str.replace('[','')
df['country'] = df['country'].str.replace(']','')

df['new'] = df['new'].str.replace('\'','')
df['new'] = df['new'].str.replace('[','')
df['new'] = df['new'].str.replace(']','')

df['all'] = df['all'].str.replace('\'','')
df['all'] = df['all'].str.replace('[','')
df['all'] = df['all'].str.replace(']','')

df['cure'] = df['cure'].str.replace('\'','')
df['cure'] = df['cure'].str.replace('[','')
df['cure'] = df['cure'].str.replace(']','')

df['death'] = df['death'].str.replace('\'','')
df['death'] = df['death'].str.replace('[','')
df['death'] = df['death'].str.replace(']','')

df.to_csv(filename+'_.csv',index=None)
