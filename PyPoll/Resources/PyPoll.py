# Goal is to calculate the results of the election and create a .txt file in the same folder that will have the following ##values

## The total number of votes cast

## A complete list of candidates who received votes

## The percentage of votes each candidate won

## The total number of votes each candidate won

## The winner of the election based on popular vote

# Dataset is a csv file with 3 columns
# Coloumn 1 is the ballot id, Column 2 is the county and coloumn 3 is the candidate

#Import the functions needed
import os
import csv

#Define file paths
csv_file = "election_data.csv"
output = "Election_result.txt"

#Initialize Variables
candidates = {}
total_votes = 0
winner = ""

# Load budget_data.csv in a readable format
pypoll = os.path.join("..", "Resources", "election_data.csv")

with open(pypoll, encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    
    #Extract the candidates names from the row
    for row in csv_reader:
        candidate = row[2]

        #Count the total number of votes
        total_votes += 1

        #track the number of votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

#Determining the winner based on popular vote
winner = max(candidates, key=candidates.get)

#Calculate the percentage of of vote for each candidate
percentages = {}
for candidate, votes in candidates.items():
    percentage = (votes / total_votes)
    percentages[candidate] = (percentage * 100)

#Printing results to .txt file
with open(output, "w") as file:
    file.write("Election Results\n")
    file.write("\n")
    file.write("---------------------\n")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("\n")
    file.write("---------------------\n")
    file.write("\n")

    for candidate, votes in candidates.items():
        percentage = percentages[candidate]
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        file.write("\n")
        file.write("\n")
    file.write("---------------------\n")
    file.write("\n")
    file.write(f"Winner: {winner}\n")
    file.write("\n")
    file.write("---------------------\n")

with open(output,'r') as file:
    ouput_content = file.read()
    print(ouput_content)

print("The elections results are also saved in the same directory under election_results.txt\n")




