Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def direc():
    direction = input("type \"enc\" to encrypt or type \"dec\" to decrypt: ")
    # check direction
    if direction == "enc" or direction == "dec": return direction
    else: print("Unknow answer!"), exit()
direction = direc()
message = input('what is your massage? ').lower()
try: shift = int(input("type the shift number: "))
except: print("Unknow answer!"), exit()
if direction == "enc":
    message_len = len(message)
    for i in range(message_len):
        try:
            index = int(Letters.index(message[i]) + shift)
            if index > 26: Distance = index - 26, print(f"Number {i + 1}: " + Letters[Distance])
            elif index < 26: print(f"Number {i + 1}: " + Letters[index])
        except: print(f"Number {i + 1}: " + message[i])
elif direction == "dec":
    message_len = len(message)
    for i in range(message_len):
        try:
            index = int(Letters.index(message[i]) - shift)
            if index < 0: Distance = index + 26, print(f"Number {i + 1}: " + Letters[Distance])
            else: print(f"Number {i + 1}: " + Letters[index])
        except: print(f"Number {i + 1}: " + message[i])





# Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] * 2 
# direction = input("type 'encode' to encrypt or type 'decode' to decrypt:\n ")
# text = input('what is your massage?\n').lower()
# shift = int(input("type the shift number:\n"))
# def encode(text,shift) :
#     lent = len(text)
#     textcode = []
#     strcode = ""
#     for i in range(lent) :
#         textcode.extend(text[i])
#     for i in range(lent) :
#         index = Alphabet.index(textcode[i] ) + shift
#         textcode[i] = Alphabet[index]
#     for j in range(lent) :
#        strcode += textcode[j] 
#     return strcode
# def decode(text,shift) :
#     lent = len(text)
#     textcode = []
#     strcode = ""
#     for i in range(lent) :
#         textcode.extend(text[i])
#     for i in range(lent) :
#         index = Alphabet.index(textcode[i] ) - shift
#         textcode[i] = Alphabet[index]
#     for j in range(lent) :
#        strcode += textcode[j]
#     return textcode
# if direction == "encode" :
#     print(encode(text,shift))
# else:
#     print(decode(text,shift)) 