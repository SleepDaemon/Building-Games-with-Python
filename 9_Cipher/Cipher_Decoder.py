lst = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

sentence = input("Enter the encoding: ")
key = int(input("Enter a key (1-51): "))

if key < 1 or key > 51:
    print("Key must be between 1 and 51")

def decoder(sentence, key):
    decoded_string = ""
    for j in range(len(sentence)):
        if sentence[j] == " ":
            decoded_string += " "
            continue
        for i in range(len (lst)):
            if sentence[j] == lst[i]:
                code_location = i - key
                if code_location < 0:
                    code_location = code_location + 52
                decoded_string += lst[code_location]
    return decoded_string

print("Original: ", sentence)

decoded_string = decoder(sentence, key)
print("Decoded String:", decoded_string)