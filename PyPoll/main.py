import os
import csv

pypoll_csv_path = os.path.join(".", "PyPoll\Resources", "election_data.csv")

voters=[]
country=[]
candidate=[]
unique_candidate_list=[]

candidate_vote=0
vote_count=0
unique_candidate1Count=0
unique_candidate2Count=0
unique_candidate3Count=0
unique_candidate4Count=0

with open(pypoll_csv_path,newline="")as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csv_reader)
    for row in csv_reader:
        voters.append(row[0])
        country.append(row[1])
        candidate.append(row[2])

def unique(candidate):
    for x in candidate:
        if x not in unique_candidate_list:
            unique_candidate_list.append(x)
unique(candidate)

for i in range(len(candidate)):
    if unique_candidate_list[0]==candidate[i]:
        unique_candidate1Count=unique_candidate1Count+1
    if unique_candidate_list[1]==candidate[i]:
        unique_candidate2Count=unique_candidate2Count+1
    if unique_candidate_list[2]==candidate[i]:
        unique_candidate3Count=unique_candidate3Count+1
    if unique_candidate_list[3]==candidate[i]:
        unique_candidate4Count=unique_candidate4Count+1

vote_percentage1 = '{0:.3f}'.format((unique_candidate1Count/len(voters))*100)
vote_percentage2 = '{0:.3f}'.format((unique_candidate2Count/len(voters))*100)
vote_percentage3 = '{0:.3f}'.format((unique_candidate3Count/len(voters))*100)
vote_percentage4 = '{0:.3f}'.format((unique_candidate4Count/len(voters))*100)

print("Election Results")
print("-------------------------------")
print("Total Votes: " + str(len(voters)))
print("-------------------------------")
print(unique_candidate_list[0]+ ": " + str(vote_percentage1) + "% " + "("+str(unique_candidate1Count)+")")
print(unique_candidate_list[1]+ ": " + str(vote_percentage2) + "% " + "("+str(unique_candidate2Count)+")")
print(unique_candidate_list[2]+ ": " + str(vote_percentage3) + "% " + "("+str(unique_candidate3Count)+")")
print(unique_candidate_list[3]+ ": " + str(vote_percentage4) + "% " + "("+str(unique_candidate4Count)+")")

if unique_candidate1Count>unique_candidate2Count and unique_candidate1Count>unique_candidate3Count and unique_candidate1Count>unique_candidate4Count:
    winner=unique_candidate_list[0]
elif unique_candidate2Count>unique_candidate1Count and unique_candidate2Count>unique_candidate3Count and unique_candidate2Count>unique_candidate4Count:
    winner=unique_candidate_list[1]
elif unique_candidate3Count>unique_candidate1Count and unique_candidate3Count>unique_candidate2Count and unique_candidate3Count>unique_candidate4Count:
    winner=unique_candidate_list[2]
else:
    winner=unique_candidate_list[3]
print("------------------")
print("Winner: ", winner)
print("------------------")

pypoll_output_path = os.path.join("..", "PyPoll", "pypoll_out.txt")
with open(pypoll_output_path,'w', newline='') as file:
    file.write("Election Results\n")
    file.write("------------------\n")
    file.write("Total Votes:")
    file.write(str(len(voters)))
    file.write("\n")
    file.write("------------------\n")
    file.write(unique_candidate_list[0]+ ": " + str(vote_percentage1) + "% " + "("+str(unique_candidate1Count)+")\n")
    file.write(unique_candidate_list[1]+ ": " + str(vote_percentage2) + "% " + "("+str(unique_candidate2Count)+")\n")
    file.write(unique_candidate_list[2]+ ": " + str(vote_percentage3) + "% " + "("+str(unique_candidate3Count)+")\n")
    file.write(unique_candidate_list[3]+ ": " + str(vote_percentage4) + "% " + "("+str(unique_candidate4Count)+")\n")
    file.write("------------------\n")
    file.write("Winner: "+ winner)
    file.write("\n")
    file.write("------------------")
    
