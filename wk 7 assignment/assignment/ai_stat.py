import csv, statistics as stat

scores = []

with open("students.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # row is a dictionary representing a student
        # e.g., {'name': 'Alice', 'age': '23', 'grade': 'A'}
        # extract the score for each student
        # put the scores in the scores list
        # remove the print statement below and replace it with your code
        scores.append(int(row["score"]))

print(scores)
        
# Perform statistical analysis on the scores list
# calculate min, max,mean, median, mode, standard deviation
# print the results
# use the tab character (\t) to separate the label from the value
# e.g., print("Min:\t", min_score)
# add enough tab characters to align the values
# for those results that have a decimal value, round to 2 decimal places
# e.g., round(mean_score, 2)
print("\nMin:\t\t\t", min(scores))

print("Max:\t\t\t", max(scores))

print('Mean:\t\t\t', round(stat.mean(scores), 2))

print("Median: \t\t", round(stat.median(scores), 2))

print('Mode:  \t\t\t', stat.mode(scores))

print('Standard Deviation:\t', round(stat.stdev(scores), 2))

print('Variace: \t\t', round(stat.variance(scores), 2))

print('Range: \t\t\t', max(scores)-min(scores))

print('Quartiles: \t\t', stat.quantiles(scores, n=4))

quant = stat.quantiles(scores, n=4)

iqr = quant[2] -quant[0]
print("IQR: \t\t\t", iqr)

data_2 = [81, 88, 81, 89, 85, 98, 71, 77, 91, 56, 46, 99, 93, 90, 73, 96, 77, 80, 82, 84, 80, 78, 91, 100, 96, 90, 95, 96, 95, 71]

print('Correlation (x,y): \t', round(stat.correlation(scores, data_2), 2))
print('Correlation (y,x): \t', round(stat.correlation(data_2, scores), 2))
