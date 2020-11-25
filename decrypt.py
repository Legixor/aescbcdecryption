from Crypto.Cipher import AES
import sys
import base64
### KEY VAR ###
key = b'RXZpbERlZmF1bHRQWYXNzIQ=='
###VECTOR VAR###
vec = bytearray([0,1,0,3,5,3,0,1,0,0,2,0,6,7,6,0])


###MAIN ###
def main(filename):
    ###OPENING THE FILE###
    with open(filename, 'rb') as file:
        content = file.read()
        file.close()
    
aes = AES.new(base64.b64decode(key), AES.MODE_CBC, vec)
###BLOC SIZE VAR ###
aes.block_size = 128
text = aes.decrypt(content)
 
 res_filename = filename[:-5]
 with open(res_filename, 'wb') as file:
     file.write(text)
     file.close()


if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Utilisation du script: decrypt.py <file>")
    else:
        main(sys.argv[1])
