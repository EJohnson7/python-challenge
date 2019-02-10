# Import Libraries
import os
import re
# Lists for storage
letters = []


# Read file in path
paragraph = os.path.join("raw_data/paragraph_1.txt")
with open(paragraph, 'r') as textfile:
    data = textfile.read()
    # Word Count
    w = len(data.split(" "))
    # Sentence Count
    s = len(re.split("(?<=[.!?]) +", data))
    # Words Per Sentence
    ws = (w) / (s)
    # Letter Count
    letters = len(re.findall('[A-Za-z]', data))
    # Letters per Word rounded
    averageletters = round(letters / (w), 1)
 
# Print Analysis
print("Paragraph Analysis")
print ("-----------------")
print ("Approximate Word Count: " + str(w))
print ("Approximate Sentence Count: " + str(s))
print ("Average Letter Count: " + str(averageletters))
print ("Average Sentence Length: " + str(ws))
