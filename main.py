# Create list of letters
Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]  # 26 Letter
# Create values:
dot = "."
# get direction
def direc():
    direction = input("type \"enc\" to encrypt or type \"dec\" to decrypt: ")
    # check direction
    if direction == "enc" or direction == "dec": return direction
    else: print("Unknow answer!"), exit()
direction = direc()
# get user message
message = input('what is your massage? ').lower()
# try for get int input
try: shift = int(input("type the shift number: "))
except: print("Unknow answer!"), exit()
if direction == "enc":
    message_len = len(message) - 1
    counter = 0
    for i in range(message_len):
        try:
            index = int(Letters.index(message[counter]) + shift)
        except:
            print(f"Number {counter + 1}: " + message[i])
        if index > 26:
            Distance = index - 26
            print(f"Number {counter + 1}: " + Letters[Distance])
            break
        else:
            print(f"Number {counter + 1}: " + Letters[index])
        counter += 1
elif direction == "dec":
    message_len = len(message)
    counter = 0
    for i in range(message_len):
        try:
            index = int(Letters.index(message[counter]) - shift)
        except:
            print(f"Number {counter + 1}: " + message[i])
        if index < 0:
            Distance = index + 26
            print(f"Number {counter + 1}: " + Letters[Distance])
        else:
            print(f"Number {counter + 1}: " + Letters[index])
        counter += 1

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