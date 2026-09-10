#age classification

name = input("Enter your NAME ----> ")
age = int(input("Enter your AGE ----> "))

print("Hi," , name, "That age is considered as")
if age >= 1 and age <=5:
	print("INFANT")
elif age >=6 and age <=12:
	print("KID")
elif age >=13 and age <=19:
	print("TEENAGER")
elif age >=20 and age<=29:
	print("EARLY ADULT HOOD")
elif age >=30 and age <=48:
	print("ADULT")
elif age >= 49 and age <=59:
	print("ADVANCED ADULT")
elif age >=60 and age <=150:
	print("SENIOR")
else:
	print("INVALID")