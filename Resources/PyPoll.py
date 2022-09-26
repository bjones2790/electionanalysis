# The data we need to retrieve
# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources" , "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis" , "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: Read and analyze the data here
    file_reader = csv.reader(election_data)
    #print the header row in the CSV file.
    headers = next(file_reader)
    print(headers)
#file_to_load = os.path.join("Desktop", "UNCC", "Module_3" , "Resources" , "election_results.csv") 

#1. The total number of votes cast

#2. A complete list of candidates who received votes

#3. The % of votes each candidate won

#4. The total number of votes each candidate won

#5. The winner of the election based on popular vote