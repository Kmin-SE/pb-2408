
n = 6
s = 1
for i in range(1, n+1):
    if n % i == 0 and i % 2 == 0:
        s *= i
print(s)

# a = 1
# b = 2
# c = 3
# s = 0
# if a < 0:
#     s += a
# if b < 0:
#     s += b
# if c < 0:
#     s += c