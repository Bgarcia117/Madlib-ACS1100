# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the descirption. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!

print("Area of a Rectangular Prism Calculator")
w = int(input("What is the width of your rectangular prism in inches?"))
l = int(input("What is the length of your shape in inches"))
h = int(input("Finally, what is the height of your shape in inches?"))
area = 2 * ((w * l) + (h * l) + (h * w))
print(f"The are of your rectangular prism with the width of {w}, the length of {l}, and the height of {h} is {area} inches")


