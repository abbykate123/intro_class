name1 = "Abby"
name2 = "Honey"

if name1 > name2:
	print "My name is greater!"
elif name1 < name2:
	print "Their name is greater."
else:
	print "Our names are equal!" 
----------------------
today = raw_input("day of the week ") 
	
if today == "Monday":
	print "Yaaas Monday! Here we go!" 

elif today == "Tuesday":
	print "Sigh, it's only Tuesday."

elif today == "Wednesday":
	print "Humpday!"

elif today == "Thursday":
	print "#tbt"

elif today == "Friday":
	print "TGIF!"
else: 
	print "Yeah, it's the weekend!"
Ask how to deal with the code is like FRIDAY "Yeah its the weekend!"
-------------------
age = raw_input("What is your age? ")

if age <= 18:
	print "Yay! I can vote!"
----------------------
age = int(raw_input("What is your age? "))
if age >= 18:
	print "Yay! I can vote!"
else:
	print "Aww, I cannot vote."
----------------------------
age = int(raw_input("What is your age? "))
if age >= 18 and age >= 21:
	print "I can vote and got to a bar!"
----------------------------
age = int(raw_input("What is your age? "))
if age >= 21:
	print "I can vote and go to a bar!"
elif age >= 18:
	print "I can vote but I cannot go to a bar."
-----------------------------
age = int(raw_input("What is your age? "))
if age >= 21:
	print "I can vote and go to a bar!"
elif age >= 18:
	print "I can vote but I cannot go to a bar."
else:
	print "I cannot vote or go to a bar."
--------------------------------
num = int(raw_input("Give me a number. "))
if int(num) % 2 == 0:
	print "The number is Even"
else:
	print "The number is Odd"
---------------------------------
num = int(raw_input("Give me a number. "))
if int(num) % 2 == 1:
	print "The number is Odd"
else:
	print "The number is Even"
------------------------------------
if 8 % 2 == 0 and 9 % 2 == 0:
	print "Both numbers are even."
else:
	print "Both numbers are odd."
------------------------------
if 8 % 2 == 0 and 9 % 2 == 0:
	print "Both numbers are even."
elif 8 % 2 == 0 and 9 % 2 == 1:
	print "8 is even and 9 is odd."
else:
	print "Both are odd."
-------------------------------
color = raw_input("What is your favorite color? ")
if color == "blue":
	print "My favorite color is blue!"
else:
	print "My favorite color is not blue." 
--------------------------------
color = raw_input("What is your favorite color? ").lower()
if color == "red" or color == "yellow" or color == "blue":
	print "My favorite color is primary color."
else:
	print "My favorite color is a secondary color."