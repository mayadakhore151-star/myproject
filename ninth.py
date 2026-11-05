def rectangle_area(length, width):
    area = length * width
    return area

l = float(input("Enter length: "))
w = float(input("Enter width: "))

result = rectangle_area(l, w)

print("Area of Rectangle:", result)
