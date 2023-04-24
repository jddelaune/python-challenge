#PyBank

# INSTRUCTIONS: Your task is to create a Python script that analyzes the records to
# calculate each of the following values:

# (A) The total number of months included in the dataset
# (B) The net total amount of "Profit/Losses" over the entire period
# (C)The changes in "Profit/Losses" over the entire period, and then the average of those changes
# (D) The greatest increase in profits (date and amount) over the entire period
# (E) The greatest decrease in profits (date and amount) over the entire period

# In addition, your final script should both print the analysis to the terminal
# and export a text file with the results.

# open the CSV file and declare some variables
import os
import csv

CSV_PATH = os.path.join("Resources", "budget_data.csv")
OUTPUT_PATH = os.path.join("analysis", "pybank_output.txt")

prev_month = None
avg_change = 0
greatest_inc = 0
greatest_dec = 0
sum_delta_pl = 0

pl_data = {}

with open(CSV_PATH) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header into a dictionary
    for row in csvreader:
        pl_data[row[0]] = int(row[1])
        
    # count the number of months in the dictionary (A)
    months = len(pl_data)
    
    # get all the Profit/Loss entries as a list. Sum the entire list and write to a variable. (B)
    total_pl = sum(pl_data.values())

    # loop through the dictionary
    for mm in pl_data.keys():
        cur_month = mm
        # compare each month's P/L to the P/L for the following month (skipping first month)
        if prev_month != None:
            delta_pl = pl_data[cur_month] - pl_data[prev_month]
            sum_delta_pl = sum_delta_pl + delta_pl # add the difference between P/L to an ongoing sum (to get avg)
            if delta_pl > greatest_inc: # check if it was the greatest increase in profits so far, if so, store it (D)
                greatest_inc = delta_pl
                greatest_inc_month = cur_month
            if delta_pl < greatest_dec: # check if it was the greatest decrease in profits so far, if so, store it (E)
                greatest_dec = delta_pl
                greatest_dec_month = cur_month
        prev_month = cur_month # set previous month to current month and go back to start of loop

    avg_change = sum_delta_pl / (months - 1) # divide that sum* by total number of entries to get the average Profit/Loss (C)

    pybank_output = f"""
            Financial Analysis
            --------------------------
            Total Months: {months}
            Total: ${total_pl}
            Average Change: ${round(avg_change, 2)}
            Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})
            Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})"""

    with open(OUTPUT_PATH, 'w') as txtfile:
        txtfile.write(pybank_output)
        print(pybank_output)




    
    
    



