# mmd-table
MMD 動画作成時に、お借りしたものリスト

実際の表示はこちら <https://bagof.crap.jp/etc/mmdt/>

## テーブル作成手順
1. [mmdt.toml](mmdt.toml) に手動でデータを追加する
2. [toml2js.py](toml2js.py) を実行する
3. [mmdt.js](mmdt.js) が作られる
4. [index.html](index.html) から mmdt.js を読み込んで表示する
