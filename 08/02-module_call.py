from modules import num_add
from modules import *
import modules

a = num_add(10, 20)
b = modules.num_add(20, 30)
print(a, b)

from folder import f_module
from folder.f_module import add_num
import folder.f_module

a = f_module.add_num(10, 20)
b = add_num(10, 20)
c = folder.f_module.add_num(10, 20)
print(a, b, c)