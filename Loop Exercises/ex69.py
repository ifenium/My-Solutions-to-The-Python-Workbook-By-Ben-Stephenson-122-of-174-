'''
Exercise 69: Approximate π
The value of π can be approximated by the following infinite series:
π ≈ 3 + 4/(2 × 3 × 4) − 4/(4 × 5 × 6) + 4/(6 × 7 × 8) − 4/(8 × 9 × 10) + 4/(10 × 11 × 12).....
Write a program that displays 15 approximations of π. The first approximation
should make use of only the first term from the infinite series. Each additional approximation displayed by your program should include one more term in the series, making
it a better approximation of π than any of the approximations displayed previously.
'''

constant = 3
even = 0
odd = 0

i_odd = list(range(4, 32, 4))
j_odd =  list(range(5, 39, 4))
k_odd = list(range(6, 46, 4))

i_even = list(range(2, 20, 4))
j_even = list(range(3, 28, 4))
k_even = list(range(4, 36, 4))


for i,j,k in zip(i_odd, j_odd, k_odd):
    odd += 4 / (i * j * k)

for i,j,k in zip(i_even, j_even, k_even):
    even += 4 / (i * j * k)


pi = constant + even - odd
print('The value of π(pi) after 15 iterations is: {}'. format(pi))