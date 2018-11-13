import os
import csv

election_csv = os.path.join("C:/Python_Challenge_Homework_3/python-challenge/PyPoll","election_data.csv")
count = 0
candidate_list = []
Khan_count = 0
Correy_count = 0
Li_count = 0
Tooley_count = 0

with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip header as header is not part of the data
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    for row in csvreader:
    # count number of row    
        count += 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        if row[2] == "Khan":
            Khan_count += 1
        if row[2] == "Correy":
            Correy_count += 1
        if row[2] == "Li":
            Li_count += 1
        if row [2] == "O'Tooley":
            Tooley_count +=1

Khan_percent = (Khan_count / count)
Correy_percent = (Correy_count / count)
Li_percent = (Li_count / count)
Tooley_percent = (Tooley_count / count)


print("Election Results")

print("-------------------------")

print("Total Votes: " + str(count))

print("-------------------------")

print("Khan: " + str("{:.3%}".format(Khan_percent)) + " (" + str(Khan_count) + ")")
print("Correy: " + str("{:.3%}".format(Correy_percent)) + " (" + str(Correy_count) + ")")
print("Li: " + str("{:.3%}".format(Li_percent)) + " (" + str(Li_count) + ")")
print("Tooley: " + str("{:.3%}".format(Tooley_percent)) + " (" + str(Tooley_count) + ")")

print("-------------------------")

if (Khan_percent > Correy_percent and Khan_percent > Li_percent and Khan_percent > Tooley_percent):
    result = ("Winner: Khan")
    #print(result)
elif (Correy_percent > Khan_percent and Correy_percent > Li_percent and Correy_percent > Tooley_percent):
    result = ("Winner: Correy")
    #print(result)
elif (Li_percent > Khan_percent and Li_percent > Correy_percent and Li_percent > Tooley_percent):
    result = ("Winner: Li")
    #print(result)
else:
    result = ("Winner: O'Tooley")
print(result)

print("-------------------------")
#print(candidate_list)
for candidate in range(len(candidate_list)):
    candidate_name = str(candidate_list[candidate])
    print(candidate_name)


# export the results above to a text file
# if we export using csv, there will be a , between each letter so don't use it
# if we export without +'\n' all result will be in the same line
# with +'\n' there will be a line break

output_file = os.path.join("PyPoll_result.txt")
with open(output_file, "w") as datafile:
    datafile.write("Election Results" +'\n')

    datafile.write("-------------------------" + '\n')

    datafile.write("Total Votes: " + str(count) + '\n')

    datafile.write("-------------------------" + '\n')

    datafile.write("Khan: " + str("{:.3%}".format(Khan_percent)) + " (" + str(Khan_count) + ")" + '\n')
    datafile.write("Correy: " + str("{:.3%}".format(Correy_percent)) + " (" + str(Correy_count) + ")" + '\n')
    datafile.write("Li: " + str("{:.3%}".format(Li_percent)) + " (" + str(Li_count) + ")" + '\n')
    datafile.write("Tooley: " + str("{:.3%}".format(Tooley_percent)) + " (" + str(Tooley_count) + ")" + '\n')

    datafile.write("-------------------------" + '\n')

    datafile.write(result + '\n')