# area of a circle
#


def circle_area(r):
    area = r * r * 3.14
    print(area)


while True:
    radius = float(input("Enter the radius of the circle"))
    circle_area(radius)
