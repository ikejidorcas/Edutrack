import pandas as pd
sd =pd.read_excel('lokoja.xls')
sd.to_csv('lokoja.csv', index = False)
print('lokoja.xls converted')