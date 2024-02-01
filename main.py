from gates import *
from adder import *
from cache import Cache
from memory import Memory

registers = ['' for i in range(8)]

def addition(instruction):
    rd_idx = int(str(instruction)[0:3])
    rs_idx = int(str(instruction)[3:6])
    rt_idx = int(str(instruction)[6:])
    rs_val = int(registers[rs_idx], 2)
    rt_val = int(registers[rt_idx], 2)
    for i, j in registers[rs_idx], registers[rt_idx]:
        carry = 0b0
        digit = 
        registers[rd_idx].insert(0, )
    
    

def cu(instruction):
    if instruction // 0b1000000000 == 0b000:
        addition(instruction%0b1000000000)
    if instruction // 0b1000000000 == 0b001:
        pass
    if instruction // 0b1000000000 == 0b010:
        pass
    if instruction // 0b1000000000 == 0b011:
        pass
    if instruction // 0b1000000000 == 0b100:
        pass
    if instruction // 0b1000000000 == 0b101:
        pass
    if instruction // 0b1000000000 == 0b110:
        pass

print(addition(101010101))