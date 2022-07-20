import csv
import re
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import pandas as pd
import numpy as np

filename = "noun_list_inproper.csv"
aiue_dic = {}
all = 0
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1][0] not in aiue_dic.keys():
            aiue_dic[row[1][0]] = [0,0]
        aiue_dic[row[1][0]][0] += 1
        all += 1

df = pd.DataFrame(
        index=["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","ゔ","が","ぎ","ぐ","げ","ご","ざ","じ","ず","ぜ","ぞ","だ","ぢ","づ","で","ど","ば","び","ぶ","べ","ぼ","ぱ","ぴ","ぷ","ぺ","ぽ"],
        columns=["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","ゔ","が","ぎ","ぐ","げ","ご","ざ","じ","ず","ぜ","ぞ","だ","ぢ","づ","で","ど","ば","び","ぶ","べ","ぼ","ぱ","ぴ","ぷ","ぺ","ぽ"])
df.fillna(0, inplace=True)

with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        last = ""
        i = -1
        while True:
            v = row[1][i]
            p1 = re.compile(r'[あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわゔがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽん]')
            if p1.fullmatch(v) != None:
                last = v
                break
            elif v == "ゃ":
                last = "や"
                break
            elif v == "ゅ":
                last = "ゆ"
                break
            elif v == "ょ":
                last = "よ"
                break
            else:
                i -= 1

        if last in aiue_dic.keys():
            aiue_dic[last][1] += 1
            df.at[row[1][0],last] += 1

dic = {}
for key,value in sorted(aiue_dic.items()):
    dic[key] = value[1]/value[0]
    print('{} : {}'.format(key,value))
print(all)
for key,value in sorted(dic.items(), key=lambda x:x[1]):
    print('{} : {}'.format(key,value))

df.to_csv("data_siritori_inproper.csv")
plt.figure(figsize=(18,18))
sns.heatmap(df,robust=True,square=True,cbar=False)
plt.savefig('siritori_inproper_heatmap.png')
