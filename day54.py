import csv, os
os.path.join('FAVORITES', 'bianca-sheet1.csv')
with open('bianca-sheet1.csv') as file:
    
    s = csv.DictReader(file)
    for t in s:
        print(t)