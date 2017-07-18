"""
Implementation of the Vigenère Cipher.
Ex:
	- A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
	A a b c d e f g h i j k l m n o p q r s t u v w x y z
	B b c d e f g h i j k l m n o p q r s t u v w x y z a
	C c d e f g h i j k l m n o p q r s t u v w x y z a b
	D d e f g h i j k l m n o p q r s t u v w x y z a b c
	E e f g h i j k l m n o p q r s t u v w x y z a b c d
	F f g h i j k l m n o p q r s t u v w x y z a b c d e
	G g h i j k l m n o p q r s t u v w x y z a b c d e f
	H h i j k l m n o p q r s t u v w x y z a b c d e f g
	I i j k l m n o p q r s t u v w x y z a b c d e f g h
	J j k l m n o p q r s t u v w x y z a b c d e f g h i
	K k l m n o p q r s t u v w x y z a b c d e f g h i j
	L l m n o p q r s t u v w x y z a b c d e f g h i j k
	M m n o p q r s t u v w x y z a b c d e f g h i j k l
	N n o p q r s t u v w x y z a b c d e f g h i j k l m
	O o p q r s t u v w x y z a b c d e f g h i j k l m n
	P p q r s t u v w x y z a b c d e f g h i j k l m n o
	Q q r s t u v w x y z a b c d e f g h i j k l m n o p
	R r s t u v w x y z a b c d e f g h i j k l m n o p q
	S s t u v w x y z a b c d e f g h i j k l m n o p q r
	T t u v w x y z a b c d e f g h i j k l m n o p q r s
	U u v w x y z a b c d e f g h i j k l m n o p q r s t
	V v w x y z a b c d e f g h i j k l m n o p q r s t u
	W w x y z a b c d e f g h i j k l m n o p q r s t u v
	X x y z a b c d e f g h i j k l m n o p q r s t u v w
	Y y z a b c d e f g h i j k l m n o p q r s t u v w x
	Z z a b c d e f g h i j k l m n o p q r s t u v w x y

	Key: apples

	Plaintext:  hello world!
	Ciphertext: htaws oogao!
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
