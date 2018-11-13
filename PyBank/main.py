import os
import csv

bank_csv = os.path.join('C:/Python_Challenge_Homework_3/python-challenge/PyBank','budget_data.csv')
count = 0
netamount = 0
max_increase = 0
max_decrease = 0

with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip header as header is not part of the data
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    for row in csvreader:
    # count number of row    
        count += 1
    # sum of value in a column
        netamount += int(row[1])
    # average change    
        average = netamount / count
    # find max value in a column
        if (max_increase < int(row[1])):
            max_increase = int(row[1])
            max_increase_month = row[0]
    # find min value in a column
        if (max_decrease > int(row[1])):
            max_decrease = int(row[1])
            max_decrease_month = row[0]
print ("Total Months: " + str(count)) 
print("Total: $" + str(netamount))
# only keep 2 decimal in the result
print("Average Change: $" + str(format(average, '.2f')))
# ----------------------------------
print("Greatest Increase in Profits: " + str(max_increase_month) + " " + str(max_increase))
print("Greatest Decrease in Profits: " + str(max_decrease_month) + " " + str(max_decrease))

# export the results above to a text file
# if we export using csv, there will be a , between each letter so don't use it
# if we export without +'\n' all result will be in the same line
# with +'\n' there will be a line break

output_file = os.path.join("PyBank_result.txt")
with open(output_file, "w") as datafile:
    datafile.write("Total Months: " + str(count) +'\n')
    datafile.write("Total: $" + str(netamount) + '\n')
    datafile.write("Average Change: $" + str(format(average, '.2f')) + '\n')
    datafile.write("Greatest Increase in Profits: " + str(max_increase_month) + " " + str(max_increase) + '\n')
    datafile.write("Greatest Decrease in Profits: " + str(max_decrease_month) + " " + str(max_decrease) + '\n')