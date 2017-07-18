"""
Implementation of the ADFGVX Cipher.
Ex:
	Keyword: crayon
	Keysquare:	- A D F G V X
				A 9 s 6 z l 2
				D r i n 8 m 1
				F 5 b 7 a w 4
				G c p h t y v
				V g x k o 0 f
				X q j d 3 u e

	Plaintext:    hello world!
	Ciphertext(i): GFXXAVAVVG FVVGDAAVXF!

		C  R  A  Y  O  N 		A  C  N  O  R  Y
		GF XX AV AV VG    -->   AV GF    VG XX AV
		FV VG DA AV XF !		DA FV !  XF VG AV

	Ciphertext(ii): AVGF VGXXAVDAFV!XFVGAV
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

def encrypt(keyword, keysquare, plaintext):
	pass

def decrypt(key, keysquare, ciphertext):
	pass

# -------- Place any helper functions you need here -------- #

# -------- Place any variables you need here -------- #
