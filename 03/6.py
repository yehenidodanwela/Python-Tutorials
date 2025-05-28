letter = input ("Enter a letter: ")

if ("a" <= letter <= "z"):
    if (letter in ("a", "e", "i", "o", "u")) :
        print ("Vowel")
    else :
        print ("Consonant")
else:
    print ("Enter a valid letter")
    
