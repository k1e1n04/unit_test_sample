# unit_test_sample

## 概要

ユニットテスト説明プログラムです。

### 必要なもの

- Python 3.8 以降
※anacondaの仮想環境が起動している場合は停止してください。

### 参考資料
- [pytest公式](https://pleiades.io/help/pycharm/pytest.html)
- [pytestチートシート](https://qiita.com/kawano_fumihiko/items/9518d94b2f6efe23050d)

### インストール

以下は、`unit_test_sample` をローカルで開発するためのセットアップ手順です。

1. GitHub から `unit_test_sample` リポジトリをクローンします。

2. 新しい仮想環境を作成します。

```shell
$ python -m venv .venv
```

3. 仮想環境をアクティブにします。
MacOS/Linux の場合:

```shell
$ source .venv/bin/activate
```

Windows の場合:

```shell
$ .\.venv\Scripts\activate
```

4. 依存関係をインストールします。

```shell
$ pip install --upgrade pip
$ pip install -e .
```

### テスト実行
以下のコマンドを実行して、ユニットテストを実行します。

```shell
$ pytest
```

以下のコマンドでカバレッジを出力できます。

```shell
pytest -v --cov=packages --cov-branch
```

以下のコマンドでカバレッジをHTMLに出力できます。

```shell
pytest -v --cov-branch --cov-report html
```

### サンプルプログラム実行(api.py除く)

```shell
$ python main.py
```
