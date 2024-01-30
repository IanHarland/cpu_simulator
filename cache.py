class Cache:

    def __init__(self):
        ##stores memory location and instruction
        self.locations = [(0b000000000, 0b000000000000) for i in range(2**5)]
    
    def __repr__(self):
        return f"Current status of cache:\n{self.locations}"
    
    def get(self, memory_name, memory_location):
        instruction = memory_name.locations[memory_location]
        i = 0
        current = self.locations[i]
        while current[0] != 0:
            i += 1
            if i == 32:
                current = self.locations[0]
                break
        current = (memory_location, instruction)