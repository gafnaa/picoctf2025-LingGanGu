import ast

def unscramble(cypher):
    i = len(cypher) - 1
    while i >= 2:
        # Extract the appended sublist
        if cypher[i-1] and isinstance(cypher[i-1], list) and cypher[i-1][-1]:
            sublist = cypher[i-1][-1]
            # Remove the appended sublist
            cypher[i-1] = cypher[i-1][:-1]
            # Insert the extracted sublist back to its original position
            cypher[i-2:i-2] = sublist
        # Decrement the index
        i -= 1
    return cypher

def decode_flag(cypher):
    # First, unscramble the cypher
    unscrambled = unscramble(cypher)
    # Flatten the list and convert hex to characters
    flag = ''
    for item in unscrambled:
        if isinstance(item, list):
            for hex_val in item:
                if isinstance(hex_val, str) and hex_val.startswith('0x'):  # Ensure it's a valid hex string
                    try:
                        flag += chr(int(hex_val, 16))
                    except ValueError:
                        # Handle invalid hex values
                        pass
        elif isinstance(item, str) and item.startswith('0x'):  # Ensure it's a valid hex string
            try:
                flag += chr(int(item, 16))
            except ValueError:
                # Handle invalid hex values
                pass
    return flag

# Read the cypher data from output.txt
with open('output.txt', 'r') as file:
    cypher_data = file.read()

# Parse the cypher data (it's a string representation of a list)
cypher = ast.literal_eval(cypher_data)

# Decode the flag
flag = decode_flag(cypher)
print("Decoded Flag:", flag)