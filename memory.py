class Memory:
    def __init__(self):
        memory_register = ''
        for i in range(32):
            memory_register += '0'
        self.locations = [memory_register for i in range(2**16)]

    def write(self, location, data):
        self.locations[int(location, 2)] = data
        return f"Data {data} stored in memory at memory location: {location}"