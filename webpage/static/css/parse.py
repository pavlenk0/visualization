import csv

with open("titanic(full).csv") as f:
    reader = csv.reader(f)
    next(reader)
    with open("titanic(parse).csv", 'w') as k:
        for row in reader:
            if not row[4].strip():
                continue
            else:
                writer = csv.writer(k)
                writer.writerow(row)

