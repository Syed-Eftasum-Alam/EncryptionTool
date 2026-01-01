import numpy as np
from mapping import *
from functions import *



def cracker(plain_text, ciper_text):

    plain_text = plain_text.upper().replace(" ", "")
    if len(plain_text) % 2 != 0:
        plain_text += "X"


    plain_text = plain_text.replace(" ", "")
    plain_num = []
    for i in plain_text:
        plain_num.append(char_to_num[i])


    ciper_numbs=[]
    ciper_text = ciper_text.upper().replace(" ", "")
    for i in ciper_text:
        ciper_numbs.append(char_to_num[i])



    ciper_matrix = np.array(ciper_numbs).reshape(2,2).T
    plaint_matrix = np.array(plain_num).reshape(2,2).T



    adj_ciper = np.array([
        [plaint_matrix[1][1], plaint_matrix[0][1] * -1],
        [plaint_matrix[1][0] * -1, plaint_matrix[0][0]]
    ])

    det = (plaint_matrix[0][0] * plaint_matrix[1][1] - plaint_matrix[0][1] * plaint_matrix[1][0])
    mi = mod_inverse(det, 26)
    if mi:
        inverse = (mi * adj_ciper) % 26
    else :
        print("Inverse not possible of the plain Text")
        return None

    key = (np.matmul(ciper_matrix, inverse)) % 26
    return key

p_text = input("Enter Text : ")
c_text = input("Enter Cipher Text : ")
Key = cracker(p_text, c_text)
print(Key)
