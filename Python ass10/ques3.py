# Circle Area and Circumference

def circle_properties(radius):
    pi = 3.1416
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return area, circumference

area, circumference = circle_properties(5)
print(f"Area: {area}")
print(f"Circumference: {circumference}")
