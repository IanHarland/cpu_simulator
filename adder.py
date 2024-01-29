from gates import nand_, or_, and_, not_, nor_, xnor_, xor_

def half_adder(i, j):
    result = xor_(i, j)
    carry = and_(i, j)
    return result, carry

#tests
if __name__ == '__main__':
    print ('(result, carry)', half_adder(0, 0))
    print ('(result, carry)', half_adder(0, 1))
    print ('(result, carry)', half_adder(1, 0))
    print ('(result, carry)', half_adder(1, 1))