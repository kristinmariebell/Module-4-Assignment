#import the os module
import os
#import the csv module
import csv


#create object "csvpath" that hold the value that is the contents of the "election_data" file
csvpath = os.path.join("Resources_poll", "election_data.csv")

#setting up variables
total_votes = 0
candidates_name = {}
candidates_options = {}
#name of candidate is the key and the value as the number of votes
candidate_votes = {}
percentage_votes = float
votes_per_candidate = 0
winner = ""

with open(csvpath) as csvfile:

    #use the .reader function to read the "election_data" file
    csvreader = csv.reader(csvfile, delimiter=',')

    #read the header of the file
    csv_header = next(csvfile)
    #print(csv_header)

    #starting the loop - for each row in csvreader, do this...
    for row in csvreader:

        #calculate total votes
        total_votes = total_votes +1

        #this is the column where the candidate names are
        candidates_name = row[2]

        #creating a list of candidates by saying if a name is not in the list, add it to the list
        if candidates_name not in candidates_options:
            candidates_options.append(candidates_name)
print(candidates_name)
            #tally the candidate's votes
            #candidate_votes(candidates_name) = 0
            #candidate_votes(candidates_name) = candidate_votes(candidates_name) +1



            #print(candidates_names)
    #for i, name in enumerate(csvreader):
        #candidates_names = (row[2])
    #print(candidates_names)

        #for candidate in csvreader:
        #yield candidates_names, person
        #candidates_names += 1



    #use 'next' inside the loop to not count the header in the file
    #next(csvreader, None)

    #for rows in csvreader:
       # total_votes += 1
        #if rows == [2]:
           # print(candidates_names)
        #candidates_names = 2
        #print(candidates_names)
        #print(total_votes)
        #print(rows)



