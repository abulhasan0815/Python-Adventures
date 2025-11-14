print("Project Crypto")

def enigma_light():
# create keys string
    keys = "abcdefghijklmnopqrstuvwxyz !?.,"
    values = keys[-4 : -1] + keys[0 : -4]
# create two dictionaries
    dict_encryption = dict(zip(keys, values))
    dict_decryption = dict(zip(values, keys))
# OR create 1 and then flip 
#   dict_decryption = {value:key for key, value in dict_encryption.items()} 
#user input 'the message' and mode
    message = input("Enter your secret message quietly: ")
    mode = input("Crypto mode: encode (e) OR decrypt as default: ")
# run encode or decode
    if mode.lower() == 'e':
        newMessage = ''.join([dict_encryption[char] for char in message.lower()])
    else:
        newMessage = ''.join([dict_decryption[char] for char in message.lower()])

    return newMessage.capitalize()    
    
print(enigma_light())