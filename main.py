from algos import *

algo = int(input("Choose Algorithm : 1 = Ceser Ciper, 2 = Affine Ciper, 3 = PlayFair Ciper, 4 = Hill Ciper "))
msg = input("Enter text: ")
msg= msg.replace(" ","")


if(algo==1):
  shift = 3
  ask_mode = input("Enter E to Encrypt or D to Decrypt : ")
  if(ask_mode == 'E'):
    encrypt = caesar(msg,shift,'encrypt')
    print(encrypt)
  elif(ask_mode == 'D'):
    decrypt = caesar(msg,shift,'decrypt')
    print(decrypt)
  else:
    print("Invalid Mode")

elif(algo == 2):

  ask_mode = input("Enter E to Encrypt or D to Decrypt : ")
  a = int(input("Enter The Key value alpha : "))
  b = int(input("Enter The Key value beta : "))
  if(ask_mode == 'E'):
    encrypt = affine_ciper(msg,a,b,'encrypt')
    print(encrypt)
  elif(ask_mode == 'D'):
    decrypt = affine_ciper(msg,a,b,'decrypt')
    print(decrypt)
  else:
    print("Invalid Mode")

elif(algo == 3):
  key = input("Enter The Key : ")
  ask_mode = input("Enter E to Encrypt or D to Decrypt : ")
  if(ask_mode == 'E'):
    encrypt = playfair_simple(msg,key,'encrypt')
    print(encrypt)
  elif(ask_mode == 'D'):
    decrypt = playfair_simple(msg,key,'decrypt')
    print(decrypt)
  else:
    print("Invalid Mode")

elif(algo == 4):
  my_key = [[3, 3], [2, 5]]
  ask_mode = input("Enter E to Encrypt or D to Decrypt : ")
  if (ask_mode == 'E'):
    encrypt = hill_2x2(msg, my_key, 'encrypt')
    print(encrypt)
  elif (ask_mode == 'D'):
    decrypt = hill_2x2(msg, my_key, 'decrypt')
    print(decrypt)
  else:
    print("Invalid Mode")

else:
  print("Invalid Algorithm")
