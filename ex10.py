tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

test = """
a\\b\'c\"d\ae\bf\fg\nh\ri\tj\vklmnopqrstuvwxyz

"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print test

while Ture:
	for i in["/","-","\\","|"]:
		print "%s\r" % i,