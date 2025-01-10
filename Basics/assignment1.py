import math

def Area_and_Perimeter(shape):
    try:
        if shape == 'square':
            side = float(input("Enter the side of the square: "))
            if side <= 0:
                raise ValueError("Side length must be a positive number.")
            area = side ** 2
            perimeter = 4 * side
            print(f"Area of square: {area}")
            print(f"Perimeter of square: {perimeter}")
        
        elif shape == 'rectangle':
            length = float(input("Enter the length of the rectangle: "))
            breadth = float(input("Enter the breadth of the rectangle: "))
            if length <= 0 or breadth <= 0:
                raise ValueError("Length and breadth must be positive numbers.")
            area = length * breadth
            perimeter = 2 * (length + breadth)
            print(f"Area of rectangle: {area}")
            print(f"Perimeter of rectangle: {perimeter}")
        
        elif shape == 'parallelogram':
            base = float(input("Enter the base of the parallelogram: "))
            height = float(input("Enter the height of the parallelogram: "))
            side = float(input("Enter the side of the parallelogram: "))
            if base <= 0 or height <= 0 or side <= 0:
                raise ValueError("Base, height, and side must be positive numbers.")
            area = base * height
            perimeter = 2 * (base + side)
            print(f"Area of parallelogram: {area}")
            print(f"Perimeter of parallelogram: {perimeter}")
        
        elif shape == 'triangle':
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            side1 = float(input("Enter the first side of the triangle: "))
            side2 = float(input("Enter the second side of the triangle: "))
            side3 = float(input("Enter the third side of the triangle: "))
            if base <= 0 or height <= 0 or side1 <= 0 or side2 <= 0 or side3 <= 0:
                raise ValueError("All sides and height must be positive numbers.")
            area = 0.5 * base * height
            perimeter = side1 + side2 + side3
            print(f"Area of triangle: {area}")
            print(f"Perimeter of triangle: {perimeter}")
        
        elif shape == 'circle':
            radius = float(input("Enter the radius of the circle: "))
            if radius <= 0:
                raise ValueError("Radius must be a positive number.")
            area = math.pi * (radius ** 2)
            perimeter = 2 * math.pi * radius
            print(f"Area of circle: {area}")
            print(f"Perimeter of circle: {perimeter}")
        
        else:
            print("Invalid shape entered. Please enter one of the following: square, rectangle, parallelogram, triangle, circle.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("Select a shape (square, rectangle, parallelogram, triangle, circle):")
    shape = input().lower()
    Area_and_Perimeter(shape)

if __name__ == "__main__":
    main()
