import pandas as pd

# tạo các series
s = {'một': pd.Series([1., 2., 3., 5.], index=['a', 'b', 'c', 'e']),
     'hai': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

# tạo DataFrame từ dict theo các index được chọn
df = pd.DataFrame(s, index=['a','c','d'])

print(df)

# Output:
#
#    một  hai
# a  1.0  1.0
# c  3.0  3.0
# d  NaN  4.0