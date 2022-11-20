"""This algorithm uses Newton's formula to provide a rounded square root of a positive integer"""
def mySqrt(x: int) -> int:
    r = x
    while r * r > x:
        r = (r + x / r) / 2
    return int(r)

print("Please enter a positive integer to return it's approximate square root")
x = input()
x = int(x)
print(mySqrt(x))
