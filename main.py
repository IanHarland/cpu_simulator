from gates import *
from adder import *
from cache import Cache
from memory import Memory

register = ""
for i in range(32):
    register += '0'
registers = [register for i in range(32)]

def addition(instruction):
    rd_idx = int(instruction[3:8], 2)
    temp_reg = registers[rd_idx]
    if rd_idx == 0:
        return f"Invalid destination register {rd_idx}"
    rs_idx = int(instruction[8:13], 2)
    rt_idx = int(instruction[13:18], 2)
    rs_val = registers[rs_idx]
    rt_val = registers[rt_idx]
    carry = 0
    for i in range(31, -1, -1):
        next_digit = full_adder(int(rs_val[i]), int(rt_val[i]), carry)[0]
        next_carry = full_adder(int(rs_val[i]), int(rt_val[i]), carry)[1]
        temp_reg = temp_reg[:i] + str(next_digit) + temp_reg[i + 1:]
        carry = next_carry
    registers[rd_idx] = temp_reg
    return (rd_idx, registers[rd_idx])
    
def addi(instruction):
    rd_idx = int(instruction[3:8], 2)
    temp_reg = registers[rd_idx]
    if rd_idx == 0:
        return f"Invalid destination register {rd_idx}"
    rs_idx = int(instruction[8:13], 2)
    imm = '0000000000000' + instruction[13:]
    rs_val = registers[rs_idx]
    carry = 0
    for i in range(31, -1, -1):
        next_digit = full_adder(int(rs_val[i]), int(imm[i]), carry)[0]
        next_carry = full_adder(int(rs_val[i]), int(imm[i]), carry)[1]
        temp_reg = temp_reg[:i] + str(next_digit) + temp_reg[i + 1:]
        carry = next_carry
    registers[rd_idx] = temp_reg
    return (rd_idx, registers[rd_idx])


def cu(instruction):
    if len(instruction) != 32 or type(instruction) != str:
        return "Invalid instruction"
    for char in instruction:
        if char not in ('0','1'):
            return "Invalid instruction"
    if instruction[:3] == '000':
        return addition(instruction)
    if instruction[:3] == '001':
        pass
    if instruction[:3] == '010':
        pass
    if instruction[:3] == '011':
        pass
    if instruction[:3] == '100':
        pass
    if instruction[:3] == '101':
        return addi(instruction)
    if instruction[:3] == '110':
        pass
    if instruction[:3] == '111':
        pass

#add 0b1 to r0 val and insert into r2
print(cu('10100010000000000000000000000001'))
#add 0b11 to r2 val and insert into r3
print(cu('10100011000100000000000000000011'))
#add r2 to r3 and insert into r1
print(cu('00000001000100001100000000000000'))
