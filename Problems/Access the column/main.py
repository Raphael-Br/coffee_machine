import pandas as pd


my_dict = {'A': {1: 1, 
                 2: 4, 
                 3: 6},
           'B': {1: 2, 
                 2: 7,
                 3: 10},
           'C': {1: 3, 
                 2: 11, 
                 3: 16}}

my_df = pd.DataFrame(my_dict)

print(my_df['C'])
print()
print(my_df[['C']])

print("\n* * *")

print('\nSeries:')
print(my_df['C'].values)
print(type(my_df['C']))

print('\nData Frame:')
print(my_df[['C']].values)
print(type(my_df[['C']]))

my_df.to_csv('books1.csv', columns=['A'])
# my_df.to_csv('books2.csv', columns=['A', 'B'])
my_df.to_csv('books3.csv', index=False, columns=['A', 'B'])
# my_df.to_csv('books4.csv', index=True)
# my_df[['Title']].to_csv('books.csv', index=True)
