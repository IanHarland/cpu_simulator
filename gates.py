def nand_(i, j):
    if i and j:
        return False
    return True

def not_(i):
    return nand_(i, i)

def or_(i, j):
    return nand_(nand_(i), nand_(j))

def and_(i, j):
    