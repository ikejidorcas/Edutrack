import traceback
debug = False
list1 = []
try:
    f = open('nawa.f', 'r')
    f1 = eval(f.read())
    f.close()
except:
    if debug:
        print(traceback)
    else:
        print('oops there isa problem with your code')
    
for row in list:
    print(row)