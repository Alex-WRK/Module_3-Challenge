# Goal is to calculate the following ##values and print the results to a .txt file in the same folder

## The total number of months included in the dataset

## The net total amount of "Profit/Losses" over the entire period

## The changes in "Profit/Losses" over the entire period, and then the average of those changes

## The greatest increase in profits (date and amount) over the entire period

## The greatest decrease in profits (date and amount) over the entire period

# Dataset is a csv file with 2 columns
# Coloumn 1 is the date, Column 2 is the PnL

### Data for this dataset was generated by edX Boot Camps LLC, and is intended for educational purposes only.


#import functions needed
import os
import csv

#Define file paths
csv_file = 'budget_data.csv'
ouput = 'analysis_file.txt'

#Initialize Variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = [0]
greatest_increase = [' ', 0]
greatest_decrease = [' ', 0]


# Load budget_data.csv in a readable format
pybank = os.path.join("..", "Resources", "budget_data.csv")

with open(pybank, encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)


    for row in csv_reader:
        # Extract the date and PnL from each row
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total months and net total
        total_months += 1
        net_total += profit_loss

        #Comparing PnLs to eachother to find the greatest increase and greatest decrease
        if previous_profit_loss != 0:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]
        previous_profit_loss = profit_loss

#Calculate the avg change
average_change = sum(changes) / (total_months - 1)

#print results to text file in the same folder as the code
with open (ouput, 'w') as file:
    file.write("Finanancial Analysis\n")
    file.write("-----------------------\n")
    file.write(f"Total months: {total_months}\n")
    file.write("\n")
    file.write(f"Total: ${net_total}\n")
    file.write("\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write("\n")
    file.write(f"Greatest Increase in Profit: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write("\n")
    file.write(f"Greatest Decrease in Profit: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

#Print output into terminal and confirm that the .txt file was created

with open(ouput,'r') as file:
    ouput_content = file.read()
    print(ouput_content)

print("The analysis results are also saved in the same directory under the name analysis_file.txt\n")









