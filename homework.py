import csv
source_file = open("wedhomeworkcsv.csv")
file_reader = csv.reader(source_file)
file_data = list(file_reader)
n = int(file_reader.line_num)# 最多列數

def gender(i):
    gen = ""
    if i == 1:
        gen = "男性"
    if i == 2:
        gen = "女性"
    if i == 3:
        gen = "其他(如雙性人 hermaphrodite)"
    if i == 4:
        gen = "變性人"
    if i == 9:
        gen = "不詳或在病歷上未記載"
    return gen

# CASITE with 2num
c_w_2num = []
for i in range(1, n):
    c_w_2num.append(file_data[i][14])

# 總共分幾類
class_num = []
for i in c_w_2num:
    if i not in class_num:
        #print(i)
        class_num.append(i)
print("癌症代碼共有 " + str(len(class_num)) + " 類")

# 各類總例數
print("\n類別代碼: 例數")
for i in class_num:
    n = c_w_2num.count(i)
    
    print(i + ": " + str(n))


        
# ID col 0/ sex 1/ seq 6/ diagAge 12/ CASITE 2 num 14
# file_data[i][]
print("\n依個別病患摘要")
for i in range(1, 1604):
    print("病患ID: " + file_data[i][0])
    print("性別: " + gender(int(file_data[i][1])))
    print("初診年齡: " + file_data[i][12])
    print("罹癌類別代碼: " + file_data[i][14])
    print("序位: " + file_data[i][6])
    print("\n")

