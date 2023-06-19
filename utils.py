import json
from datetime import datetime

def get_data():
    with open('operations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_filtered_data(data, filter_empty_from=False):

    #print(f"�� ����������: {len(data)}")
    #print(f"��� ����� \"state\": {[x for x in data if 'state' not in x]}")

    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]

    #print(f"����� ���������� ���������: {len(data)}")
    # assert False

    return data

def get_last_values(data, count_last_values):

    #def key_sort(x):
        #return x["data"]

    #dates = '\n'.join([x['data'] for x in data][:10])
    #print(f"���� �� ����������: \n{ dates }\n")

    data = sorted(data, key=lambda x: x["date"], reverse=True)

    #data = sorted(data, key=key_sort, reverse=True)

    # dates = '\n'.join([x['data'] for x in data][:10])
    # print(f"���� ����� ����������: \n{ dates }\n")

    data = data[:count_last_values]
    return data

def encode_bill_info(bill_info):
    bill_info = bill_info.split()
    bill, info = bill_info[-1], " ".join(bill_info[:-1])
    if len(bill) == 16:
        # print(f"����� ����� ��: {bill}")
        bill = f"{bill[:4]}{ bill[4:6] }** **** {bill[-4:]}"
        #print(f"����� ����� �����: {bill}")
        #assert (False)

    else:
        # print(f"���� ����� ��: { bill }")
        bill = f"** { bill[-4:]}"
        # print(f"���� ����� �����: { bill }")
        # assert (False)

    to = f"{info} {bill} "
    return to

def get_formatted_data(data):
    formatted_data = []
    for row in data:

        #print(f"����: {row['data']}")
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        # print(f"����: {date}")

        description = row["description"]
        # print(f"��������: {description}")

        if "from" in row:
            #print(f"����������� ��: {row['from']}")
            sender = encode_bill_info(row['from'])
            sender = f"{sender}-> "
            # print(f"����������� �����: {sender}")
            # assert (False)
        else:
            sender = ""

        #print(f"���������� ��: {row['to']}")
        to = encode_bill_info(row['to'])
        # print(f"���������� �����: {to}")

        operations_amount = f"{row['operationAmount']['amount']}{row['operationAmount']['currency']['name']}"
        formatted_data.append(f"""\
        {date} {description}
        {sender}{to}
        {operations_amount}""")

    return formatted_data

