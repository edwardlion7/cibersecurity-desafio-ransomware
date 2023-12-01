import os
import Cryptodome.Cipher.AES as AES

## abrir o arquivo criptografado
file_name = "teste.txt.ransomwaretroll"
file = open(file_name, "rb")
nonce, tag, ciphertext = [ file.read(x) for x in (16, 16, -1) ]
file.close()

## chave para descriptografia
key = b"chave_secreta_cr"
cipher = AES.new(key,AES.MODE_EAX,nonce)

decrypt_data = cipher.decrypt_and_verify(ciphertext,tag)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo descriptografado
new_file = "teste.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
