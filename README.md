# 各ファイルについて

```
github-emoji-scraping
├─.editorconfig ←各種ファイルの規則（文字コードや改行コード、インデントなど）が記載している
├─.gitignore ←Gitの管理対象から外す対象を記載している
├─README.md ←本ファイル
├─config.ini.sample ←このファイルをもとにファイルを作成し各個人ごとの情報を記載する
├─requirements.txt ←このプログラムを動かすうえで必要なパッケージが記載されている
└─github-emoji-scraping
   ├─main.py  ←エントリーポイント
   └─config.py ←config.iniを読み込むためのソース
```

# 使い方

1. python環境構築

```
$ python -m venv .venv

$ .\.venv\Scripts\Activate.ps1 # or $ source ./.venv/Scripts/activate

$ python -V
Python 3.7.4

$ pip install -r requirements.txt

```

2. config.iniの作成

```
$ cp config.ini.sample config.ini
```

3. GitHubのAccessTokeを発行しconfig.iniに書き込む

4. プログラムをCLIで実行する

```
$ cd github-emoji-scraping
$ python main.py
```
