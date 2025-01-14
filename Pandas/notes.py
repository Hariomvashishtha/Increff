import  pandas as pd  # type: ignore
df = pd.read_csv('data.csv') # put the path to your data file here , all the data will be stored in df
print(df.head())  
print(df.head(4)) # print the first 4 rows of the data
print(df.tail(5)) # print the last 5 rows of the data
print(df.columns) # print the columns of the data
df_xls = pd.read_excel('data.xlsx') # put the path to your data file here , all the data will be stored in df_xls
print(df_xls.head())
print(df_xls.head(4)) # print the first 4 rows of the data
print(df_xls.tail(5)) # print the last 5 rows of the data
read_csv = pd.read_csv('data.csv', nrows=5) # read only the first 5 rows of the data
df = pd.read_csv('data.csv', header=None, delimiter='\t') # read the data without the header
print(read_csv)
read_csv = pd.read_csv('data.csv', usecols=[0,1,2]) # read only the first 3 columns of the data


# read headers
print(df.columns)

# read each column , specific column
print(df['Name'])   
print(df['Name'][0]) # read the first row of the column
print(df['Name', 'Age']) # read the two columns
print(df['Name'][0:5]) # read the first 5 rows of the column

# read each row
print(df.head(2)) # read the first 2 rows of the data
print(df.iloc[1]) # read the second row of the data
print(df.iloc[0:4]) # read the first 4 rows of the data
print(df.iloc[1, 2]) # read the second row of the data and the third column

# iterate through each row
for index, row in df.iterrows():
    print(index, row['Name'])
    print(index, row)

df.loc[df['Type'] == 'A'] # read the rows where the column 'Type' has the value 'A'

# sorting in pandas
df.sort_values('Name', ascending=False) # sort the data by the column 'Name' in descending order


df['Total'] = df.iloc[:, 4:10].sum(axis=1) 
# add a new column 'Total' to the data which is the sum of the columns from 4 to 10

cols = list(df.columns) # get the columns of the data
df = df[cols[0:4] + [cols[-1]]+cols[4:12]] # re-arrange the columns of the data

df.to_csv('data.csv', index=False) # save the data to a csv file without the index
df.to_excel('data.xlsx', index=False) # save the data to an excel file without the index
df.to_csv('data.csv', index=False, sep='\t') # save the data to a csv file without the index and with tab delimiter

new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)] # filter the data
new_df = new_df.reset_index(drop=True) # reset the index of the data

df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['Test 1', 'Test 2']
# change the values of the columns 'Generation' and 'Legendary' where the column 'Total' is greater than 500



df = pd.read_csv('modified.csv')
df['count'] = 1 # add a new column 'count' to the data
df.groupby(['Type 1', 'Type 2']).count()['count'] # group the data by the columns 'Type 1' and 'Type 2' and count the number of rows in each group



new_df = pd.DataFrame(columns=df.columns) # create a new data frame with the same columns as the original data
for df in pd.read_csv('modified.csv', chunksize=5): # read the data in chunks of 5 rows each
    results = df.groupby(['Type 1']).count() # group the data by the column 'Type 1' and count the number of rows in each group
    new_df = pd.concat([new_df, results]) # concatenate the results to the new data frame


df.loc[~df['Name'].str.contains('Mega')] # read the rows where the column 'Name' does not contain the string 'Mega'
# it will return all the strings that does not contain 'Mega'
df.loc[~df['Name'].str.contains('Mega' | 'fire') & (df['Type 1'] == 'Grass')] # read the rows where the column 'Name' does not contain the string 'Mega' and the column 'Type 1' has the value 'Grass'


# use of the flags = re.I ( ignore the case )
df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)] # read the rows where the column 'Name' starts with 'pi' followed by any number of characters

# give me some code for the conditional changes or set the column values
df.loc[df['Type 1'] == 'Grass', 'Type 1'] = 'Test 1' # change the values of the column 'Type 1' where the column 'Type 1' has the value 'Grass'

# aggregate statics ( group by ) ,( mean , sum , count , etc )
df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False) # group the data by the column 'Type 1' and calculate the mean of each group and sort the data by the column 'Defense' in descending order