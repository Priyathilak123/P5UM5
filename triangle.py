# Python Program to find Area of a Triangle

a = float(input('Please Enter the First side of a Triangle: '))
b = float(input('Please Enter the Second side of a Triangle: '))
c = float(input('Please Enter the Third side of a Triangle: '))

# calculate the Perimeter
Perimeter = a + b + c

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
Area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print("\n The Perimeter of Traiangle = %.2f" %Perimeter);
print(" The Semi Perimeter of Traiangle = %.2f" %s);
print(" The Area of a Triangle is %0.2f" %Area)
