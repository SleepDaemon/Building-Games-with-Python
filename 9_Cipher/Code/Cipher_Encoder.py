lst = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

sentence = input("Enter a sentence: ")
key = int(input("Enter a key (1-51): "))

if key < 1 or key > 51:
    print("Key must be between 1 and 51")

def encoder(sentence, key):
    encoded_string = ""
    for j in range(len(sentence)):
        if sentence[j] == " ":
            encoded_string += " "
            continue
        for i in range(len (lst)):
            if sentence[j] == lst[i]:
                code_location = i + key
                if code_location > 51:
                    code_location = code_location - 52
                encoded_string += lst[code_location]
    return encoded_string

print("Original: ", sentence)

encoded_string = encoder(sentence, key)
print("Encoded String:", encoded_string)