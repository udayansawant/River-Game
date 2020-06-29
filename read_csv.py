import csv


def read_csv():
    filename = "Task_Training_Data .csv"

    fields = []
    rows = {}

    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        fields = next(csv_reader)

        for row in csv_reader:
            # print("[Name,Email]:", row[:2])
            rows[row[0]] = row[1]
    # print("The total number of rows: %d" % csv_reader.line_num)
    # print("Field names are:" + ','.join(field for field in fields))
    return rows


result = read_csv()


