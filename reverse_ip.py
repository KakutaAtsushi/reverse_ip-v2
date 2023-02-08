import csv
from datetime import datetime
from time import sleep
import requests


def GetReverseDomain():
    domain_name = input("domain名を入力してください\n")
    url = "https://api.hackertarget.com/reverseiplookup/?q={}&page=1&apikey=".format(
        domain_name)
    res = requests.get(url)
    res = res.text.replace(" ", "")
    return res, domain_name


def OutputCsv():
    reverse_func = GetReverseDomain()
    domain_data = []
    if reverse_func is None:
        return "抽出できませんでした。"
    domain_array = reverse_func[0].split("\n")
    for data in domain_array:
        domain_data.append([data])

    print(domain_data)
    domain_name = reverse_func[1]
    f = open("ReverseIP-CSV/{0} {1}.csv".format(domain_name, datetime.today().strftime('%Y-%m-%d %H-%M')), 'w',newline="")
    writer = csv.writer(f)
    for d in domain_data:
        writer.writerow(d)
    f.close()
    sleep(5)
    return print("抽出に成功しました")


if __name__ == '__main__':
    OutputCsv()
