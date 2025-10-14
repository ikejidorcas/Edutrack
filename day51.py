w1 = []
g = open('today.rfg', 'r')
g1 = eval(g.read())
g.close()
def print1():
    for row in w1:
        print(f'{row[0]:^15} --- {row[1]:^15}')
while True:
    w2 =input('1:add? \n2:remove? \n...: ')
    if w2 == '1':
        w3= input('what would u like to add: ')
        w4 = input('what date please? ')
        row = [w3, w4]
        w1.append(row)
        print1()
    else:
        w2 = input('what would u like to remove: ')
        for row in w1:
            if w2 in w1:
                w1.remove(row)

    g = open('today.rfg', 'w')
    g.write(str(w1))
    g.close()