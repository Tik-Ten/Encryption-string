Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] * 2 
direction = input("type 'encode' to encrypt or type 'decode' to decrypt:\n ")
text = input('what is your massage?\n').lower()
shift = int(input("type the shift number:\n"))

def encode(text,shift) :
    lent = len(text)
    textcode = []
    strcode = ""
    for i in range(lent) :
        textcode.extend(text[i])
    for i in range(lent) :
        index = Alphabet.index(textcode[i] ) + shift
        textcode[i] = Alphabet[index]
    for j in range(lent) :
       strcode += textcode[j] 




    return strcode




def decode(text,shift) :
    lent = len(text)
    textcode = []
    strcode = ""
    for i in range(lent) :
        textcode.extend(text[i])
    for i in range(lent) :
        index = Alphabet.index(textcode[i] ) - shift
        textcode[i] = Alphabet[index]
    for j in range(lent) :
       strcode += textcode[j]




    return textcode



if direction == "encode" :
    print(encode(text,shift))


else:
    print(decode(text,shift)) 