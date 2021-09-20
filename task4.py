#!python3
 
"""
Assignment 5:
Make a Mad Lib

Ask the user to enter a number of words, one for each of the underscored words in the following paragraph.  Once they have finished, display the following story to them with the replacements made in the Mad Lib

Today we picked apple from _PERSON_'s Orchard. I had no idea there were so many different varieties of apples. I ate _ADJECTIVE_ apples straight off the tree that tasted like _FOOD_. Then there was a _ADJECTIVE_ apple that looked like a _NOUN_.  When our bag was full, we went on a free hay ride to _PLACE_ and back. It ended at a hay pile where we got to _VERB_ _ADVERB_. I can hardly wait to get home and cook with the apples. We are going to make apple _FOOD_ and _THINGS_ pies!
"""

name1 = input("Enter a name: ").strip()

adjective1 = input("Enter a adjective: ").strip()

food1 = input("Enter the name of a food: ").strip()

adjective2 = input("Enter another adjective: ").strip()

noun1 = input("Enter a noun: ").strip()

place1 = input("Enter a place: ").strip()

verb1 = input("Enter a verb: ").strip()

adverb1 = input("Enter a adverb: ").strip()

food2 = input("Enter another name of a food: ").strip()

thing1 = input("Enter a thing: ").strip()

print(f"Today we picked apple from {name1}'s Orchard. I had no idea there were so many different varieties of apples. I ate {adjective1} apples straight off the tree that tasted like {food1}. Then there was a {adjective2} apple that looked like a {noun1}.  When our bag was full, we went on a free hay ride to {place1} and back. It ended at a hay pile where we got to {verb1} {adverb1}. I can hardly wait to get home and cook with the apples. We are going to make apple {food2} and {thing1} pies!")