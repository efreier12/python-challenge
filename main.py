import os
import csv

#create variables
total_votes = 0
candidates = []
candidates2 = [] 
candidates_votes = [0, 0, 0, 0]
percent_votes = [0, 0, 0, 0]
winner = []

#path to csv file
csv_data = os.path.join('.', 'Resources', 'election_data.csv')

#open csv file and read it using csv.reader(new variable)
with open(csv_data, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
#skip the header
    csv_header = next(csv_reader)

#loop through file - count votes, add     
    for vote in csv_reader:
        total_votes += 1
        candidates.append(str(vote[2]))
    for vote[2] in candidates:
        if vote[2] not in candidates2:
            candidates2.append(vote[2])
        if vote[2] == candidates2[0]:
            candidates_votes[0] += 1
        elif vote[2] == candidates2[1]:
            candidates_votes[1] += 1
        elif vote[2] == candidates2[2]:
            candidates_votes[2] += 1
        elif vote[2] == candidates2[3]:
            candidates_votes[3] += 1
            
#function to find % oftotal votes
    percent_votes[0] = round(100 * (candidates_votes[0] / total_votes), 4)
    percent_votes[1] = round(100 * (candidates_votes[1] / total_votes), 4)
    percent_votes[2] = round(100 * (candidates_votes[2] / total_votes), 4)
    percent_votes[3] = round(100 * (candidates_votes[3] / total_votes), 4)

#and the winner is...
    if candidates_votes[0] == max(candidates_votes[0], candidates_votes[1], candidates_votes[2], candidates_votes[3]):
        winner = candidates2[0]
    elif candidates_votes[1] == max(candidates_votes[0], candidates_votes[1], candidates_votes[2], candidates_votes[3]):
        winner = candidates2[1]    
    elif candidates_votes[2] == max(candidates_votes[0], candidates_votes[1], candidates_votes[2], candidates_votes[3]):
        winner = candidates2[2]
    elif candidates_votes[3] == max(candidates_votes[0], candidates_votes[1], candidates_votes[2], candidates_votes[3]):
        winner = candidates2[3]
        
#print functions
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    print(f"{candidates2[0]}: {percent_votes[0]}% ({candidates_votes[0]})")        
    print(f"{candidates2[1]}: {percent_votes[1]}% ({candidates_votes[1]})")
    print(f"{candidates2[2]}: {percent_votes[2]}% ({candidates_votes[2]})")
    print(f"{candidates2[3]}: {percent_votes[3]}% ({candidates_votes[3]})")
    print("-------------------------")
    print(f"Winner: {winner}")        
    print("-------------------------")
    
#print to text file
results_path = os.path.join(".", "Results", "Final_Results_Poll.txt")
with open(results_path, 'w', newline='') as text_file:
    print("Election Results", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print("-------------------------", file=text_file)
    print(f"{candidates2[0]}: {percent_votes[0]}% ({candidates_votes[0]})", file=text_file)        
    print(f"{candidates2[1]}: {percent_votes[1]}% ({candidates_votes[1]})", file=text_file)
    print(f"{candidates2[2]}: {percent_votes[2]}% ({candidates_votes[2]})", file=text_file)
    print(f"{candidates2[3]}: {percent_votes[3]}% ({candidates_votes[3]})", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Winner: {winner}", file=text_file)        
    print("-------------------------", file=text_file)

csvfile.close()   
    
