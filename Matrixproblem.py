'''To give a quadratic matrix of dimension n * n calculate the last digit of the product of the elements on line k.'''

n = int(input("The number n="))
k = int(input("The number k="))
matrix = []

for line in range(0, n):
    line_column = []
    for column in range(0, n):
        line_column.append(int(input()))
    matrix.append(line_column)

product = 1
for column in range(0, n):
    product = product * matrix[k-1][column]

product = product % 10
print(product)
