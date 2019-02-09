import os
import re
letters = []
characters = []
# Read file in path
paragraph = os.path.join("raw_data/paragraph_1.txt")
with open(paragraph, 'r') as textfile:
    data = textfile.read()
    # Word Count
    w = len(data.split(" "))
    s = len(re.split("(?<=[.!?]) +", data))
    ws = (w) / (s)
    letters = len(re.findall('[A-Za-z]', data))
    averageletters = letters / (w)
 
# Word Count
# Sentence Count
# Letter Count
# Sentence Length
print("Paragraph Analysis")
print ("-----------------")
print ("Approximate Word Count: " + str(w))
print ("Approximate Sentence Count: " + str(s))
print ("Average Letter Count: " + str(averageletters))
print ("Average Sentence Length: " + str(ws))
