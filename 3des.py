#author:Divyanshu Kumar, ECE(2019-2023), NIT Silchar 
#email-divyanshu_ug@ece.nits.ac.in
#Date:  21 May 2021
#Demo video of usage - https://youtu.be/qRKkrRrsw84


#--------------------Python and Library version used---------------
# Pyhton 3.9.2
#Pycrypto 2.6.1
#getpass (inbuilt python 3.9.2)




#Password hashing Iterations - KEEP CONSTANT through out this application existence.
pi=100005

#password SALT, This variable should remain constant throught out this application life. This will make RAINBOW HASH TABLES USELESS
#For deactivating salting, just leave salt="" i.e. blank in paranthesis.
#DO NOT CHANGE BELOW VALUE AT ANY COST-------------------------------------------------------------------------------------------
salt_const=b"$ez*}-d3](%d%$#*!)$#%s45le$*fhucdivyanshu75456dgfdrrrrfgfs^"
#DO NOT CHANGE ABOVE VALUE AT ANY COST-------------------------------------------------------------------------------------------










#importing libraries
from Crypto.Cipher import DES
from Crypto.Hash import SHA256
from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2











#encrypting function
def encryptor(path):
	#opening the image file
	try:
		with open(path, 'rb') as imagefile:
			image=imagefile.read()
			
		#padding	
		while len(image)%8!=0:
			image+=b" "
	except:
		print("Error loading the file, make sure file is in same directory, spelled correctly and non-corrupted")
		exit()
	
	#hashing original image in SHA256	
	hash_of_original=SHA256.new(data=image)
	
	
	
	#Inputting Keys
	key_enc=getpass(prompt="		      Enter minimum 8 character long password:")
	#Checking if key is of invalid length
	while len(key_enc)<8:
		key_enc=getpass(prompt="		      Invalid password! Enter atleast 8 character password:")
	
	key_enc_confirm=getpass(prompt="		       Enter password again:")
	while key_enc!=key_enc_confirm:
		print("Key Mismatch.Try again.")
		key_enc=getpass(prompt="		      Enter 8 character long password:")
	
		#Checking if key is of invalid length
		while len(key_enc)<8:
			key_enc=getpass(prompt="		      Invalid password! Enter atleast 8 character password:")
		key_enc_confirm=getpass(prompt="		       Enter password again:")
	
	
	#Salting and hashing password
	key_enc=PBKDF2(key_enc,salt_const,48,count=pi)

	
	#Encrypting using triple 3 key DES	
	print("			encrypting...")	
	try:
		
		cipher1=DES.new(key_enc[0:8],DES.MODE_CBC,key_enc[24:32])
		ciphertext1=cipher1.encrypt(image)
		cipher2=DES.new(key_enc[8:16],DES.MODE_CBC,key_enc[32:40])
		ciphertext2=cipher2.decrypt(ciphertext1)
		cipher3=DES.new(key_enc[16:24],DES.MODE_CBC,key_enc[40:48])
		ciphertext3=cipher3.encrypt(ciphertext2)
		print("			!!!ENCRYPTION SUCCESSFUL!!!")
	except:
		print("			Encryption failed...Possible causes:Library not installed properly/low device memory/Incorrect padding or conversions")
		exit()
	
	#Adding hash at end of encrypted bytes
	ciphertext3+=hash_of_original.digest()

	
	#Saving the file encrypted
	try:
		dpath="encrypted_"+path
		with open(dpath, 'wb') as image_file:
    			image_file.write(ciphertext3)
		print("			Encrypted Image Saved successfully as filename "+dpath)
    		
		
	except:
		temp_path=input("			Saving file failed!. Enter alternate name without format to save the encrypted file. If it is still failing then check system memory")
		try:
			dpath=temp_path+path
			dpath="encrypted_"+path
			with open(dpath, 'wb') as image_file:
    				image_file.write(ciphertext3)
			print("			Encrypted Image Saved successfully as filename "+dpath)
			exit()
		except:
			print("			Failed....Exiting...")
			exit()



















#decrypting function
def decryptor(encrypted_image_path):
	
	try:
		with open(encrypted_image_path,'rb') as encrypted_file:
			encrypted_data_with_hash=encrypted_file.read()
			
	except:
		print("			Unable to read source cipher data. Make sure the file is in same directory...Exiting...")
		exit()
	
	
	#Inputting the key
	key_dec=getpass(prompt="		      Enter password:")
	
	
	#extracting hash and cipher data without hash
	extracted_hash=encrypted_data_with_hash[-32:]
	encrypted_data=encrypted_data_with_hash[:-32]

	
	#salting and hashing password
	key_dec=PBKDF2(key_dec,salt_const,48,count=pi)
	

	#decrypting using triple 3 key DES
	print("			Decrypting...")
	try:
		
		cipher1=DES.new(key_dec[16:24],DES.MODE_CBC,key_dec[40:48])
		plaintext1=cipher1.decrypt(encrypted_data)
		cipher2=DES.new(key_dec[8:16],DES.MODE_CBC,key_dec[32:40])
		plaintext2=cipher2.encrypt(plaintext1)
		cipher3=DES.new(key_dec[0:8],DES.MODE_CBC,key_dec[24:32])
		plaintext3=cipher3.decrypt(plaintext2)
		
		
	except:
		print("			Decryption failed...Possible causes:Library not installed properly/low device memory/Incorrect padding or conversions")
		
	
	
	
	
	#hashing decrypted plain text
	hash_of_decrypted=SHA256.new(data=plaintext3)

	
	#matching hashes
	if hash_of_decrypted.digest()==extracted_hash:
		print("Password Correct !!!")
		print("			DECRYPTION SUCCESSFUL!!!")
	else:
		print("Incorrect Password!!!")
		exit()
		
		
		
	#saving the decrypted file	
	try:
		epath=encrypted_image_path
		if epath[:10]=="encrypted_":
			epath=epath[10:]
		epath="decrypted_"+epath
		with open(epath, 'wb') as image_file:
			image_file.write(plaintext3)
		print("			Image saved successully with name " + epath)
		print("			Note: If the decrypted image is appearing to be corrupted then password may be wrong or it may be file format error")
	except:
		temp_path=input("			Saving file failed!. Enter alternate name without format to save the decrypted file. If it is still failing then check system memory")
		try:
			epath=temp_path+encrypted_image_path
			with open(epath, 'wb') as image_file:
				image_file.write(plaintext3)
			print("			Image saved successully with name " + epath)
			print("			Note: If the decrypted image is appearing to be corrupted then password may be wrong or it may be file format error")
		except:
			print("			Failed! Exiting...")
			exit()
















#Documentations
print("--------------------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------IMAGE ENCRYPTOR DECRYPTOR TOOL triple-DES-------------------------------------------")
print("")
print("")
print("		        You need to provide atleast 8 character long password for secure ")
print("		        encryption.")
print("		        Choose a strong and non-repeating password for best security.")
print("		        This app is capable of encrypting ANY KIND OF FILE <300 MB on 4GB RAM.")
print("		        With bigger RAM, it can encrypt files larger than that.")
print("")
print("")
print("")
print("")
print("		        CBC Method is applied in this program. The files on which operations are being ")
print("		        performed should be in same folder. The encrypted and decrypted files by default are saved as")
print("		        encrypted_originalname.originalformat and decrypted_originalname.originalformat respectively. ")
print("		        In some cases, file format error during decryption may occur if image was not encrypted using this program.")
print("		        The encrypted file is saved in same format as original.")
print("")
print("")



















#--------------------------------------MAIN PROGRAM-----------------------------------------------
#Mode selection
try:
	choice=int(input("		Press 1 for Encryption || 2 for Decryption: "))
	while choice!=1 and choice!=2:
		choice=int(input("		      Invalid Choice! Try Again:"))
except:
	print("Error, please provide valid Input")
	exit()



if choice==1:
#Encryption Mode, function call
	path=input("		Enter image's name to be encypted:")
	encryptor(path)
		


else:
#Decryption mode, function call
	encrypted_image_path=input("		Enter file name to decrypted:")
	decryptor(encrypted_image_path)

print("")
print("")
print("-------------------------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------------------------")
