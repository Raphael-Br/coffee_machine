import pandas as pd


def print_dim(df):
    x, y = df.shape
    print(f'This DataFrame contains {x} rows and {y} columns')


students_list = [['Anna', 'Smith', 21],
                 ['Bob', 'Jones', 20],
                 ['Maria', 'Williams', 25],
                 ['Jack', 'Brown', 22]]
students = pd.DataFrame(students_list, columns=['First name', 'Family Name', 'Age'])

print_dim(students)
