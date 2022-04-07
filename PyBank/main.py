#import depedencies 

import os
import csv

profit_list = []
months_list= []
profit_change_list =[]


csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#open csv file here
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Header row
    csv_header = next(csvreader)

    

    for rows in csvreader:
        months_list.append(rows[0]) 
        profit_list.append(int(rows[1])) 

#calculating the list of monthly profit change
for i in range(1,len(profit_list)):
    profit_change_list.append(profit_list[i] - profit_list[i-1])

#calculation
with open("pybank.txt", "w") as txt_file:
    txt_file.write( "financial Analysis"+ '\n')
    txt_file.write( "total Months"+ '\n')
    txt_file.write( "total"+ '\n')
    txt_file.write( "Average Change"+ '\n')
    txt_file.write( "Greatest Increase in Profit"+ '\n')
    txt_file.write( "Decrease  in Profit"+ '\n')
    print (f"financial Analysis")
    print("----------------------")
    print(f"total Months: {len(months_list)}")
    print(f"Total: ${sum(profit_list):,}")
    print (f"Average Change: ${round(sum(profit_change_list)/len(profit_change_list),2):,}")

#get the max profit 
    index = profit_change_list.index(  max(profit_change_list))
    print(f"Greatest Increase in Profit: {months_list[index + 1]} :${profit_change_list[index]:,})")

    index = profit_change_list.index(  min(profit_change_list))
    print(f"Decrease  in Profit: {months_list[index + 1]} :${profit_change_list[index]:,})")
