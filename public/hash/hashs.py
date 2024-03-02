# You are not allowed to use any known hash functions!!!
# I recommend you to use numpy for any arithmatic operation

# BTW- I checked if chatGPT knows how to generate it's own hash function.abs
# He really can't, I mean he generated some bad functions eve after I told him how to improve them.abs
# Good Luck!

# This class is exposed to everyone in the world. A hash is not hidden.
class Hash:
    def __init__(self):
        pass

    # Implement your first hash function here
    # Example implementation: Convert string to ASCII and XOR the values
    def hash_function1(self, input_string):
        hash_value = 0
        for char in input_string:
            hash_value ^= ord(char)
        return hash_value & 0xFFFFFF  # 24-bit mask

    # Implement your second hash function here
    # Example implementation: Take the least significant byte
    def hash_function2(self, input_number):
        return input_number & 0xFF  # 8-bit mask

    # Implement your third hash function here
    # Example implementation: Length of the string
    def hash_function3(self, input_string):
        return len(input_string)

