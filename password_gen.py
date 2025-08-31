import random 
import string 

def password_generate(min_lenth, numbers=True, spacial_char=True): 
	letter = string.ascii_letters 
	digit = string.digits
	spacial = string.punctuation 

	characters = letter
	if numbers: 
		characters += digit
	if spacial_char: 
		characters += spacial
		 

	pwd = "" 
	meets_crateria = False 	
	has_number = False 
	has_spacial = False 

	while not meets_crateria or len(pwd) < min_lenth: 
		new_char = random.choice(characters) 
		pwd += new_char
 
		if new_char in digit: 
			has_number = True 
		elif new_char in spacial: 
			has_spacial = True

		meets_crateria = True 
		if numbers: 
			meets_crateria	= has_number
		if spacial_char: 
			meets_crateria = meets_crateria and has_spacial

	return pwd

user_choice = int(input("Parol uchun uzunlik: "))
has_num = input("Parol uchun raqam qoshilsinmi (y/n)? ") == "y"
has_spcl = input("Parol uchun belgi qoshilsinmi (y/n)? ") == "y"

pwd = password_generate(user_choice, has_num, has_spcl) 

print("Sizga taqdim etilgan parol: ", pwd)  