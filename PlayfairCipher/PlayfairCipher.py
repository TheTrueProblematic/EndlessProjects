
# Hey there, Happy programmer here! We're about to embark on a super fun cryptography journey with the Playfair Cipher!
# Get your thinking cap on because we're diving deep into the wondrous world of secret codes and hidden messages.

def create_matrix(key):
    # Oh the beauty of freshly cleansed key. No duplicates, all clean!
    key = ''.join(sorted(set(key), key=key.index))

    # Let's a-Z-oom through the alphabet and create our cipher matrix.
    # But remember we're leaving out 'j' because 'i' is feeling a little jealous in the Playfair cipher.
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    matrix = []

    for e in key:
        if e in alphabet:
            matrix.append(e)
            alphabet = alphabet.replace(e, '')
    matrix += list(alphabet)

    # Voila! Matrix done and dusted! Let's split this baby up into 5*5 and take it to the playfair!
    matrix_grouped = []
    for i in range(5):
        matrix_grouped.append('')

    matrix_grouped = [matrix[n:n+5] for n in range(0, len(matrix), 5)]
    return matrix_grouped

def message_to_digraphs(message):
    # Everyday I'm shuffling... letters into pairs (digraphs)!
    message = message.replace('j', 'i')
    digraphs = [(message[n], message[n + 1]) for n in range(0, len(message) - 1, 2)]

    return digraphs

def find_position(key_matrix, letter):
    # Alright, it's exploration time! Let's dive into our matrix.
    # We're looking for that one special letter, where are you hiding buddy?
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == letter:
                # Hooray! Found our letter, we can all take a deep breath now.
                return i, j

def playfair(message, key, mode='encrypt'):
    # Tag along! We're going down the rabbit hole of hidden messages and secret codes. Get stoked!
    key_matrix = create_matrix(key)

    message = message_to_digraphs(message)
    cipher = ''
    
    for e in message:
        p1, q1 = find_position(key_matrix, e[0])
        p2, q2 = find_position(key_matrix, e[1])
        if p1 == p2:
            if mode == 'encrypt':
                cipher += key_matrix[p1][(q1 + 1) % 5] + key_matrix[p2][(q2 + 1) % 5]
            else:
                cipher += key_matrix[p1][(q1 - 1) % 5] + key_matrix[p2][(q2 - 1) % 5]
        elif q1 == q2:
            if mode == 'encrypt':
                cipher += key_matrix[(p1 + 1) % 5][q1] + key_matrix[(p2 + 1) % 5][q2]
            else:
                cipher += key_matrix[(p1 - 1) % 5][q1] + key_matrix[(p2 - 1) % 5][q2]
        else:
            cipher += key_matrix[p1][q2] + key_matrix[p2][q1]

    # Ta-da! Here's your secret message. Shhh. Don't tell anyone!
    return cipher

# Let's put our crafty playfair function to action.
# Remember, ssshhhhh. It's all very hush hush. ;)
message = 'fleeatonce'
key = 'monarchy'

print('Message: '+ message)
print('Key: '+ key)
cipher = playfair(message, key)
print('Encryption: '+ cipher)
decoded = playfair(cipher, key, mode='decrypt')
print('Decryption: '+ decoded)
