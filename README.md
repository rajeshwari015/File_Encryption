# File Encryption with AES Algorithm
* This is a Python script that demonstrates file encryption and decryption using the AES algorithm from the cryptography library.

## Prerequisites
* Python 3.0 installed on your system.
* The cryptography library installed. You can install it using the following command:

``` pip install cryptography```

## Usage
Run the script by executing the following command in your terminal:
``` python encryption.py```

 * You will be prompted to enter the name of the input file. Provide the path or name of the file you want to encrypt.
 * The script will generate a random key using the AES algorithm.
 * The input file will be encrypted, and the encrypted data will be saved in a file named encrypted.txt.
 * You will be prompted to enter a password for decryption.
 * The encrypted file will be decrypted using the provided password, and the decrypted data will be saved in a file named decrypted.txt.
 * The decrypted content will be displayed in the terminal.

### Note: Ensure that you remember the password used for encryption. Without the correct password, decryption will not be possible.
