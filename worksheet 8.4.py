#def area_of_rectangle(width,height):
 #   return width * height
#print(area_of_rectangle(5,10))

#def area_of_sqaure(length,bredth):
def square_num(value):
    return value ** 2
def square_num2(A):
    return A+A+A+A

def area_of_rectangle(c,d):
    return c * d
def perimeter_of_rectangle(C,D):
    return 2*(C+D)

def area_of_circle(p,r):
    return p*r**2
def perimeter_of_circle(P,R):
    return 2*P*R

def area_of_triangle(b,h):
    return 0.5*b*h
def perimeter_of_triangle(L,B,H):
    return L+B+H


shape=input("Would you like to find the solution for a square,solution for a rectangle ,solution for a circle or solution for triangle: ")
if shape == "square":
    print ("Would you like to find the area or perimeter, please type below")
    solution = input(":")
    if solution == "area":
        print("Welcome to my calculator for the area of a square")
        a=int(input("Please input a number: "))
        print(square_num(a))
    if solution == "perimeter":
        print("Welcome to my calculator for the perimeter of a square")
        A=int(input("Please input a number: "))
        print(square_num2(A))



if shape =="rectangle":
    print ("Would you like to find the area or perimeter, please type below")
    solution1 = input(":")
    if solution1 == "area":
        print("Welcome to my calculator for the area of a rectangle")
        c=int(input("Please input a number: "))
        d=int(input("Please input a number: "))
        result = area_of_rectangle(c,d)
        print("the area of the rectangle is: ",result)
    if solution1 == "perimeter":
        print("Welcome to my calculator for the perimeter of a rectangle")
        C=int(input("Please input a number: "))
        D=int(input("Please input a number: "))
        result = perimeter_of_rectangle(C,D)
        print("the perimeter of the rectangle is: ",result)
        

if shape == "circle":
    print("Would you like to find the area or perimeter, please type below")
    solution2 = input(":")
    if solution2 == "area":
        print("Welcome to my calculator for the area a circle")
        p = 3.1415926535
        r = int(input("Please input a radius: "))
        result = area_of_circle(p,r)
        print("the area of the circle is: ",result)
    if solution2 == "perimeter":
        print("Welcome to my calculator for the perimeter of a circle")
        P = 3.1415926535
        R = int(input("Please input a radius: "))
        result = perimeter_of_circle(P,R)
        print("the perimeter of the circle is: ",result)


if shape == "triangle":
    print("Would you like to find the area or perimeter, please type below")
    solution3 = input(":")
    if solution3 == "area":
        print("Welcome to my calculator for the area a triangle")
        b = int(input("Please input a base: "))
        h = int(input("Please input a height: "))
        result = area_of_triangle(b,h)
        print("the area of the triangle is: ", result)
    if solution3 == "perimeter":
        print("Welcome to my calculator for the perimeter of a triangle")
        L = int(input("Please input a side: "))
        B = int(input("Please input a side: "))
        H = int(input("Please input a side: "))
        result = perimeter_of_triangle(L,B,H)
        print("the perimeter of the triangle is: ", result)

