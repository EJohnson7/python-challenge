#import libraries
import os
import csv
import pathlib

#Declare Lists
Votes = []
count = []
cand = []
Percentage = []
greatest = 0
#myDict = {}
# path
vote_csv = os.path.join("..", "Resources", "election_data.csv")
# Open and read csv
with open(vote_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
# Read the header row first     
    csv_header = next(csvfile)

#Print header
    #print(f"Header: {csv_header}")
# Read through each row of data after the header
    for row in csvreader:
        Votes.append(row[2])

#Count number of votes   
    total = len(Votes)

#Find who won by counting each string in Votes 
    for i in Votes:
        if i not in cand:
            cand.append(i)
    for x in cand:
        count.append(Votes.count(x))
    for i in count:
        if i > greatest:
            greatest = int(i)
            winner = cand[count.index(i)]
        percentagecount = round(float((i/total)*100), 2)
        Percentage.append(percentagecount)

#Print answers
    print("")
    print("Election Results")
    print("----------------------")
    print("Total Votes: " + str(total))
    print("----------------------")
    for x in range(0, len(cand)):
        print(str(cand[x]) + ": " + str((Percentage[x])) + "00% " + "(" + str(count[(x)]) + ")")
        
    
    print("----------------------")
    print("Winner: " + str(winner))
    print("----------------------")

#output
    # Specify the file to write to
    output_path = os.path.join("..", "output", "election_output.txt")
    #create path if it doesn't exist
    pathlib.Path("..", "output").mkdir(parents=True, exist_ok=True) 

    # Open the file using "write" mode. Specify the variable to hold the contents
    #Create text if not there
    with open(output_path, 'w+',) as text_file:
        #Print answers
        print("", file=text_file)
        print("Election Results", file=text_file)
        print("----------------------", file=text_file)
        print("Total Votes: " + str(total), file=text_file)
        print("----------------------", file=text_file)
        for x in range(0, len(cand)):
            print(str(cand[x]) + ": " + str((Percentage[x])) + "00% " + "(" + str(count[(x)]) + ")", file=text_file)
        
    
        print("----------------------", file=text_file)
        print("Winner: " + str(winner), file=text_file)
        print("----------------------", file=text_file)

  