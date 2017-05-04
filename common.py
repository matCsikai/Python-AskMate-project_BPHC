import csv
import base64
import time


def read_data(file_name):

    data_list = []

    with open(file_name) as f:
        for line in csv.reader(f, delimiter=","):
            line[4] = base64.b64decode(line[4]).decode('utf-8')
            line[5] = base64.b64decode(line[5]).decode('utf-8')
            # line[6] = base64.b64decode(line[6]).decode('utf-8')
            data_list.append(line)

    return data_list


def write_data(file_name, data_list):
    with open(file_name, "w") as f:
        for line in data_list:
            line[4] = base64.b64encode(bytes(line[4], "utf-8")).decode("utf-8")
            line[5] = base64.b64encode(bytes(line[5], "utf-8")).decode("utf-8")
            line = ','.join(line)
            f.write(line + "\n")


def generate_data_id(filename):
    all_data = read_data(filename)
    list_of_data_id = []

    if all_data == []:
        list_of_data_id.append(0)
    else:
        for data in all_data:
            list_of_data_id.append(int(data[0]))

    return max(list_of_data_id) + 1


def time_decode(all_data):
    decoded_data = []
    for line in all_data:
        time_number = int(line[1])
        localtime = time.localtime(time_number)
        line[1] = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
        decoded_data.append(line)
    return decoded_data
