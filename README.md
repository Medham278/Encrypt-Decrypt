# Encrypt-Decrypt

Created a GUI in Python with guizero to Encrypt and Decrypt text files and images.

Features:

1. It allows secure encryption of data which includes text files and images. 
2. Give different permissions to the creator(admin) and other users to whom the data is sent.
3. Text files are encrypted by using concept of ‘private key’ by creating an OTP(One Time Pad) consisting of n number of lines of random data.
4. Image files are encrypted by converting image into bytearray and then ‘XOR’ing using a fixed key.
