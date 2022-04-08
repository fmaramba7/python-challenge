from doctest import OutputChecker
import os
import csv

total_votes = 0
candidates_list = {}
winners_name = ""
winners_count = 0


csvpath = os.path.join( '..','Resources', 'election_data.csv')

#open csv file here
with open(csvpath,) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Header row
    csv_header = next(csvreader)

    for row in csvreader:
        names = row [2]
        if names in candidates_list:
            candidates_list[names] = candidates_list[names] + 1
        else: 
            candidates_list [names] = 1


        total_votes = total_votes +1
with open("pypoll.txt", "w") as txt_file:

    print("election results")
    txt_file.write("election results" + '\n')
    txt_file.write("-------------------------"+ '\n')
    txt_file.write("Total votes: " + str(total_votes) + '\n')
    txt_file.write("-------------------------"+ '\n')
    txt_file.write("Winner" + winners_name + '\n')

    print("-------------------------")
    print ("Total votes: " + str(total_votes))
    print("-------------------------")
#print (candidates_list)
    for key, value in candidates_list.items():
        percent = value *100/total_votes
        output = key + ": " + str(round(percent, 3)) + "% (" + str(value) + ")"
        print(output)
        if value > winners_count :
            winners_name = key
            winners_count =value
    print("-------------------------")
    print("Winner" + winners_name) 
    print("-------------------------")    





