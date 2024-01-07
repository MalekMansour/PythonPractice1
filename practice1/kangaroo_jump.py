'''
You are choreographing a circus show with various animals. 
For one act, you are given two kangaroos on a number line ready to jump in the positive direction 
(i.e, toward positive infinity).
You have to figure out a way to get both kangaroos at the same location at the same time 
as part of the show. If it is possible, return YES, otherwise return NO.
'''
def kangaroo(x1, v1, x2, v2):
    if x1 == x2 and v1 == v2:
        return "YES"
    if v1 != v2 and (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) >= 0:
        return "YES"
    else:
        return "NO"

# Example:
result1 = kangaroo(0, 3, 4, 2)
result2 = kangaroo(2, 5, 6, 2)
print(result1)
print(result2)
