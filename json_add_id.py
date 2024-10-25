import json

# JSONファイルにidを追加する関数（idは1から始まる）
def add_id_to_json(input_json_file_path, output_json_file_path):
    # JSONファイルを読み込む
    with open(input_json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    # 各エントリにidを追加（1から始まる）
    for index, entry in enumerate(data, start=1):
        entry['id'] = index  # idを1から始める
    
    # 新しいJSONファイルに書き込む
    with open(output_json_file_path, 'w', encoding='utf-8') as output_json_file:
        json.dump(data, output_json_file, ensure_ascii=False, indent=4)

# 使用例
input_json_file_path = './data/data.json'
output_json_file_path = './data/wrimev4.json'

add_id_to_json(input_json_file_path, output_json_file_path)
