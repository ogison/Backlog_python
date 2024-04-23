import requests
import json
import os
from datetime import datetime

start_date = '2024-04-22T00:00:00Z'
end_date = '2024-04-22T23:59:59Z'

file_path = 'setting.json'
api_key = ''
project_name = ''
directory = 'output'

"""
setting_json（設定ファイル）を読み込み
"""
def read_setting():
    global start_date
    global end_date
    global api_key

    with open(file_path, 'r') as file:
        setting_data = json.load(file)

    start_date = setting_data['start_date']
    end_date = setting_data['end_date']
    api_key = setting_data['api_key']
    project_name = setting_data['project_name']

"""
日付の比較 
d1 > d2 : True
d1 < d2 : False
"""
def date_comparison(d1, d2):
    date1 = datetime.strptime(d1, "%Y-%m-%dT%H;%M:%SZ")
    date2 = datetime.strptime(d2, "%Y-%m-%dT%H;%M:%SZ")

    if date1 > date2:
        return True
    else:
        return False

def check_expired_tichket(user_id, user_name):
    payload = {
        'apiKey' : api_key,
        'count'  : user_id
    }

    response = requests.get(f"https://{project_name}.backlog.jp//api/v2/issues", payload)
    json_list = response.json()

    output_txt = ''

    for json in json_list:
        ticket_name = json['summary']
        issue_key = json['issueKey']
        due_date = json['dueDate']

        if date_comparison(start_date, due_date):
            output_txt += user_name + ':' + issue_key + " " + ticket_name + " " + str(due_date) + '\n'
    
    file_path = f'{directory}/expired/{user_name}.txt'
    if not os.path.exists(file_path):
        with open(file_path, "x") as f:
            f.write(output_txt)
    else:
        with open(file_path, "w") as f:
            f.write(output_txt)

def main():
    read_setting()
    print(start_date)

if __name__ == '__main__':
    main()

    