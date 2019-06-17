import os
import csv

#define variables
months = 0
date_list = []
profit_loss = []
total_profit_loss = float(0)
change_value = []
prior_value = float(0)

#path to csv file
csv_data = os.path.join('.', 'Resources', 'budget_data.csv')

#open csv file and read it using csv.reader(new variable)
with open(csv_data, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
#skip the header
    csv_header = next(csv_reader)

#creating a loop through the data    
    for value in csv_reader:
        months += 1
        date_list.append(str(value[0]))
        profit_loss.append(float(value[1]))
        
#list of profit/loss changes month to month     
        current_value = value[1]
        current_change_value = float(current_value) - float(prior_value)
        change_value.append (current_change_value)
        prior_value = current_value
        
#function to find average change in profit/loss month to month
def average(change_value):
    x = len(change_value)
    total = sum(change_value) - change_value[0]
    avg = total / (x - 1)
    return avg

average_change = round(average(change_value), 2)
         
        
#find total profit/loss
total_profit_loss = round(sum(profit_loss))

#dates with hig/low profit/loss

high = round(max(profit_loss))
low = round(min(profit_loss))
high_index = profit_loss.index(high)
low_index = profit_loss.index(low)

#print functions
print("Financial Analysis")
print("------------------")
print(f"Total Months: {months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {date_list[high_index]} ({high})")
print(f"Greatest Decrease in Profits: {date_list[low_index]} ({low})")

#path to text file
results_path = os.path.join(".", "Results", "Final_Results.txt")
with open(results_path, 'w', newline='') as text_file:
    print("Financial Analysis", file=text_file)
    print("------------------", file=text_file)
    print(f"Total Months: {months}", file=text_file)    
    print(f"Total: ${total_profit_loss}", file=text_file)    
    print(f"Average Change: ${average_change}", file=text_file)    
    print(f"Greatest Increase in Profits: {date_list[high_index]} ({high})", file=text_file)    
    print(f"Greatest Decrease in Profits: {date_list[low_index]} ({low})", file=text_file)
    
csvfile.close()    
    
    

















