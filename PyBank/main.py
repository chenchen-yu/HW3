import os
import csv

csvpath="/Users/chenchen/Downloads/HW/HW3/python-challenge/PyBank/budget_data.csv"

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #The total number of months included in the dataset
    #The total net amount of "Profit/Losses" over the entire period
    row_count = 0
    total_net = 0
    last_month = 0

    month=[]
    increase=[]

    for row in csvreader:
        row_count += 1 #method 2: row_count = sum(1 for row in csvreader)
        total_net += int(row[1])
        increase.append(int(row[1]) - last_month)
        last_month = int(row[1])

        month.append(row[0])

    #format total net amount
    total_net = '${:}'.format(total_net)
    #The average change in "Profit/Losses" between months over the entire period
    ave_change = '${:}'.format(round(sum(increase[1:len(increase)])/(row_count-1),2))

    #The greatest increase in profits (date and amount) over the entire period
    max_increase='${:}'.format(max(increase))
    max_increase_month=month[increase.index(max(increase))]
    #The greatest decrease in losses (date and amount) over the entire period
    min_increase='${:}'.format(min(increase))
    min_increase_month=month[increase.index(min(increase))]

#print the analysis to the terminal
print ("Financial Analysis")
print ("---------------------------------------------")
print (f'Total Months: {row_count}')
print (f'Total: {total_net}' )
print (f'Average Change: {ave_change}')
print (f'Greatest Increase in Profits: {max_increase_month} ({max_increase})')
print (f'Greatest Decrease in Profits: {min_increase_month} ({min_increase})')

#export a text file with the results
txtpath="/Users/chenchen/Downloads/HW/HW3/python-challenge/PyBank/output.txt"
txtfile = open(txtpath,'w')

txtfile.write("Financial Analysis\n")
txtfile.write("---------------------------------------------\n")
txtfile.write("Total Months: " + str(row_count) +'\n')
txtfile.write("Total: " + str(total_net) +'\n')
txtfile.write("Average Change: " + str(ave_change) +'\n')
txtfile.write("Greatest Increase in Profits: " + max_increase_month + " " + "(" + str(max_increase) + ")" + '\n')
txtfile.write("Greatest Decrease in Profits: " + min_increase_month + " " + "(" + str(min_increase) + ")" + '\n')
txtfile.close() 
