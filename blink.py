# summation.py
# Compute the sum of the first 100 integer values and print
# the results.

# Initialize a constant variable.
NUM_WORDS = 0
MY_STRING = "A quick brown fox jumped over a lazy dog"

#Print the string first

print MY_STRING

length = len(MY_STRING); 

import time

# for i in range(length):
#     time.sleep(0.1)
#     print 'Downloading File FooFile.txt [%d%%]\r'%i,

# sys.stdout.write("Download progress: %d%%   \r" % (progress) )

words = MY_STRING.split();

sys.stdout.write("\n")
sys.stdout.write("\n")
sys.stdout.write("\n")

for word in words:
	NUM_WORDS = NUM_WORDS + 1
	sys.stdout.write(word)
	sys.stdout.write("     ")
	sys.stdout.write("\r")

	time.sleep(0.5)
	sys.stdout.flush()

sys.stdout.write("\n")
print(NUM_WORDS);
sys.stdout.write("Done and Done")

# Compute the sum.
# summation = 0
# i = 1
# while i < length:
#    #summation = summation + i
#    # print MY_STRING[i] 
#    sys.stdout.write(": %c   \r" % (MY_STRING[i]) )
#    # sys.stdout.write(MY_STRING[i] + "\r")

#    time.sleep(0.1)
#    sys.stdout.flush()
#    i = i + 1

# import curses  # Get the module
# stdscr = curses.initscr()  # initialise it
# stdscr.clear()  # Clear the screen

# Print the results.
# print "The sum of the first", NUM_VALUES, \
#       "integers is", summation