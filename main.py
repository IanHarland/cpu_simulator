from gates import *
from adder import *
from cache import Cache
from memory import Memory

# ISA
# OPCODES
# 000 | PLACE ENTIRE INSTRUCTION INTO REGISTER 31 FROM MEMORY
#     | 
# 001 | MULTIPLY
#     | rd(5) rs(5) rt(5) NULL(14)
# 010 | FLOOR DIVIDE
#     | rd(5) rs(5) rt(5) NULL(14)
# 011 | MODULO
#     | rd(5) rs(5) rt(5) NULL(14)
# 100 | ADDI
#     | rd(5) rs(5) imm(19)
# 101 | WRITE
#     | mem(16) reg(5) NULL(8)
# 110 | ADD
#     | rd(5) rs(5) rt(5) NULL(14)
# 111 | RETRIEVE/EXECUTE
#     | mem(16) NULL(13)


# INSTANTIATE MEMORY AND CACHE
memory = Memory()
cache = Cache()

# CREATE REGISTERS
register = ""
for i in range(32):
    register += '0'
registers = [register for i in range(32)]

# CU/ALU FUNCTIONS

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

def multiply(instruction):
    rd_idx = int(instruction[3:8], 2)
    rs_idx = int(instruction[8:13], 2)
    rt_idx = int(instruction[13:18], 2)
    rs_val = int(registers[rs_idx], 2)
    rt_val = int(registers[rt_idx], 2)
    registers[rd_idx] = bin(rs_val*rt_val)[2:]
    needed_0s = 32 - len(registers[rd_idx])
    leading_0s = ''
    for i in range(needed_0s):
        leading_0s += '0'
    registers[rd_idx] = leading_0s + registers[rd_idx]
    return (rd_idx, registers[rd_idx])

def floor_division(instruction):
    rd_idx = int(instruction[3:8], 2)
    rs_idx = int(instruction[8:13], 2)
    rt_idx = int(instruction[13:18], 2)
    rs_val = int(registers[rs_idx], 2)
    rt_val = int(registers[rt_idx], 2)
    registers[rd_idx] = bin(rs_val//rt_val)[2:]
    needed_0s = 32 - len(registers[rd_idx])
    leading_0s = ''
    for i in range(needed_0s):
        leading_0s += '0'
    registers[rd_idx] = leading_0s + registers[rd_idx]
    return (rd_idx, registers[rd_idx])

def mod(instruction):
    rd_idx = int(instruction[3:8], 2)
    rs_idx = int(instruction[8:13], 2)
    rt_idx = int(instruction[13:18], 2)
    rs_val = int(registers[rs_idx], 2)
    rt_val = int(registers[rt_idx], 2)
    registers[rd_idx] = bin(rs_val%rt_val)[2:]
    needed_0s = 32 - len(registers[rd_idx])
    leading_0s = ''
    for i in range(needed_0s):
        leading_0s += '0'
    registers[rd_idx] = leading_0s + registers[rd_idx]
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

def retrieve(instruction):
    mem_loc = instruction[3:19]
    new_data = cache.get(memory, mem_loc)
    return cu(new_data)

def write(instruction):
    mem_loc_0 = "0000000000000000"
    mem_loc = instruction[3:19]
    if mem_loc == mem_loc_0:
        return "Cannot write to location 0."
    reg_idx = int(instruction[19:24], 2)
    data = registers[reg_idx]
    return cache.write_to_mem(memory, mem_loc, data)

# Since for this simulation, I'll mostly just be storing
# integers in cache, the following function exists to simply place
# number into register 31 if the OPCODE is 000 (which for
# almost all 32 bit integers, it will be.)

def place(instruction):
    i = format(int(instruction, 2), '05b')
    return cu('1101111100000' +  i + '00000000000000')

# CU/ALU

def cu(instruction):
    if len(instruction) != 32 or type(instruction) != str:
        return "Invalid instruction"
    for char in instruction:
        if char not in ('0','1'):
            return "Invalid instruction"
    if instruction[:3] == '000':
        return place(instruction)
    if instruction[:3] == '001':
        return multiply(instruction)
    if instruction[:3] == '010':
        return mod(instruction)
    if instruction[:3] == '011':
        return floor_division(instruction)
    if instruction[:3] == '100':
        return addi(instruction)
    if instruction[:3] == '101':
        return write(instruction)
    if instruction[:3] == '110':
        return addition(instruction)
    if instruction[:3] == '111':
        return retrieve(instruction)
    
# TESTS

# add 0b1 to r0 val and insert into r2
print(cu('10000010000000000000000000000001'))
# add 0b11 to r2 val and insert into r3
print(cu('10000011000100000000000000000011'))
# add r2 to r3 and insert into r1
print(cu('11000001000100001100000000000000'))
# write r1 to memory location 1
print(cu('10100000000000000010000100000000'))
# multiply r1 by r3 and put into r4
print(cu("00100100000010001100000000000000"))
# floor divide r4 by r3 and insert into r5
print(cu("01100101001000001100000000000000"))
# r5 mod r3 and insert into r6
print(cu('01000110001010001100000000000000'))
# retrieve from memory location 1 (twice, in order to prove cache hit.)
print(cu('11100000000000000010000000000000'))
print(cu('11100000000000000010000000000000'))
# write r2 to memory location 1 (should write to cache)
print(cu('10100000000000000010001000000000'))
# Fill memory 2-129 with r6 which is currently 0b1
for i in range(2, 130):
    print(cu('101' + format(i, '016b') + '0011000000000'))
# Fill cache by retrieving from mem locations
for i in range(130):
    print(cu('111' + format(i, '016b') + '0000000000000'))
# Fill memory again (should fill cache and add dirty bits)
for i in range(2, 130):
    print(cu('101' + format(i, '016b') + '0011000000000'))
# Retrieve from memory again to see write back
for i in range(130):
    print(cu('111' + format(i, '016b') + '0000000000000'))