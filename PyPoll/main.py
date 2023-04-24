# PyPoll

# INSTRUCTIONS: Create a Python script that analyzes the votes and calculates each of
# the following values:
    # The total number of votes cast (A)
    # A complete list of candidates who received votes (B)
    # The percentage of votes each candidate won (C)
    # The total number of votes each candidate won (D)
    # The winner of the election based on popular vote (E)

# In addition, your final script should both print the analysis to the terminal and
# export a text file with the results.

# open the CSV file
import os
import csv


CSV_PATH = os.path.join("Resources", "election_data.csv")
CAND_IDX = 2
OUTPUT_PATH = os.path.join("analysis", "pypoll_output.txt")


os.chdir(os.path.dirname(os.path.realpath(__file__)))


cand_votes = {}
results = {}

total_votes = 0
most_votes = 0

stars = ("*" * 20) + "\n"
output = "Election Results \n" + stars + "\n"

with open(CSV_PATH) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header into a dictionary
    # If the name in the current row is already present as a key, increment their votes by 1
    # If not, add it as a key with 1 vote.
    for row in csvreader:
        curr_name = row[CAND_IDX]
        if curr_name in cand_votes.keys():
            cand_votes[curr_name] += 1
        else:
            cand_votes[curr_name] = 1

       # if we cared about the counties we would use a nested dictionary
#      cand_votes[row[0]] = {'results': {'county': row[1], 'candidate': row[2] }}

    print(cand_votes)

    for v in cand_votes.values():
        total_votes = total_votes + v
    
    output = output + "Total Votes: " + str(total_votes) + "\n\n" + stars + "\n"
    

    # Calculate percentage of votes for each candidate and add their info to the output
    for c in cand_votes:
        curr_name = c
        curr_votes = cand_votes[curr_name]
        curr_pct = (curr_votes / total_votes)
        curr_pctstr = "{:.3%}".format(curr_pct)

        output = output + curr_name + ": " + curr_pctstr + "  (" + str(curr_votes) + ")\n"

        if curr_votes > most_votes:
            most_votes = curr_votes
            winner = curr_name
  
    # Find the winner, add to output
    output = output + "\n" + stars + "\n" + "Winner: " + winner + "\n\n" + stars

    with open(OUTPUT_PATH, 'w') as txtfile:
        txtfile.write(output)
        print(output)
    



    




