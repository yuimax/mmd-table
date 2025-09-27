import tomllib
import json

# TOMLファイルを読み込む
toml_file = "mmdt.toml"
with open(toml_file, 'rb') as f:
    data = tomllib.load(f)

# item 配列と uses 配列を取り出す
item_list = data['item']
uses_list = data['uses']

# 配列 item_list を、辞書 item_dict に変換
item_dict = {}
for item in item_list:
    item_id = item.pop('id')
    if item_id in item_dict:
        print(f"ERROR: ID \"{item_id}\" が重複しています")
        exit(1)
    item_dict[item_id] = item
    
# item_dict と uses_list をまとめてオブジェクト db を作る
db = { "item": item_dict, "uses": uses_list }    

# オブジェクト db を JSON に変換する
json_str = json.dumps(db, indent=2, ensure_ascii=False)

# JavaScript の代入文を作り、"mmdt.js" に書き込む
js_file = "mmdt.js"
with open(js_file, 'w', encoding='utf8') as f:
    f.write(f"const db = {json_str};\n")

print(f"CREATED: {js_file}")
