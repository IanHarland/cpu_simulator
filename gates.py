def nand_(i, j):
    if i and j:
        return 0
    return 1

def not_(i):
    return nand_(i, i)

def or_(i, j):
    return nand_(nand_(i, i), nand_(j, j))

def and_(i, j):
    return not_(nand_(i, j))

def nor_(i, j):
    return not_(or_(i, j))

def xor_(i, j):
    return and_(nand_(i, j), or_(i, j))

def xnor_(i, j):
    return not_(xor_(i, j))

#test cases
if __name__ == '__main__':
    print('nand', nand_(1, 1), nand_(1,0), nand_(0,1), nand_(0,0))
    print('not', not_(1), not_(0))
    print('or', or_(1, 1), or_(1,0), or_(0,1), or_(0,0))
    print('and', and_(1, 1), and_(1,0), and_(0,1), and_(0,0))
    print('nor', nor_(1, 1), nor_(1,0), nor_(0,1), nor_(0,0))
    print('xor', xor_(1, 1), xor_(1,0), xor_(0,1), xor_(0,0))
    print('xnor', xnor_(1, 1), xnor_(1,0), xnor_(0,1), xnor_(0,0))