# --encoding = utf-8--
"""
    @Time  : 2022/1/21 23:03
    @Author: Chen Feng
    @File  : method.py
"""
for i in range(1, 10):
    for j in range(1, i+1):
        print("%sX%s=%s" % (j, i, i*j), end=" ")
    print()

print("-"*50)

a = 1
while a < 10:
    b = 1
    while b < a+1:
        print("%sX%s=%s" % (b, a, a*b), end=" ")
        b += 1
    print()
    a += 1



