import pandas as pd

s = {'một': pd.Series([1., 2., 3., 5.], index=['a', 'b', 'c', 'e']),
     'hai': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd']),
     'ba': pd.Series([9., -1.3, 3.5, 41.1], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(s)

# chọn cột hai
df_hai = df['hai']
print(df_hai)

# Output:
#
# a    1.0
# b    2.0
# c    3.0
# d    4.0
# e    NaN
# Name: hai, dtype: float64