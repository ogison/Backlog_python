# Backlog_python
BacklogAPIをPythonで動かします

# 準備
1. 必要なライブラリをインストール  
```
pip install -r requirements.txt
```
2. setting.jsonに必要な情報を記載
api_key：BacklogのAPIキー
project_name：BacklogのスペースID 

# 機能
## 期限切れのチケットを確認
1. setting.jsonにstart_dateに基準の日付を設定
2. backlog_api.pyを実行
```
python backlog_api.py
```
3. output/expired/expired_ticket_list.txtを確認(期限切れのチケット一覧が出力)

## 更新したチケットをまとめる
1. setting.jsonにstart_date, end_dateに基準の日付を設定
2. user.jsonにuser_id(Backlogで使用しているユーザーID), user_name(ユーザー名)を設定
3. backlog_api.pyを実行
```
python backlog_api.py
```
4. output/expired/ユーザ名.txtを確認(指定日の期間で更新したチケット一覧が出力)
