import csv
import re
import regex
from pykakasi import kakasi
import MeCab

tagger = MeCab.Tagger("-p")
p = re.compile(r'[あ-んア-ン\u2E80-\u2FDF\u3005-\u3007\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\U00020000-\U0002EBEF]')
kakasi = kakasi()
kakasi.setMode('J', 'H') #漢字からひらがなに変換
kakasi.setMode("K", "H") #カタカナからひらがなに変換
conv = kakasi.getConverter()

def get_pos(word):
    # 制約付き解析の形態素断片形式にする
    p_token = f"{word}\t*"
    # 出力のEOS部分を捨てる
    parsed_line = tagger.parse(p_token).splitlines()[0]
    feature = parsed_line.split("\t")[1]
    # ,(カンマ)で区切り、品詞,品詞細分類1,品詞細分類2,品詞細分類3 の4項目残す
    pos_list = feature.split(",")
    return pos_list

def main():
    csvPath = "word-level-japanese.tsv"
    filename = "noun_list.csv"
    with open(filename,"w") as n_f:
        pass

    with open(csvPath) as f:
        reader = csv.reader(f, delimiter = '\t')
        for row in reader:
            m = p.match(row[0])
            if m==None or row[0]=="":
                continue
            pos_list = get_pos(row[0])
            if "名詞" in pos_list and "固有名詞" not in pos_list:
                hiraganaStr = conv.do(row[0])
                if re.match(r'[あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわゔがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ]',hiraganaStr) == None:
                    continue
                row.insert(1, hiraganaStr)
                with open(filename,"a") as n_f:
                    csv.writer(n_f).writerow(row)


if __name__ == '__main__':
    main()
