def ori_calc(num, n):
    return num * n

def lam_calc(n):
    return lambda x : x * n

f_double = lam_calc(2)
f_triple = lam_calc(3)
f_quadruple = lam_calc(4)

print(ori_calc(10, 2))
print(f_double(10))
print(f_triple(10))
print(f_quadruple(10))