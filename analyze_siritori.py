import csv
import re
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import pandas as pd
import numpy as np


filepath = "data_siritori.csv"
aiueo = ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","ゔ","が","ぎ","ぐ","げ","ご","ざ","じ","ず","ぜ","ぞ","だ","ぢ","づ","で","ど","ば","び","ぶ","べ","ぼ","ぱ","ぴ","ぷ","ぺ","ぽ"]

df = pd.read_csv(filepath,index_col=0)
comp_df = pd.DataFrame(
        index=aiueo,
        columns=aiueo)

for s1 in aiueo:
    for s2 in aiueo:
        comp_df.at[s1,s2] = df.at[s1,s2]/df.at[s2,s1]
comp_df.to_csv("only_noun_letter_strong.csv")
plt.figure(figsize=(18,18))
sns.heatmap(df,robust=True,square=True,cbar=False)
plt.savefig('only_noun_letter_strong.png')
