import binascii

ciphers = [
    "2d0a0612061b0944000d161f0c1746430c0f0952181b004c1311080b4e07494852",
    "200a054626550d051a48170e041d011a001b470204061309020005164e15484f44",
    "3818101500180b441b06004b11104c064f1e0616411d064c161b1b04071d460101",
    "200e0c4618104e071506450604124443091b09520e125522081f061c4e1d4e5601",
    "304f1d091f104e0a1b48161f101d440d1b4e04130f5407090010491b061a520101",
    "2d0714124f020111180c450900595016061a02520419170d1306081c1d1a4f4601",
    "351a160d061917443b3c354b0c0a01130a1c01170200191541070c0c1b01440101",
    "3d0611081b55200d1f07164b161858431b0602000454020d1254084f0d12554249",
    "340e0c040a550c1100482c4b0110450d1b4e1713185414181511071b071c4f0101",
    "2e0a5515071a1b081048170e04154d1a4f020e0115111b4c151b492107184e5201",
    "370e1d4618104e05060d450f0a104f044f080e1c04540205151c061a1a5349484c"
]

cipher1 = "2d0a0612061b0944000d161f0c1746430c0f0952181b004c1311080b4e07494852"
cipher2 = "200a054626550d051a48170e041d011a001b470204061309020005164e15484f44"

messages = []

fw = open("results.txt", "a+")

def xor(str1, str2):
    xor_str = ""
    for char1, char2 in zip(str1, str2):
        xor_char = int(char1, 16) ^ int(char2, 16)
        xor_str += hex(xor_char)[2:]   # strip leading hex digits
    return xor_str

def drag_crib(cipher, word):
    count = 0
    for i in range(0, len(cipher), len(word)):  # split cipher into word-sized blocks and analyze
        new_cipher = cipher[i:i + len(word)]
        hex_xor = xor(new_cipher, word)
        bytes_xor = bytes.fromhex(hex_xor)
        xor_string = bytes_xor.decode("ASCII")
        fw.write('%d:%s\n' % (count, xor_string))
        print(f'{count}:{xor_string}')
        count += 1

def top_words():
    fr = open("top_words.txt", 'r')
    top_words = fr.readlines()
    fr.close()

    cipher_text = xor(cipher1, cipher2)
    
    for word in top_words:
        fw.write("\n################################\n%s\n" % word)

        word = binascii.hexlify(word.encode('utf-8'))
        word = word.decode('utf-8')

        drag_crib(cipher_text, word)

def manual_crib():
    # get and hex encode input
    word = input("\n\nEnter a crib word    :")
    fw.write("\n################################\n%s\n" % word)
    word = binascii.hexlify(word.encode('utf-8'))
    word = word.decode('utf-8')
    
    cipher_text = xor(cipher1, cipher2)
    word_xor_cipher_text = drag_crib(cipher_text, word)

def get_key():
    message = "Testing testing can you read this"
    message = binascii.hexlify(message.encode("utf-8"))
    message = message.decode('utf-8')

    xor_key = xor(message, cipher1)

    key_bytes = bytes.fromhex(xor_key)
    key_str = key_bytes.decode("ASCII")

    return key_str

def get_convo(key):
    for cipher in ciphers:
        xor_msg = xor(cipher, key)
        bytes_msg = bytes.fromhex(xor_msg)
        msg = bytes_msg.decode("ASCII")
        messages.append(msg)
    
if __name__ == "__main__":

    key = get_key()
    key = binascii.hexlify(key.encode("utf-8"))
    key = key.decode('utf-8')

    get_convo(key)

    for message in messages:
        print(message)
