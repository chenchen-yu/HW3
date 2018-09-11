import os
import csv
csvpath="/Users/chenchen/Downloads/HW/HW3/python-challenge/PyPoll/election_data.csv"

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #The The total number of votes cast
    total_votes=0
    candidate=[]
    candidate_list=[]
    percen_list=[]
    n=0

    for row in csvreader:
        total_votes += 1 #method 2: row_count = sum(1 for row in csvreader)
        candidate.append(row[2])

        if row[2] not in candidate_list:
            candidate_list.append(row[2])

    candidate_votes = {i:candidate.count(i) for i in candidate_list}

    per_Khan="{0:.3f}%".format(100*int(candidate_votes[candidate_list[0]])/total_votes)
    per_Correy="{0:.3f}%".format(100*int(candidate_votes[candidate_list[1]])/total_votes)
    per_Li="{0:.3f}%".format(100*int(candidate_votes[candidate_list[2]])/total_votes)
    per_OTooley="{0:.3f}%".format(100*int(candidate_votes[candidate_list[3]])/total_votes)

#print the analysis to the terminal
print ("Election Results")
print ("---------------------------------------------")
print (f'Total Votes: {total_votes}')
print ("---------------------------------------------")
print (f'{candidate_list[0]}: {per_Khan} ({candidate_votes[candidate_list[0]]})')
print (f'{candidate_list[1]}: {per_Correy} ({candidate_votes[candidate_list[1]]})')
print (f'{candidate_list[2]}: {per_Li} ({candidate_votes[candidate_list[2]]})')
print (f'{candidate_list[3]}: {per_OTooley} ({candidate_votes[candidate_list[3]]})')
print ("---------------------------------------------")
print ("Winner: Khan" )
print ("---------------------------------------------")

#export a text file with the results
txtpath="/Users/chenchen/Downloads/HW/HW3/python-challenge/PyPoll/output.txt"
txtfile = open(txtpath,'w')
txtfile.write("Election Results\n")
txtfile.write("---------------------------------------------\n")
txtfile.write("Total Votes: " + str(total_votes) +'\n')
txtfile.write("---------------------------------------------\n")
txtfile.write(candidate_list[0] + " : " + per_Khan + "  (" + str(candidate_votes[candidate_list[0]]) + ")" +'\n')
txtfile.write(candidate_list[1] + " : " + per_Correy + "  (" + str(candidate_votes[candidate_list[1]]) + ")" +'\n')
txtfile.write(candidate_list[2] + " : " + per_Li + "  (" + str(candidate_votes[candidate_list[2]]) + ")" +'\n')
txtfile.write(candidate_list[3] + " : " + per_OTooley + "  (" + str(candidate_votes[candidate_list[3]]) + ")" +'\n')
txtfile.write("---------------------------------------------\n")
txtfile.write("Winner: Khan\n")
txtfile.write("---------------------------------------------\n")
txtfile.close() 
