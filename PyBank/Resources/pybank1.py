############################################################Ankur Srivastava###############################################

import os
import csv

csv_dict = {}
earning = 0


BudgetData = os.path.join('..', 'Resources', 'budget_data.csv')

with open(BudgetData, newline='') as newbudget:

    Budget_reader = csv.reader(newbudget, delimiter=',')
    Budget_header = next(Budget_reader)
    
    for row in Budget_reader:
        
        if row[0] not in csv_dict.keys():
            
            csv_dict[row[0]] = float(row[1])

        else:
            csv_dict[row[0]] = csv_dict[row[0]] + float(row[1])

        total_months = len(csv_dict.keys())
        
        print("The total number of months included in the dataset are", total_months)


average_sum = 0
highest_gain = ["", 0]
highest_loss = ["", 0]


for date in csv_dict.keys():
    if csv_dict[date] > highest_gain[1] or highest_gain[0] is "":
        highest_gain = [date, csv_dict[date]]
        
            
        
    
    if csv_dict[date] < highest_loss[1] or highest_loss[0] is "":
        highest_loss = [date, csv_dict[date]]
    

    earning += csv_dict[date]

    earning_total = round(earning)

if total_months > 0:
    average_sum = earning / total_months

average_earning = round(average_sum)

max_gain = format(highest_gain)
max_loss = format(highest_loss)

print("total earnings in a span of" , total_months, "months is", earning_total)

print("Average earnings are", average_earning)

print("maximum gain over the period is", max_gain)

print("maximum loss over the period is", max_loss)

