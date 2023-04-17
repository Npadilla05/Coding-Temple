import pandas as pd
import numpy as np

df_snow = pd.read_csv(r'C:\Users\Noki\Downloads\archive (7)\annualsnow.csv', sep=',')
df_resort = pd.read_csv(r'C:\Users\Noki\Downloads\archive (7)\skiresorts.csv', sep=',')

# Lower case all column names
df_resort.columns = df_resort.columns.str.lower()
df_snow.columns = df_snow.columns.str.lower()

df_snow = df_snow.replace('"', '', regex=True) # regex specifies first argument is a regular expression. Replacing all instances with ''
df_resort = df_resort.replace('"', '', regex=True)

df_snow.columns = df_snow.columns.str.replace(' ','_') # Replace empty space with an underscore
df_resort.columns = df_resort.columns.str.replace(' ','_')

df_snow = df_snow.replace('cm', '',regex=True) # Realized the data included 'cm' so instead of doing indivd columns i replaced the entire data at once

df_snow['average_summit_depth'] = df_snow['average_summit_depth'].astype(int) # Average_summit_depth is now int
df_snow['total_snowfall'] = df_snow['total_snowfall'].astype(int)
df_snow['average_base_depth'] = df_snow['average_base_depth'].astype(int)
df_snow['max_base_depth'] = df_snow['max_base_depth'].astype(int)
df_snow['biggest_snowfall'] = df_snow['biggest_snowfall'].astype(int)

# Rename columns to indicate that my data is in cm
df_snow = df_snow.rename(columns={'total_snowfall': 'total_snowfall(cm)', 'average_base_depth': 'average_base_depth(cm)', 
                                  'average_summit_depth': 'average_summit_depth(cm)',
                                  'max_base_depth': 'max_base_depth(cm)', 'biggest_snowfall': 'biggest_snowfall(cm)'
                                   })

df_snow['location'] = df_snow['location'].str.title() # Titlecase the location column values

# miles = km * 0.621371
# Converting km to mi
new = []
for value in df_resort['longest_run']:
    if type(value) == float:
        value = '0.0 mi'
        new.append(value)
    elif type(value) == str:
        l = value.split()
        if l[1] == 'km':
             l[0] = str(round(float(l[0])* 0.621371,1))
             l[1] = 'mi'
             new.append(' '.join(l))
        else:
            new.append(value)

print(new)
df_resort['longest_run'] = new

# Drop and replace columns
df_resort = df_resort.replace('N.A.', 0)
df_resort = df_resort.drop(['limited_or_unlimited'], axis=1)
df_resort = df_resort.drop(['projected_closing'],axis=1)
df_resort = df_resort.drop(['projected_opening'],axis=1)
df_resort = df_resort.drop(['snow_making'],axis=1)

# Convert KM to Acres
new_list = []
for value in df_resort['skiable_terrain']:
    l = value.split()
    if l[1] == 'km':
        l[0] =round(float(l[0]) * 247.105, 1)
        
        new_list.append(l[0])
    else:
        new_list.append(l[0])
print(new_list)

df_resort['skiable_terrain'] = new_list

# new_skiable_terrain list to skiable_terrain
df_resort['skiable_terrain'] = new_list

df_resort= df_resort.drop_duplicates(subset=['skiable_terrain']) ## -> Not working??

# Rename columns to display labels
df_resort = df_resort.rename(columns={'summit_height': 'summit_height(ft)', 'vertical_drop': 'vertical_drop(ft)', 
                                      'base_elevation': 'base_elevation(ft)', 'longest_run': 'longest_run(mi)',
                                      'skiable_terrain': 'skiable_terrain(ac)', 'average_snowfall': 'average_snowfall(cm)',
                                      'beginners_runs': 'beginner_runs(%)', 'intermediate_runs': 'intermediate_runs(%)',
                                      'advanced_runs': 'advanced_runs(%)', 'expert_runs': 'expert_runs(%)'})

# Deleting labels from the values in the columns
to_clean = [df_resort['longest_run(mi)'], df_resort['runs_in_total'], df_resort['summit_height(ft)'], df_resort['vertical_drop(ft)'], df_resort['base_elevation(ft)'], df_resort['skiable_terrain(ac)'], df_resort['night_skiing']]
for col in to_clean:
    df_resort['longest_run(mi)'] = df_resort['longest_run(mi)'].str.replace('mi', '')
    df_resort['runs_in_total'] = df_resort['runs_in_total'].str.replace('km', '')
    df_resort['runs_in_total'] = df_resort['runs_in_total'].str.replace('mi', '')
    df_resort['summit_height(ft)'] =  df_resort['summit_height(ft)'].str.replace('m', '')
    df_resort['vertical_drop(ft)'] = df_resort['vertical_drop(ft)'].str.replace('m', '')
    df_resort['base_elevation(ft)'] = df_resort['base_elevation(ft)'].str.replace('m', '')
    df_resort['skiable_terrain(ac)'] = df_resort['skiable_terrain(ac)'].str.replace('ac', '')
    df_resort['skiable_terrain(ac)'] = df_resort['skiable_terrain(ac)'].str.replace('km', '')
    df_resort['night_skiing'] = df_resort['night_skiing'].str.replace('km', '')
    df_resort['night_skiing'] = df_resort['night_skiing'].str.replace('ac', '')

# Removing labels from values in column
df_resort = df_resort.replace("'", "", regex=True)
df_resort = df_resort.replace("cm","", regex=True)
df_resort = df_resort.replace("%","", regex=True)

# Title case location values to capitalize location names
df_resort['location'] = df_resort['location'].str.title() 

# Change  values in night skiing to be boolean 
df_resort['night_skiing'] = df_resort['night_skiing'].replace({1: True, 0: False})
df_resort['night_skiing'] = df_resort['night_skiing'].fillna(False)
df_resort['night_skiing'] = pd.to_numeric(df_resort['night_skiing'], errors='coerce')
df_resort['night_skiing'] = df_resort['night_skiing'].astype(bool)

df_resort['skiable_terrain(ac)'].drop_duplicates(inplace=True) ## -> Not working??

# Hard coded the replacement values to convert runs_in_total to integer
df_resort['runs_in_total'] = df_resort['runs_in_total'].replace('18.2', '18',regex=True)
df_resort['runs_in_total'] = df_resort['runs_in_total'].replace('41.8', '41',regex=True)
df_resort['runs_in_total'] = df_resort['runs_in_total'].replace('39.2', '39',regex=True)
df_resort['runs_in_total'] = df_resort['runs_in_total'].replace('103.3', '103',regex=True)
df_resort['runs_in_total'] = df_resort['runs_in_total'].replace('31.4', '31',regex=True)

# Converted NaN to 0 in order to get the runs columns to an integer
df_resort = df_resort.replace(np.nan, 0) 

# Convert data types to float or integer
df_resort['summit_height(ft)'] = df_resort['summit_height(ft)'].astype(int)
df_resort['vertical_drop(ft)'] = df_resort['vertical_drop(ft)'].astype(int)
df_resort['base_elevation(ft)'] = df_resort['base_elevation(ft)'].astype(int)
df_resort['runs_in_total'] = df_resort['runs_in_total'].astype(int)
df_resort['longest_run(mi)'] = df_resort['longest_run(mi)'].astype(float)
df_resort['projected_days_open'] = df_resort['projected_days_open'].astype(int)
df_resort['years_open'] = df_resort['years_open'].astype(int)
df_resort['days_open_last_year'] = df_resort['days_open_last_year'].astype(int)
df_resort['average_snowfall(cm)'] = df_resort['average_snowfall(cm)'].astype(int)
df_resort['beginner_runs(%)'] = df_resort['beginner_runs(%)'].astype(int)
df_resort['intermediate_runs(%)'] = df_resort['intermediate_runs(%)'].astype(int)
df_resort['advanced_runs(%)'] = df_resort['advanced_runs(%)'].astype(int)
df_resort['expert_runs(%)'] = df_resort['expert_runs(%)'].astype(int)

# Final step: Merge data together based on location, resort, and season pass
df_final = pd.merge(df_snow, df_resort, on=['location', 'resort', 'pass'])

# To csv
# When write to a csv file, the index becomes a column. That column becomes named "unknown: 0"
# To circumvent this we specify index = False
df_final.to_csv('ski_resort.csv', index=False)

'''
Resort Location vs Avg Snowfall shows the resorts which recieve the highest average snowfall.
Average of Total Snowfall(Cm) for each Resort broken down by Location.  Color shows details about Pass.  The marks are labeled by average of Runs In Total.  Details are shown for Night Skiing. 

Night Skiing Resorts with Longest Run shows all resorts which allow night skiing and which of those resorts have the longest run available.
Average of Longest Run(Mi) for each Resort.  Color shows average of Total Lifts.  The marks are labeled by Pass.

Locations with Highest Avg Projected Days Open show which locations are most likely to stay open the longest during season.
Average of Projected Days Open for each Location.  Color shows average of Average Base Depth(Cm).  The marks are labeled by average of Years Open.
'''