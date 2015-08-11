line_break = '\n-----------------------------------------\n'
indent = '    '

print(line_break + '\t\tPart 1 ' + line_break); 
print('Morpheus:')
print('I see it in your eyes.\nYou have the look of a man who accepts what he sees because he is expecting to wake up.\nIronically, that\'s not far from the truth.\nDo you believe in fate, ____?\n')

# Now ask for input
valid_input = False;
while(not valid_input):
	main_character = raw_input('INSTRUCTIONS: Do you know what should go in the blank? If you do, type it in and then press ENTER. \n\n'+indent+'main_character = ') # or`input("Some...`
	if(main_character == ""):
		print('\nHey! You gotta type something.')
	elif ('Neo' in main_character or 'neo' in main_character):
		print('\nGreat! You got it.')
		valid_input = True;
	else:
		print("\nSorry, that's not it.")
		valid_input = True;


print("Here's the answer:")
print("  main_character = Neo\n")
main_character = "Neo";

raw_input('Press the ENTER key to to see how Neo responds.') # or`input("Some...`

print line_break + '\t\tPart 2 ' + line_break;

print(main_character + ': No.')
print('Morpheus: Why not?\n' +
main_character + ": Because I don't like the idea that I'm not in control of my life.")

print("\nMorpheus:")
print("I know *exactly* what you mean. Let me tell you why you're here.\nYou're here because you know something. What you know you can't explain, but you feel it.\nYou've felt it your entire life, that there's something wrong with the world.\nYou don't know what it is, but it's there, like a splinter in your mind, driving you mad.\nIt is this feeling that has brought you to me.\nDo you know what I'm talking about?\n")

movie_name = raw_input('INSTRUCTIONS: Do you know the name of this movie? If you do, type it in. \n\n'+indent+'movie_name = ') # or`input("Some...`

valid_input = False;
while(not valid_input):
	if(main_character == ""):
		print('\nHey! You gotta type something.')
	elif ('Matrix' in movie_name or 'matrix' in movie_name):
		print('\nGreat! You got it.')
		valid_input = True;
	else:
		print("\nNope. That's not it.")
		valid_input = True;

	print("The movie is The Matrix!\n")

raw_input('Press the ENTER key.') # or`input("Some...`
print(line_break)
movie_year = raw_input('INSTRUCTIONS: What year was this movie released?\n\n'+indent+'movie_year = ')

valid_input = False;
while(not valid_input):
	if(main_character == ""):
		print('\nHey! You gotta type something.')
	elif ('1999' in movie_year):
		print('\nYup! That\'s it.')
		valid_input = True;
	else:
		print("\nNope. This is the answer:\n  movie_year = 1999")
		valid_input = True;
print(line_break)
print("Yay! You finished. Go to this link to take a look at the code behind this! \n")

