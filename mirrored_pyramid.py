n = int(input("Enter the number of rows (half-diamond height): "))
# Upper half (pyramid)
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2*i + 1))
# Lower half (inverted pyramid)
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2*i + 1))