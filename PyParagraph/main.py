import os
import re

words = []
wordcount = 0
# Read file in path
paragraph = os.path.join("paragraph.txt")
with open(paragraph, 'r') as textfile:
    data = textfile.read(delimiter= " ")
    
    for x in data:
        s = data.split(" ")
        words.append(s)
        #print(s)
    u = len(words)
    #print(data)

    for x in words:
        wordcount = wordcount + 1
print((data))
    
# Store Words into List
# Store Letters and only letters
# Store Sentences delimited by periods or other sentence endings into list
# 
#  
# Word Count
# Sentence Count
# Letter Count
# Sentence Length
