import pandas as pd

s = {'một': pd.Series([1., 2., 3., 5.], index=['a', 'b', 'c', 'e']),
     'hai': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd']),
     'ba': pd.Series([9., -1.3, 3.5, 41.1], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(s)

# thêm cột bốn với giá trị mỗi ô theo công thức
df['bốn'] = df['hai'] - df['ba']

# thêm cột với giá trị vô hướng (scalar value)
df['Chuẩn'] = 'OK'

# thêm cột không cùng số lượng index với DataFrame
df['Khác'] = df['hai'][:3]

# thêm cột True/False theo điều kiện
df['KT'] = df['một'] == 3.0

# dùng hàm insert. Cột "chèn" bên dưới sẽ ở vị trí 2 (tính từ 0), có giá trị bằng cột một
df.insert(2, 'chèn', df['một'])

print(df)

#Output:

   một  hai  chèn    ba   bốn Chuẩn  Khác     KT
a  1.0  1.0   1.0   9.0  -8.0    OK   1.0  False
b  2.0  2.0   2.0  -1.3   3.3    OK   2.0  False
c  3.0  3.0   3.0   3.5  -0.5    OK   3.0   True
d  NaN  4.0   NaN  41.1 -37.1    OK   NaN  False
e  5.0  NaN   5.0   NaN   NaN    OK   NaN  False