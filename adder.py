from gates import nand_, or_, and_, not_, nor_, xnor_, xor_

def half_adder(i, j):
    result = xor_(i, j)
    carry = and_(i, j)
    return result, carry

def full_adder(i, j, c):
    carry = or_(and_(or_(i, j), c), and_(i, j))
    result = or_(or_(and_(xor_(i,j), not_(c)), and_(nor_(i,j), c)), and_(and_(i,j), c))
    return result, carry


#tests
if __name__ == '__main__':
    print("Half adder tests:")
    print ('(result, carry)', half_adder(0, 0))
    print ('(result, carry)', half_adder(0, 1))
    print ('(result, carry)', half_adder(1, 0))
    print ('(result, carry)', half_adder(1, 1))
    print ('/n Full adder tests:')
    print ('(result, carry)', full_adder(0, 0, 0))
    print ('(result, carry)', full_adder(1, 0, 0))
    print ('(result, carry)', full_adder(0, 1, 0))
    print ('(result, carry)', full_adder(0, 0, 1))
    print ('(result, carry)', full_adder(1, 1, 0))
    print ('(result, carry)', full_adder(0, 1, 1))
    print ('(result, carry)', full_adder(1, 0, 1))
    print ('(result, carry)', full_adder(1, 1, 1))