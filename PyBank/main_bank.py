#import the os module
import os

#import the csv module
import csv

#import datetime module
from datetime import datetime

#create object "csvpath" that hold the value that is the contents of the "budget_data" file
csvpath = os.path.join("Resources_bank", "budget_data.csv")

#setting up variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
changes_in_profit_loss = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999]
change = 0
#./Resources_bank/budget_data.csv
with open (csvpath) as csvfile:
    #use the .reader funtion and the csv module to create object "csvreader" based on the parameters of "csvfile" and assigning a delimeter
    csvreader = csv.reader(csvfile, delimiter =',')

    #use 'next' to not use teh header in the equations
    next(csvreader)

    #calculate the total months (rows) and net total of profit/loss
    for rows in csvreader:
        date = datetime.strptime(rows[0], "%b-%y")
        total_months += 1
        profit_loss = int(rows[1])
        total_profit_loss += profit_loss

        #because we only want this loop to start calculating after row is greater than 1:
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes_in_profit_loss.append(change)

            #calculate the greatest increase
            if change > greatest_increase[1]:
                greatest_increase[0] = rows[0]
                greatest_increase[1] = change

            #calculate the greatest decrease
            if change < greatest_decrease[1]:
                greatest_decrease[0] = rows[0]
                greatest_decrease[1] = change



        previous_profit_loss = profit_loss

    #find the average profit loss over the entire time period
    avg_profit_loss = sum(changes_in_profit_loss)/len(changes_in_profit_loss)


    output = "Financial Analysis\n"
    output +="---------------------------------\n"
    output += f"Total Months: {total_months}\n"
    output += f"Total Profit Loss: ${total_profit_loss}\n"
    output += f"Greatest Increase in Profits: ${greatest_increase}\n"
    output += f"Greatest Decrease in Profits: ${greatest_decrease}\n"

print(output)

with open("./Analysis_bank/Analysis.txt", "w") as txtfile:
    txtfile.write(output)
    #print(total_profit_loss)
    #print(total_months)
    #print(avg_profit_loss)
#print("Hello " + str(3))
#print(f"Hello {3}")











