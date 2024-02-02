class Cache:

    def __init__(self):
        ##stores memory location [0] and data [1] in list
        self.j = 0
        cache_register = ['', '']
        for i in range(32):
            if len(cache_register[0]) < 16:
                cache_register[0] += '0'
            cache_register[1] += '0'
        self.locations = [cache_register for i in range(128)]
        self.dirty_bits = [0 for i in range(128)]
    
    def __repr__(self):
        return f"Current status of cache:\n{self.locations}"
    
    def get(self, memory_name, memory_register):
        for i in range(128):
            if memory_register == self.locations[i][0]:
                print("Cache hit!")
                return self.locations[i][1]
        data = memory_name.locations[int(memory_register, 2)]
        if self.dirty_bits[self.j] == 0:
            self.locations[self.j] = [memory_register, data]
            self.j += 1
            if self.j == 128:
                self.j = 0
            return data
        else:
            memory_name.locations[self.locations[self.j][0]] = self.locations[self.j][1]
            print(f"Writing {self.locations[self.j][1]} from cache location: {self.j} back to memory location {self.locations[self.j][0]}")
            self.dirty_bits[self.j] = 0
            self.locations[self.j] = [memory_register, data]
            self.j += 1
            if self.j == 128:
                self.j = 0
            return data

    
    def write_to_mem(self, mem_name, mem_loc, data):
        for i in range(128):
            if mem_loc == self.locations[i][0]:
                print("Cache hit!")
                self.locations[i][1] = data
                self.dirty_bits[i] = 1
                return f"Data input at cache location {i} referencing memory location {self.locations[i][0]}"
        return mem_name.write(mem_loc, data)
        