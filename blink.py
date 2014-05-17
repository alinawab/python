# summation.py
# Compute the sum of the first 100 integer values and print
# the results.

import time
import sys


def ORP(n):
    percentage = 0.45
    return int(math.ceil(n * 0.45))

def calculate_spaces(word, maxLength):
    maxOrp = ORP(maxLength) # index + 1
    orp = ORP(len(word)) # index + 1
    prefixSpace = maxOrp - orp
    postfixSpace = maxLength - len(word) - prefixSpace
    
    return (orp, prefixSpace, postfixSpace)

def print_word(word, orpConfig):
    def insert_color(word, orpIndex):
        colorCode_red = "\033[91m"
        colorCode_restore = "\033[0m"

        return word[0:orpIndex] + colorCode_red + word[orpIndex] + colorCode_restore + word[orpIndex+1:]
        
    # orp, prefix, postfix = orpConfig
    orp = orpConfig
    prefix = orpConfig
    postfix = orpConfig
    stringToPrint = " " * prefix + insert_color(word, orp-1) + " " * postfix

    print ("\r%s" % stringToPrint end='')
    print ("\r%s" % stringToPrint)
    sys.stdout.flush()    

def find_max(reading):
    reading = sorted(reading, key=lambda x: len(x), reverse=True)
    return len(reading[0])

def parse_article(article):
    """
    argument: article::string
    returns: [ word::string | sign::string ]

    word :: single word
    sign :: <pause>
    """
    charToRemoved = ",.!\xad"

    for eachChar in charToRemoved:
        article = article.replace(eachChar, "")

    article = article.strip()
    article = article.replace("\n", " <pause> ")

    return article.split()


# Initialize a constant variable.
NUM_WORDS = 0
MY_STRING = "John David Chibuk is calling"

#Print the string first

print MY_STRING

length = len(MY_STRING); 

words = MY_STRING.split();

sys.stdout.write("\n")
sys.stdout.write("\n")
sys.stdout.write("\n")

for word in words:
	NUM_WORDS = NUM_WORDS + 1
	# sys.stdout.write(word)

	print_word(word, 3)

	sys.stdout.write("     ")
	sys.stdout.write("\r")

	time.sleep(0.1)
	sys.stdout.flush()

sys.stdout.write("\n")
print(NUM_WORDS);
sys.stdout.write("Done and Done")


def spritz(wpm, reading):
    """
    function to perform "spritz"
    """

    secondPerWord = 60.0 / wpm
    sleepInterval = secondPerWord 
    maxLength = find_max(reading)

    for word in reading:
        if word == "<pause>":
            time.sleep(sleepInterval * 10)
            continue

        wordSleepInterval = 0.01 * len(word)

        time.sleep(sleepInterval + wordSleepInterval)
        orpConfig = calculate_spaces(word, maxLength)
        print_word(word, orpConfig)


def main(wpm, article):
    """
    Main function
    """
    reading = parse_article(article)
    spritz(wpm, reading)

if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1]:
        try:
            wpm = int(sys.argv[1])
        except:
            print ("<wpm> need to be an integer")
            exit(1)
    else:
        wpm = 250

    article = ""
    
    for line in fileinput.input(sys.argv[2:]):
        article += line
    
    main(wpm, article)

# spritz(250,MY_STRING)

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