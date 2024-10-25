import json
import MeCab

# JSONファイルの読み込み
with open('./data/wrimev4.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# MeCabの初期化（今回は、標準の分かち書き）
mecab = MeCab.Tagger("-Owakati")

# "Sentence"の単語分割を行い、その結果をsplit_sentenceに保存
for entry in data:
    if "Sentence" in entry:
        # Sentenceを分かち書きしてsplit_sentenceに追加
        sentence = entry["Sentence"]
        split_sentence = mecab.parse(sentence).strip()  # MeCabで分かち書き
        
        # split_sentenceという要素を追加
        entry["Split_sentence"] = split_sentence

# JSONファイルに結果を書き込む
with open('./wrimev4_add_split.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("単語分割した結果をdata_with_split.jsonに保存しました。")
