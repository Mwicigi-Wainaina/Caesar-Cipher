alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue=True

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for char in plain_text:
    if char in alphabet: 
      position = alphabet.index(char)
      new_position = position+shift_amount
      new_char = alphabet[new_position]
      cipher_text += new_char
    else: 
      cipher_text += char
  print (f"The encoded text is {cipher_text}")
def decrypt (plain_text, shift_amount):
  decoded_text = ""
  for char in plain_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position-shift_amount
      new_char = alphabet[new_position]
      decoded_text += new_char
    else:
      decoded_text += char
  print (f"The decoded text is {decoded_text}")


while should_continue is True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  plain_text = input("Type your message:\n").lower()
  shift_amount = int(input("Type the shift number:\n"))%26
  if direction=="encode":
    encrypt(plain_text, shift_amount)
  if direction=="decode":
    decrypt(plain_text, shift_amount)
  run_again=input("Type 'yes' to run again, type 'no' to end program ")
  print("\n")
  if run_again == 'no':
    should_continue=False
    print("Goodbye!")
