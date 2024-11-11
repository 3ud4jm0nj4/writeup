def djb2_hash(string):
    hash_value = 0x1505
    for char in string:
        hash_value = (hash_value *33) + ord(char)
    return hash_value & 0xFFFFFFFF  # Limit the hash value to a 32-bit unsigned integer

# Example usage
input_string = "VerY"
hash_result = djb2_hash(input_string)
print(f"The DJB2 hash of '{input_string}' is: {hex(hash_result)}")
