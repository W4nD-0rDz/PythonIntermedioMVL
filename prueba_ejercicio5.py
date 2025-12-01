import csv

with open("anses.csv", encoding="utf-8") as f:
    r = csv.reader(f)
    for row in r:
        print(row)