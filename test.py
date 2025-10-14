import math
print('CALCULATOR FOR SHAPES')
print()
print('ENTER THE SHAPE YOU WANT TO DETERMINE')
q1 = input('''1.Square
            \n2.Circle
            \n3.Triangle
            \n4.Parellelogram 
           \n5.Cube 
           \n6.Cylinder 
           \n7.Cone 
           \n8.Sphere 
           \n...: ''')
if q1 == '1':
    l1 = float(input('enter value of lenght: '))
    b1 = float(input('enter value of breadth: '))
    Area = l1 * b1
    print(f'The area of the square is {Area:.2f}')
elif q1 == '2':
    r = float(input('enter value of the radius: '))
    Ac = 3.143 * r**2
    print(f'Area of circle is equal to {Ac: .2f}')
elif q1 == '3':
    bt =float(input('enter value of base: '))
    ht = float(input('enter height of triangle: '))
    At = 0.5 *bt*ht
    print(f'area of the triangle is equal to {At: .2f}')
elif q1 == '4':
    bp = float(input('enter base of parallelogram: '))
    hp = float(input('enter height of parallelogram: '))
    Ap = bp * hp
    print(f'area of parallelogram is equal to {Ap: .2f}')
elif q1 == '5':
    lc= float(input('enter lenght of cube: '))
    Ac= 6 * lc**2
    print(f'area of cube is equal to {Ac: .2f}')
elif q1 == '6':
    rc = float(input('enter radius of cylinder: '))
    hc = float(input('enter height of cylinder: '))
    Acy = 2 * 3.143* rc (rc + hc)
    print(f'area of cylinder is equal to {Acy: .2f}')
elif q1 == '7':
    rc = float(input('enter radius of cone: '))
    lc = float(input('enter lenght of cone: '))
    Aco = 3.143 * rc * () 
    print(f'area of parallelogram is equal to {Aco: .2f}')
elif q1 == '8':
    rs = float(input('enter radius of sphere: '))
    As = 4 * 3.143* rs**2
    print(f'area of sphere is equal to {As: .2f}')
