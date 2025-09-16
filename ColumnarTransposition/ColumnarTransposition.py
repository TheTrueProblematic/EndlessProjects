
# Woohoo! It's Python time! Let's have some fun with columnar transposition cipher. 
# It's like mixing up scrambled letters to form a secret text. 
# Btw, don't worry, we'll also give you the power to unscramble the text too!
# Let's dive in! No safety gears required ;)

def create_cipher_key(keyword):
    """
    We're going to use this function to create a cipher key from a keyword.
    It's like ordering the keyword's characters alphabetically to form a new order.
    """
    keyword_list = sorted(list(set(keyword)))  # Removes duplicates and sorts
    keyword_order = [keyword.index(c) for c in keyword_list]
    return keyword_order


def create_cipher_table(text, key):
    """
    This function arranges text in a table according to our key.
    The table will have as many columns as characters in the key and rows enough to hold all characters in the text.
    """
    row_len = len(key)
    rows = [text[i: i + row_len] for i in range(0, len(text), row_len)]
    return rows


def transpose(table, key):
    """
    Get ready! Here we perform the actual columnar transposition,
    rearranging the columns of the table according to our key.
    The magic starts now!!
    """
    transposed = []
    for k in key:
        for row in table:
            try:
                transposed.append(row[k])
            except IndexError:
                continue
    return ''.join(transposed)


def encrypt(text, keyword):
    """
    And this is our superhero function tying up everything together,
    treating the text string as a long text and encrypt it using columnar transposition.
    """
    key = create_cipher_key(keyword)
    table = create_cipher_table(text, key)
    encrypted_text = transpose(table, key)
    return encrypted_text


def decrypt(cipher, keyword):
    """
    Wait, what! the superheroes got to have a sidekick, here's our decryption function,
    it 'un-mixes' the scrambled letters reordering them back into their original form.
    """
    key = create_cipher_key(keyword)
    col_len = len(cipher) // len(key)
    table = [cipher[i:i + col_len] for i in range(0, len(cipher), col_len)]
    table = [list(t) for t in zip(*table)]
    table = [table[i] for i in key]
    table = [list(t) for t in zip(*table)]
    decrypted_text = ''.join([''.join(t) for t in table])
    return decrypted_text

# Some demo fun!

demo_text = 'Hello, World!'
demo_keyword = 'python'

print("Original Text: ", demo_text)
print("Keyword/Key: ", demo_keyword)

encrypted_text = encrypt(demo_text, demo_keyword)
print("Encrypted Cipher: ", encrypted_text)

decrypted_text = decrypt(encrypted_text, demo_keyword)
print("Decrypted Text: ", decrypted_text)

# Peace, Love, Python ❤️
