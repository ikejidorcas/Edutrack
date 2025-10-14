import pandas as pd
q1 = pd.read_csv('day.csv')
q2 =q1.loc[0:]
print(q2)