# Import Dependencies
import os
import csv
import pathlib

#Dictionary for States 
us_state_abbrev = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Colombia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming',
}

# Declare Lists from CSV
Emp = []
Name = []
DOB = []
SSN = []  
State = []

# Declare Lists to CSV
FirstName = []
LastName = []

D = []
M = []
Y = []
EmpCorrDOB = []

SSNOut = "***-**-"
SSNOutNum = []
SSNCorrect = []

StateAbbr = []
StateFull = []
StateOut = []


# Split Dictionary into two lists to be able to lookup keys
for key, value in us_state_abbrev.items():
    temp = [key,value]
    StateAbbr.append(temp[0])
    StateFull.append(temp[1])


# path
data_csv = os.path.join("employee_data.csv")

# Open and read csv
with open(data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
# Read the header row first     
    csv_header = next(csvfile)

# Read through each row of data after the header and put into lists
    for row in csvreader:
        Emp.append(row[0])
        Name.append(row[1])
        DOB.append(row[2])
        SSN.append(row[3])
        State.append(row[4])
    
# Seperate Names        
    for i in range(0, len(Name)):
        fullname = Name[i]
        FirstName.append(fullname.split()[0])
        LastName.append(fullname.split()[1])
        
# Seperate DOB 
        Birth = DOB[i]
        Y = (Birth.split("-")[0]) 
        M = (Birth.split("-")[1])
        D = (Birth.split("-")[2])
        EmpCorrDOB.append(str(M + "/" + D + "/" + Y))

# Seperate SSN
        Social = SSN[i]
        SSNOutNum.append(Social.split("-")[2])
        SSNCorrect.append(str("***-**-" + SSNOutNum[i]))

# Get State Values
        Employeestate = State[i]
        index = StateFull.index(Employeestate)
        StateOut.append(StateAbbr[index])

# Zip all the Lists together 
    Employee = zip(Emp, FirstName, LastName, EmpCorrDOB, SSNCorrect, StateOut)


#output
    # Specify the file to write to
    output_path = os.path.join("..", "output", "PyBoss.csv")
    #create path if it doesn't exist
    pathlib.Path("..", "output").mkdir(parents=True, exist_ok=True) 

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w+', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

    # Write the second row
    csvwriter.writerows(Employee)