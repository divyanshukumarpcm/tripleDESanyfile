# tripleDESanyfile

Application demo video - https://youtu.be/qRKkrRrsw84

Aim to develop a DES based encryption method to encrypt any kind of file.
AND ALSO CONVERTING TO STANDALONE SINGLE APPLICATION FOR WINDOWS, LINUX, MAC OS SEPERATELY.

IMPLEMENTED ON PYTHON 3.9.2
Libraries: -
getpass (inbuilt python 3.9.2)
pycrypto (2.6.1)
(Make sure you install and build all the depedencies required by above libraries)


Tested on Linux and Windows based systems. Will surely work on MAC OS if u install all dependencies.
Can encrypt any kind of file (image, video also), you do not have to choose or do anything extra, just type the name of the file with correct format.
Capability: - Max 300 MB file on 4GB RAM (i3 7th Gen 2.3 GHz processor)


FEATURES: - 

Password hashing - PBKDF2 used(I will welcome advanced modes)
Salting done
Hashing and salting password performed multiple times (>10,000)
Peppering not done as it increases load in server, faster method are welcome
Digital signature in form of SHA256 used
Documentation provided in code
CBC (Cipher block chaining used) - triple DES
Initialization vector for CBC is derived from the password hash itself.



Tested on Linux and Windows based systems.


IT WILL BE VERY NICE OF YOU IF MENTION MY NAME WHEREVER YOU USE THIS OR PART OF THE CODE. ALTHOUGH IT IS NOT NECESSARY BUT I HAVE WORKED HARD FOR THIS FOR MORE THAN 100 HOURS RESEARCHING, CODING, DOCUMENTING.
