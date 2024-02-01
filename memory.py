class Memory:
    def __init__(self):
        memory_register = ''
        for i in range(32):
            memory_register += '0'
        self.locations = [memory_register for i in 2**29]

    def write(self, location, data):
        self.locations[location] = data