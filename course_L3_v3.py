#%%
# ====== Section 1-1: 串列 ======
# ====== 選取元素 ======
responses = [200, 201, 400, 401, 404]
print(responses[1])
print(responses[-2])


#%%
# ====== 於二維串列選取元素 ======
responses_new = [
    [200, 201],
    [400, 401, 404],
    [500, 502, 503]
]
print(responses_new[1][2])

#%%
# ====== 排序 ======
exec_time = [386, 742, 601, 499, 525]
exec_time.sort()
print(exec_time)


#%%
# ====== 反排 ======
exec_time = [386, 742, 601, 499, 525]
exec_time.reverse()
print(exec_time)


#%%
# ====== 加入元素 ======
exec_time = [386, 742, 601, 499, 525]
exec_time.append(480)
exec_time = exec_time + [307,255]
exec_time


#%%
# ====== 剔除元素 ======
exec_time = [386, 742, 601, 499, 525]
exec_time.remove(499)
exec_time.pop(-1)
exec_time

#%%
# ====== 條件取元素 ======
exec_time = [386, 742, 601, 499, 525]
print(max(exec_time))
print(min(exec_time))
print(sum(exec_time))
print(len(exec_time))
print(exec_time.index(742))


# %%
# ====== 分段取串列 ======
exec_time = [386, 742, 601, 499, 525, 279]
print(exec_time[:2])
print(exec_time[3:])
print(exec_time[1:-1:2])
print(exec_time[::-1])


# %%
# ====== 練習1 ======
'''
請設計1「行車測速紀錄程式」, 
讓使用者輸入五次紀錄, 數字到小數點第二位
請將該五筆紀錄從最高排至最低
ex: 使用者依序輸入: 100.58, 97.88, 100.14, 98.73, 99.81
正確輸出: [100.58, 100.14, 99.81, 98.73, 97.88]
提示: 需轉換為浮點數, 可使用 float() 函式
'''

speeds=[]
count = 0
while count < 5:
    try:
        speed = float(input(f"請輸入第{count+1}的行車紀錄"))
        speeds.append(speed)
        count += 1
    except ValueError:
        print("請輸入數值")

speeds.sort(reverse=True)
print(speeds)


# %%
# ====== Section 1-2: 迴圈與例外 ======
# ====== for迴圈 ======
responses = [200, 201, 400, 401, 404]
for response in responses:
    print(response)


# %%
# ====== 雙重迴圈 ======
responses_new = [
    [200, 201],
    [400, 401, 404],
    [500, 502, 503]
]
for responses in responses_new:
    for response in responses:
        print(response)


# %%
# ====== 猜數字 ======
ans = 7
guess = 0
while guess != ans:
    guess = int(input("1-10中猜一個數字:"))
print("恭喜答對了! 答案是:", ans)


# %%
# ====== 猜數字: 另一種寫法 ======
ans = 5
guess = 0
while True:     # 無窮迴圈
    guess = int(input("1-10中猜一個數字:"))
    if guess == ans:
        print("恭喜答對了! 答案是:", ans)
        break
print("程式結束")


# %%
# ====== 猜數字: 加上例外處理 ======
ans = 5
guess = 0
while True:
    try:
        guess = int(input("1-10中猜一個數字:"))
    except:
        print("格式不符, 請重新輸入")
        continue
    if guess == ans:
        print("恭喜答對了! 答案是:", ans)
        break
print("程式結束")


# %%
# ====== 練習2: 難度-中高 ======
'''
responses_new = [
    [200, 201],
    [400, 401, 404],
    [500, 502, 503]
]
# 以下程式可依橫列順序執行
for responses in responses_new:
    for response in responses:
        print(response)

# 請撰寫一程式, 改為依直排順序執行, 意即按以下順序輸出
# 200 400 500 201 401 502 404 503
'''

#%%
# ====== Section 2: 字串處理 ======
# ====== 首尾清理 ======
raw_str = "    這是一個字串 "
print(f"原字串:{raw_str}...")
raw_str = raw_str.strip()
print(f"處理後字串:{raw_str}...")


# %%
# ====== 取代 ======
raw_str = "這是一個字串"
print(f"原字串:{raw_str}...")
raw_str = raw_str.replace("一","1")
print(f"處理後字串:{raw_str}...")


# %%
# ====== 大小寫轉換 ======
raw_str = "A sentence written by Drew"
print(f"原字串:{raw_str}...")
raw_str = raw_str.lower()
print(f"小寫後字串:{raw_str}...")
raw_str = raw_str.upper()
print(f"小寫後字串:{raw_str}...")


# %%
# ====== 字串分割 ======
raw_str = "這...是...一...句...話"
print(f"原字串:{raw_str}...")
str_splitted = raw_str.split("...")
print(f"分割後串列:{str_splitted}...")


# %%
# ====== 查找字串 ======
classmate_names = "Drew, Mary, Tom, Nancy"
print(f"Nancy位置:{classmate_names.find("Nancy")}...")
print(f"Peter位置:{classmate_names.find("Peter")}...")


#%%
# ====== Section 3: 偵錯 ======
def some_function():
    print("這是一個函式")
    print("這是第二句")
    print("這是第三句")

for i in range(5):
    print("執行迴圈...")
    if (i == 1 or i == 3):
        some_function()