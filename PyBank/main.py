import os
import csv

pybank_csv_path = os.path.join(".", "PyBank\Resources", "budget_data.csv")

month=[]
total=[]
avgchange=[]

with open(pybank_csv_path,newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header=next (csv_reader)
    for row in csv_reader:
        #count=count+1
        #total.append(row[1])
        #total = total + int(row[1])
        month.append(row[0])
        total.append(int(row[1]))
    for i in range(len(total)-1):
        avgchange.append(total[i+1]-total[i])
        #avg_change=mean(avgchange)


greatest_increase_value = max(avgchange)
greatest_decrease_value = min(avgchange)
greatest_increase = month[avgchange.index(max(avgchange)) + 1]
greatest_decrease = month[avgchange.index(min(avgchange)) + 1]
avg_change =round(sum(avgchange)/len(avgchange),2)
#maxvalueDecreaseMonth = profitChange.index(min(profitChange)) + 1


print("Financial Analysis")
print("------------------")
print("The total number of months included in the dataset: "+ str(len(month)))
print("The net total amount of Profit or Losses over the entire period: "+str(sum(total)))
print("The average of the changes in Profit or Losses over the entire period: " + str(avg_change))
print("The greatest increase in profits: " + str(greatest_increase) + " " + "(" "$" + (str(greatest_increase_value)) + ")")
print("The greatest decrease in profits: " + str(greatest_decrease) + " " + "(" "$" + (str(greatest_decrease_value)) + ")")
#print(f"Greatest Increase (in Profits): {monthList[maxvalueIncreaseMonth]} (${(str(maxvalueIncrease))})")
#print(f"Greatest Decrease (in Profits): {monthList[maxvalueDecreaseMonth]} (${(str(maxvalueDecrease))})")

pybank_output_path = os.path.join("..", "PyBank", "pybank_out.txt")

with open(pybank_output_path,'w', newline='') as file:
    file.write("Financial Analysis\n")
    file.write("------------------\n")
    file.write("The total number of months included in the dataset:")
    file.write(str(len(month)))
    file.write("\n")
    file.write("The net total amount of Profit or Losses over the entire period: "+str(sum(total)))
    file.write("\n")
    file.write("The average of the changes in Profit or Losses over the entire period: " + str(avg_change))
    file.write("\n")
    file.write("The greatest increase in profits: " + str(greatest_increase) + " " + "(" "$" + (str(greatest_increase_value)) + ")")
    file.write("\n")
    file.write("The greatest decrease in profits: " + str(greatest_decrease) + " " + "(" "$" + (str(greatest_decrease_value)) + ")")
