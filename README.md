# OpenRSA
![Lines of Code](https://tokei.rs/b1/github/pyjatech/OpenRSA?category=code) 
![GitHub repo size](https://img.shields.io/github/repo-size/pyjatech/OpenRSA.svg)

OpenRSA is a program to encrypt and decrypt the RSA cipher. 

## Example
For example if you had a friend you wanted to communicate with through an encrypted chat using the RSA cipher. You could use the following command `newusr` and then type your friends name whos name is in this case **Bob**. After that then you need to write your message at `/users/Bob/encrypted.txt` and Bob's public key at `/users/Bob/pubkey.txt`. After that you can use the command `encrypt` and enter **Bob** to encrypt the contents of `/users/Bob/encrypted.txt`. 

## Installation
First of all, you need to install [git](https://git-scm.com) if you don't already have it.
```
$ git clone https://github.com/TheCodingGuys/OpenRSA.git
$ cd OpenRSA/
$ python3 run.py
Setting everything up...
```

### Commands
```
>>> help
encrypt - Encrypts a file to a specified user.
decrypt - Decrypts a file from a specified user.
newusr - Adds a new user to directory 'users'.
rmusr - Removes a user by name.
credits - Credits.
help - Displays this message.
exit - Terminates.

-- ADVANCED --
chkey - Changes current encryption and decryption key.
genkey - Generates a public and a private key with a specified key size.
```

## Authors
[vsp](https://github.com/vsp0) - Head-Developer
