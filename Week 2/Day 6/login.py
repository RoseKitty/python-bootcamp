#HASHING IS FUN~~

import hashlib
import time
#make a login system
username = input("Enter a username: ")
password = "password123!"

#print(f"Oringinal password is:{password}")
password = password.encode()#uft8 plaintext, letters and 0-9. utf-16 ->+asian chars. utf-??
hashed_pass = hashlib.sha256(password).hexdigest()
#print(f"hashed password is: {hashed_pass}")

tries = 3
wait_time = 5 #this is in seconds

successful = False

while tries >= 1 and successful == False: 
	attempt = input("Type in your password: ")
	attempt = attempt.encode() #to ensure format
	hashed_attempt = hashlib.sha256(attempt).hexdigest()
	if hashed_attempt != hashed_pass:
		#fail to log in 
		tries -= 1
		print("Incorrect password. Try again.")
		print(f"You have {tries} left")
	else: 
		print("Successfully logged in")
		successful = True 
#still need to implement the wait time
