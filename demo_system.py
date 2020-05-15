
# 1. 先建立學籍資料，包括學號、學費、繳費狀態
# key: 學號、該學期是否可註冊
# value: 學費、繳費狀態
db_dict = {}
for k in enrolled_list:
    db_dict[k] = [1000000, False]    # 後面 value 部分，有很多種實作選擇，i.e. 再用一個 dict object

#print(db_dict)

# 這學期是？
cur_semester = "1082"

# 系統開始運作，印條漂漂線
print('-'*120)

# 2. 提示使用者輸入學號
query_id = input('請輸入欲查詢的學號：\n')
status_str = ['尚未繳費', '已繳費']

# 3. 檢查學號是否具有學籍？
if (query_id, cur_semester) in db_dict:
# 3-2. 確認有學籍，顯示學費、繳費狀態
    print('學號「', query_id, '」', cur_semester+'學期應繳學費：', db_dict[(query_id, cur_semester)][0], '，繳費狀態：' , status_str[db_dict[(query_id, cur_semester)][1]] )

# 3-1. 不在學籍資料中，顯示「...」
else:
    print('學號不存在，請重新輸入。')

