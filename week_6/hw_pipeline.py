import pandas as pd
import numpy as np
import plotly_express as px

df = pd.read_csv(r'C:\Users\Noki\Downloads\AirQualityUCI\AirQualityUCI.csv', sep=';', decimal= ',', parse_dates=[['Date', 'Time']])
# print(df)

df.columns = df.columns.str.lower() # Converting column titles to lower-case for easier access

df = df.drop(['unnamed: 15', 'unnamed: 16'], axis=1) # Deleting null columns

df = df.replace(-200.0, 0) # Replacing 'missing values' of -200 with 0

print(df.dtypes)

# Drop unnamed fig out what to do with -200. either keeping at 0 or getting the mean
print(px.histogram(df, x='co(gt)'))
px.histogram(df, x='nox(gt)')

df['co(gt)'] = df['co(gt)'].replace(0.0, 1.77)
df['nox(gt)'] = df['nox(gt)'].replace(0.0, 203.65)
df['no2(gt)'] = df['no2(gt)'].replace(0.0, 93.25)

df1 = df['co(gt)'].mean() # Calculating the mean to replace 0
#print(df1)

df2 = df['nox(gt)'].mean() # Calculating the mean to replace 0
#print(df2)

df3 = df['no2(gt)'].mean() # Calculating the mean to replace 0
#print(df3)

# Save dataframe to csv file
df.to_csv('hw.csv', index=False)

'''
This is my analysis based off the story in my Tableau.

Graph 1:
-Average of Co(Gt) for each T (bin) broken down by Date Time Quarter  
-Color shows average of Co(Gt)
-The marks are labeled by average of T
-The view is filtered on T (bin), which excludes Null. 

Cooler temps reflect less pollution

Graph 2:
-The trend of average of Nmhc(Gt) for Date Time Hour
-Color shows average of Nmhc(Gt)
-The marks are labeled by average of T.

More pollution is in the air during the morning and late evening hours. 
Analysis could be that people leaving for work and leaving work may have correlation in the amount of pollution in the air. 
More people are out in the hours of 6-9am and 4-7pm which are your school and work hours.

Graph 3:
-The trends of average of Pt08.S5(O3)
-Average of Pt08.S4(No2)
-Average of Pt08.S3(Nox)
-Average of Pt08.S1(Co) 
-Average of Pt08.S2(Nmhc) for Date Time Day
-Color shows average of Ah
-The marks are labeled by sum of T.

The average pollution for each metal oxide sensor stay consistent with each other. 
There are similar amounts displayed for each day of the month. 
No type of concentration outweighs the other.
'''