def rubik_encrypt(plaintext, moves):
    blocks = [plaintext[i:i+9] for i in range(0, len(plaintext), 9)]
    result = ""
    for block in blocks:
        padded = block.ljust(9, 'X')
        cube = [list(padded[i:i+3]) for i in range(0, 9, 3)]
        for move in moves:
            if move == 'R':
                cube[0][2], cube[1][2], cube[2][2] = cube[2][2], cube[0][2], cube[1][2]
            elif move == 'L':
                cube[0][0], cube[1][0], cube[2][0] = cube[1][0], cube[2][0], cube[0][0]
            elif move == 'U':
                cube[0][0], cube[0][1], cube[0][2] = cube[0][2], cube[0][0], cube[0][1]
            elif move == 'D':
                cube[2][0], cube[2][1], cube[2][2] = cube[2][1], cube[2][2], cube[2][0]
        result += ''.join([''.join(row) for row in cube])
    return result

def rubik_decrypt(ciphertext, moves):
    blocks = [ciphertext[i:i+9] for i in range(0, len(ciphertext), 9)]
    result = ""
    for block in blocks:
        cube = [list(block[i:i+3]) for i in range(0, 9, 3)]
        for move in reversed(moves):
            if move == 'R':
                cube[0][2], cube[1][2], cube[2][2] = cube[1][2], cube[2][2], cube[0][2]
            elif move == 'L':
                cube[0][0], cube[1][0], cube[2][0] = cube[2][0], cube[0][0], cube[1][0]
            elif move == 'U':
                cube[0][0], cube[0][1], cube[0][2] = cube[0][1], cube[0][2], cube[0][0]
            elif move == 'D':
                cube[2][0], cube[2][1], cube[2][2] = cube[2][2], cube[2][0], cube[2][1]
        result += ''.join([''.join(row) for row in cube])
    return result.rstrip('X')

# Example usage:
if __name__ == "__main__":
    plaintext = "SECRET"
    key_moves = ["R", "U"]

    encrypted = rubik_encrypt(plaintext, key_moves)
    print("Encrypted:", encrypted)

    decrypted = rubik_decrypt(encrypted, key_moves)
    print("Decrypted:", decrypted)
