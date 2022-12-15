alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]
def caesar(text, shift, direction):
    CT = ""
    for i in text:
      if i in alphabet:
        P = alphabet.index(i)
        if direction == "encode":
            P = P + shift
        elif direction == "decode":
            P = P - shift
        CT += alphabet[P]
      else:
        CT+=i
    print(f"the {direction}d text is : {CT}")
  
A=True
while A:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=shift%26
  caesar(text, shift, direction)
  result=input("Do you want to continue Press 'YES' else press 'NO'").lower()
  if result =="no":
    A=False
    print("GOOD BYE")