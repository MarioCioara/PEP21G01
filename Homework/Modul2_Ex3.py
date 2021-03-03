# 40P
# Calculate the diagonal of a rectangle with sides 10 and 15


#The diagonal splits the rectangle into two equal right-angle triangles
#We use Pitagora's theorem to calculate the diagonal


#Input the length and the width
l = float(input("Length = "))
w = float(input("Width = "))

#The diagonal is square root of the sum of length at power 2 and width at power 2
diagonal = (l.__pow__(2) + w.__pow__(2)).__pow__(1/2)

print(diagonal)
