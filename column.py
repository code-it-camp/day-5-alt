"""
Implementation of the Columnar Transposition Cipher.
Ex:
	Key: crayon
	Plaintext:  hello world!

	C R A Y O N 	A C N O R Y
	h e l l o  	--> l h   o e l
	w o r l d !		r w ! d o l

	Ciphertext: lh oelrw!dol
"""

def init(encrypt_or_decrypt):
	"""
	Requests the required keys for this cipher and requests either the plaintext
	for an encryption or the ciphertext for a decryption.

	Args:
		encrypt_or_decrypt: equal to either "encrypt" or "decrypt",
			informs init whether we should be requesting encryption information
			or decryption information
	"""
	pass

def encrypt(key, plaintext):
	pass

def decrypt(key, ciphertext):
	pass

# -------- Place any helper functions you need here -------- #

# -------- Place any variables you need here -------- #
