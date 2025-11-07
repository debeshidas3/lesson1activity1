tuple1=[1,3,5,7,9]
tuple2=[2,4,6,8,10]
def multiply(p,q):
    return p*q

# Example usage:
result = [multiply(x, y) for x, y in zip(tuple1, tuple2)]
print(result)
