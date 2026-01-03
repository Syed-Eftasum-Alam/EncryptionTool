from mapping import char_to_num, num_to_char
from functions import  *


def caesar(text, shift, mode='encrypt'):

    if mode == 'decrypt':
        shift = -shift

    result = ""
    text = text.upper()

    for char in text:
        if char in char_to_num:
            # 1. Lookup the number
            number = char_to_num[char]
            # 2. Shift and Wrap around 26
            shifted_number = (number + shift) % 26
            # 3. Lookup the new letter
            result += num_to_char[shifted_number]
        else:
            # Keep spaces/symbols as they are
            result += char

    return result


def affine_ciper(text, a, b, mode='encrypt'):

    if (co_prime(a,26)==False):

      return False

    else:

      result = ""
      text = text.upper()

      if mode=='decrypt':
        for char in text:
            if char in char_to_num:
                # 1. Lookup the number
                number = char_to_num[char]
                # 2. Shift and Wrap around 26
                decrypted_value = (mod_inverse(a,26) * (number-b)) % 26
                # 3. Lookup the new letter
                result += num_to_char[decrypted_value]
            else:
                # Keep spaces/symbols as they are
                result += char

      else:
        for char in text:
            if char in char_to_num:
                # 1. Lookup the number
                number = char_to_num[char]
                # 2. Shift and Wrap around 26
                encrypted_value = ((number * a)+b) % 26
                # 3. Lookup the new letter
                result += num_to_char[encrypted_value]
            else:
                # Keep spaces/symbols as they are
                result += char

      return result



#playfair Ciper

def get_grid(key):
    # 1. Create a 25-letter alphabet (no J)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    combined = ""
    # 2. Add key letters first, then the rest of the alphabet
    for char in key.upper().replace("J", "I"):
        if char not in combined and char.isalpha():
            combined += char
    for char in alphabet:
        if char not in combined:
            combined += char

    # 3. Turn the 25 letters into a 5x5 grid
    return [list(combined[i:i+5]) for i in range(0, 25, 5)]

def find_letter(grid, letter):
    # Find the (row, col) coordinates of a letter
    for r in range(5):
        for c in range(5):
            if grid[r][c] == letter:
                return r, c

def playfair_simple(text, key, mode='encrypt'):
    grid = get_grid(key)
    text = text.upper().replace("J", "I").replace(" ", "")

    # If the text has an odd number of letters, add an 'X'
    if len(text) % 2 != 0:
        text += "X"

    result = ""
    shift = 1 if mode == 'encrypt' else -1

    # Process letters in pairs (2 at a time)
    for i in range(0, len(text), 2):
        r1, c1 = find_letter(grid, text[i])
        r2, c2 = find_letter(grid, text[i+1])

        if r1 == r2:
            # Rule 1: Same row, move right
            result += grid[r1][(c1 + shift) % 5]
            result += grid[r2][(c2 + shift) % 5]
        elif c1 == c2:
            # Rule 2: Same column, move down
            result += grid[(r1 + shift) % 5][c1]
            result += grid[(r2 + shift) % 5][c2]
        else:
            # Rule 3: Form a box, swap corners
            result += grid[r1][c2]
            result += grid[r2][c1]

    return result

def hill_2x2(text, key_matrix, mode='encrypt'):

    # Clean text
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += "X" 

 
    a, b = key_matrix[0]
    c, d = key_matrix[1]
    
    print( 'Key Matrix:', key_matrix)

    if mode == 'decrypt':

        det = (a * d - b * c) % 26
        det_inv = mod_inverse(det, 26)
        if det_inv is None:
            return "Error: Determinant has no inverse (invalid key)."

  
        a, b, c, d = (d * det_inv) % 26, (-b * det_inv) % 26, (-c * det_inv) % 26, (a * det_inv) % 26

    result = ""
    # Process text in pairs
    for i in range(0, len(text), 2):

        p1 = char_to_num[text[i]]
        p2 = char_to_num[text[i+1]]
        pair_matrix = [p1, p2]

  
        
        res_0 = ((pair_matrix[0] * key_matrix[0][0]) + (pair_matrix[1] * key_matrix[1][0])) % 26
        res_1 = ((pair_matrix[0] * key_matrix[0][1]) + (pair_matrix[1] * key_matrix[1][1])) % 26  
   
  

        result += num_to_char[res_0] + num_to_char[res_1]
       

    return result