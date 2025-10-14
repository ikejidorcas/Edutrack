import pandas as pd 
xc = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns = ['a', 'b', 'c'], index=['X', 'Y', 'Z'])

q = xc.describe
print(q)