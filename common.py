import csv
import base64


def read_data(file_name):

    data_list = []

    with open(file_name) as f:
        for line in csv.reader(f, delimiter=","):
            line[4] = base64.b64decode(line[4]).decode('utf-8')
            line[5] = base64.b64decode(line[5]).decode('utf-8')
            data_list.append(line)

    return data_list


def write_data(file_name, data_list):
    with open(file_name, "w") as f:
        for data in data_list:
            data = ';'.join(data)
            f.write(data + "\n")


def generate_data_id(filename):
    all_data = read_data(filename)
    list_of_data_id = []

    if all_data == []:
        list_of_data_id.append(0)
    else:
        for data in all_data:
            list_of_data_id.append(int(data[0]))

    return max(list_of_data_id) + 1



read_data("question.csv")
