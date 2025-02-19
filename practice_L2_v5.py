'''
===================== 第二堂課 練習題 =====================
'''

#%%
'''
===================== 練習一 =====================
鍾QA正在測試某程式不同版本執行時間, 
他有一個串列:process_time_latest, 存放A程式執行毫秒的數據(最新一筆置於最後)
ex: process_time_latest = [385, 400, 395, 375, 401]
分別代表近五次A程式執行時間, 最新一次為401毫秒

程式步驟:
1. 您的程式開始時, 能讓使用者再輸入一筆最新測試結果, 例如 389
2. 若該結果與最新5筆數據相比排前三名(時間越短, 排名越高), 則顯示pass, 否則顯示fail
3. 顯示完成後, 這筆數據須加入process_time_latest串列, 並置放於最新的一筆; 
以本範例來說, 執行後process_time_latest: [385, 400, 395, 375, 401, 389]
下一回合執行時, 重新從步驟1開始, 並會跟最新的五筆 (從400這筆~389這筆)比較

其他功能:
若於程式步驟1, 使用者輸入exit, 則終止本程式

範例:
第一回合
process_time_latest = [385, 400, 395, 375, 401]
使用者輸入389 
因389跟最新五筆比較, 列為前三名, 終端機顯示pass
第二回合
process_time_latest = [385, 400, 395, 375, 401, 389]
使用者輸入399
因399跟最新五筆比較, 列為前四名, 排在前三以外, 故終端機顯示fail

提示:
1. 請考慮使用者有意/無意輸入不符格式, 造成例外的狀況
2. 可用list.sort()來排序 (增加及刪除也放到提示)
'''
#%%
process_time_latest = [385, 400, 395, 375, 401]
process_time_latest.sort()
while True:
    new_time = input("最新一次數據：")
    if new_time == "exit":
            break
    try:
        new_time = int (new_time)
    except:
        print("請輸入整數")
    else:    
        if new_time <= process_time_latest[2]:
            print(f'最新一次數據為:{new_time} - 結果為Pass')
        else:
            print(f'最新一次數據為:{new_time} - 結果為Fail')    
        process_time_latest.append(new_time)
        process_time_latest.sort()
        print(f'目前數據為:{process_time_latest}')
   

# 以下請編寫您的練習一程式



#%%
'''
===================== L2作業 =====================
以練習題為基礎, 調整功能如下
0. 鍾QA發現有時主管會調整排名標準, 請將此程式從"前3名pass"改為一個"前n名pass"的函式, n為參數
1. 程式步驟調整如下
    a. 使用者輸入數據
    b. 數據新增到csv
    c. 查看新數據是否符合前n名標準
2. csv須保留所有舊數據, 不做任何刪除
3. 加分題: 查看前n名的邏輯時, 嘗試不使用sort()來達成. 請參考氣泡排序法檔案 (Bubble.zip)
'''
# 以下請編寫您的L2作業