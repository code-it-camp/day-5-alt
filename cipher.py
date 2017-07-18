from shift import init as shift_init, encrypt as shift_encrypt, decrypt as shift_decrypt
from substitution import init as substitution_init, encrypt as substitution_encrypt, decrypt as substitution_decrypt
from railfence import init as railfence_init, encrypt as railfence_encrypt, decrypt as railfence_decrypt
from column import init as column_init, encrypt as column_encrypt, decrypt as column_decrypt
from vigenere import init as vigenere_init, encrypt as vigenere_encrypt, decrypt as vigenere_decrypt
from onetimepad import init as onetimepad_init, encrypt as onetimepad_encrypt, decrypt as onetimepad_decrypt
from adfgvx import init as adfgvx_init, encrypt as adfgvx_encrypt, decrypt as adfgvx_decrypt

def main():
	listed = False
	action = input("Encrypt, decrypt or quit program? (e/d/q) ").strip().lower()
	while action == "e" or action == "d":
		cipher = ""
		while cipher not in _ciphers.keys():
			if not listed:
				cipher = input("Choose cipher: ('l' lists all ciphers) ").strip().lower()
				listed = True
			else:
				cipher = input("Choose cipher: ").strip().lower()
			if cipher == "l":
				print()
				print("Ciphers:", list(_ciphers.keys()))
				print()
		if action == "e":
			encrypted = encrypt(cipher)
			print()
			print("Encrypted:")
			print(encrypted)
		elif action == "d":
			decrypted = decrypt(cipher)
			print()
			print("Decrypted:")
			print(decrypted)

		print()
		action = input("Encrypt, decrypt or quit program? (e/d/q) ").strip().lower()

def encrypt(cipher):
	return _ciphers[cipher]["encrypt"](*_ciphers[cipher]["init"]("encrypt"))

def decrypt(cipher):
	return _ciphers[cipher]["decrypt"](*_ciphers[cipher]["init"]("decrypt"))

_ciphers = {
	"shift cipher": {
		"init": shift_init,
		"encrypt": shift_encrypt,
		"decrypt": shift_decrypt
	},
	"substitution cipher": {
		"init": substitution_init,
		"encrypt": substitution_encrypt,
		"decrypt": substitution_decrypt
	},
	"railfence cipher": {
		"init": railfence_init,
		"encrypt": railfence_encrypt,
		"decrypt": railfence_decrypt
	},
	"column cipher": {
		"init": column_init,
		"encrypt": column_encrypt,
		"decrypt": column_decrypt
	},
	"vigenere cipher": {
		"init": vigenere_init,
		"encrypt": vigenere_encrypt,
		"decrypt": vigenere_decrypt
	},
	"onetimepad cipher": {
		"init": onetimepad_init,
		"encrypt": onetimepad_encrypt,
		"decrypt": onetimepad_decrypt
	},
	"adfgvx cipher": {
		"init": adfgvx_init,
		"encrypt": adfgvx_encrypt,
		"decrypt": adfgvx_decrypt
	}
}

if __name__ == '__main__':
	main()
