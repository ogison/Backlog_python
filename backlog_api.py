import requests
import json
import os
# import pprint
from datetime import datetime

start_date = '2024-04-22T00:00:00Z'
end_date = '2024-04-22T23:59:59Z'

file_path = 'setting.json'
api_key = ''
project_name = ''
directory = 'output'

''' setting_json（設定ファイル）を読み込み
'''
def read_setting():
    global start_date
    global end_date
    global api_key
    global project_name

    with open(file_path, 'r') as file:
        setting_data = json.load(file)

    start_date = setting_data['start_date']
    end_date = setting_data['end_date']
    api_key = setting_data['api_key']
    project_name = setting_data['project_name']

''' 日付の比較 
Args:
    d1 : 日付
    d2 : 日付

Returns: 
    d1 > d2 : True
    d1 < d2 : False
'''
def date_comparison(d1, d2):
    date1 = datetime.strptime(d1, '%Y-%m-%dT%H:%M:%SZ')
    date2 = datetime.strptime(d2, '%Y-%m-%dT%H:%M:%SZ')

    if date1 > date2:
        return True
    else:
        return False
    
''' フォルダの作成 
Args:
    dir : フォルダ名
'''
def make_directory(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

''' 期限切れのチケットをテキストファイルに出力 
Args:
    count : 確認するチケット数
'''
def check_expired_tichket(count):
    payload = {
        'apiKey' : api_key,
        'count'  : count
    }

    response = requests.get(f'https://{project_name}.backlog.jp//api/v2/issues', payload)
    json_list = response.json()

    output_txt = ''

    for json in json_list:
        due_date = json['dueDate']
                
        if due_date is not None:
            if date_comparison(start_date, due_date):
                ticket_name = json['summary']
                issue_key = json['issueKey']
                assignee = json['assignee']['name']
                output_txt += f'ユーザ名：{assignee} チケット名：{issue_key} {ticket_name}\n'
    
    make_directory(f'{directory}/expired')
    file_path = f'{directory}/expired/expired_ticket_list.txt'
    if not os.path.exists(file_path):
        with open(file_path, 'x') as f:
            f.write(output_txt)
    else:
        with open(file_path, 'w') as f:
            f.write(output_txt)

def main():
    help(read_setting)
    read_setting()
    make_directory(directory)
    check_expired_tichket(10)

if __name__ == '__main__':
    main()

    