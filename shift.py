"""
Implementation of the Shift Cipher.
Ex:
	Key: 5
		Plaintext Alphabet --> abcdefghijklmnopqrstuvwxyz
		Ciphertext Alphabet--> fghijklmnopqrstuvwxyzabcde

	Plaintext:  hello world!
	Ciphertext: mjqqt btwqi!
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
	key = None
	while not isinstance(key, int):
		key = input("Please enter a numerical shift key: ")
		try:
			key = int(key)
		except:
			key = None
	text = input("Please enter text to be " + encrypt_or_decrypt + "ed:\n")
	return (key, text)

def encrypt(key, plaintext):
	assert isinstance(key, int)
	ciphertext = ""
	for i in range(len(plaintext)):
		letter = ""
		if plaintext[i] in _alphabet:
			index = _alphabet.index(plaintext[i])
			letter = _alphabet[(index + key) % 26]
		else:
			letter = plaintext[i]

		ciphertext += letter

	return ciphertext

def decrypt(key, ciphertext):
	assert isinstance(key, int)
	plaintext = ""
	for i in range(len(ciphertext)):
		letter = ""
		if ciphertext[i] in _alphabet:
			index = _alphabet.index(ciphertext[i])
			letter  = _alphabet[(26 + index - key) % 26]
		else:
			letter = ciphertext[i]

		plaintext += letter
	return plaintext

# -------- Place any helper functions you need here -------- #

# -------- Place any variables you need here -------- #

_alphabet = "abcdefghijklmnopqrstuvwxyz"
