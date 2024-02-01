class Cache:

    def __init__(self):
        ##stores memory location [0] and data [1] in list
        self.j = 0
        cache_register = ['', '']
        for i in range(32):
            cache_register[0] += '0'
            cache_register[1] += '0'
        self.locations = [cache_register for i in range(128)]
    
    def __repr__(self):
        return f"Current status of cache:\n{self.locations}"
    
    def get(self, memory_name, memory_register):
        for i in range(128):
            if memory_register == self.locations[i][0]:
                print("Cache hit!")
                return self.locations[i][1]
        data = memory_name.locations[memory_register]
        empty_data = ''
        for a in range(32):
            empty_data += '0'
        i = 0
        current = self.locations[i]
        while current[0] != empty_data:
            i += 1
            if i == 128:
                current = self.locations[j]
                self.j += 1
                if self.j == 128:
                    self.j = 0
                break
        current = [memory_register, data]
        return data
    
    def write_to_mem(self):
        pass