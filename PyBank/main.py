# import Libraries
import os
import csv
import pathlib

#Declare Lists
m = []
p = []
change = []
greatest = 0
least = 0

# path
bank_csv = os.path.join("..", "Resources", "budget_data.csv")

# Open and read csv
with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
# Read the header row first     
    csv_header = next(csvfile)

# Read through each row of data after the header
    for row in csvreader:
        # Append months and profits/losses list
        m.append(row[0])
        p.append(float(row[1]))

#Find average change
    for i in range(1, len(p)):
        change.append((float(p[i]) - float(p[i-1])))
    ave_change = sum(change) / len(change)
    average_change = round(ave_change, 2)

#Find Total months
    months = len(m)

# Find Total 
    total = sum(p)
    t = round(total)

#Find greatest change
    for i in change:
        if i > greatest:
            greatest = round(i)
            greatest_month = (m[change.index(i)+1])
        
#Find Least
    for i in change:
        if i < least:
            least = round(i)
            least_month = (m[change.index(i)+1])

#Print Summary
    print("Financial Analysis")
    print("------------------------------------------")
    print("Total Months: " + str(months))
    print("Total: $" + str(t))
    #print(change)
    print("Average Change: $" + str(average_change))
    print("Greatest Increase in Profits: " + str(greatest_month) + " " + "($" + str(greatest) + ")")
    print("Greatest Decrease in Profits: " + str(least_month) + " " + "($" + str(least) + ")")

    #output
    # Specify the file to write to
    output_path = os.path.join("..", "output", "bank_output.txt")
    #create path if it doesn't exist
    pathlib.Path("..", "output").mkdir(parents=True, exist_ok=True) 

    # Open the file using "write" mode. Specify the variable to hold the contents
    #Create text if not there
    with open(output_path, 'w+',) as text_file:
        print("Financial Analysis", file=text_file)
        print("------------------------------------------", file=text_file)
        print("Total Months: " + str(months), file=text_file)
        print("Total: $" + str(t), file=text_file)
        print("Average Change: $" + str(average_change), file=text_file)
        print("Greatest Increase in Profits: " + str(greatest_month) + " " + "($" + str(greatest) + ")", file=text_file)
        print("Greatest Decrease in Profits: " + str(least_month) + " " + "($" + str(least) + ")", file=text_file)