**日本語** | [English](README_en.md) | [简体中文](README.md)

## クライアントダウンロード

- [Android APK](client/ChinoNotify_android.apk)
- [iOS IPA](client/ChinoNotify_ios.ipa)
- [Windows x64 ZIP](client/ChinoNotify_windows_x64.zip)
- ### [全端 123 云盘ダウンロード](https://www.123865.com/s/Cbj7Vv-RPxuA)

# 声明

0. 本プロジェクトは商業利用を禁止します。<br>
1. クライアントはパッケージ化されていますが、オープンソースではありません。ダウンロードのみ提供します。<br>
2. サーバーはオープンソースで、自分でデプロイできます。<br>
3. ソフトウェア内で任意のサーバーを設定できます。<br>
4. ソフトウェアは完全に無料です。気に入ったら STAR を付けてください。<br>
5. このプロジェクトは AI によって開発されました。何らかの理由で気に入らない場合は、去ってください。
6. iOS 端のインストールには IPA に自分で署名する必要があります。そうしないと使用できません。
7. iOS 端のバックグラウンドプッシュは Apple 公式の APNs サービスに依存します。Apple デベロッパーアカウントが必要ですが、もちろん開設できません。
8. この非常にシンプルなサーバーに基づいて、自分のクライアントを開発することもできます。

[![image](https://img.cdn1.vip/i/691d8b2dbfdd8_1763543853.webp)](https://github.com/Chino1116/chino_blog)

# <font color="#4671bb">ChinoNotify</font>

ChinoNotify はクロスプラットフォームの通知ソフトウェアで、Android、iOS、Windows クライアントをサポートします。サーバーを自分でデプロイし、クライアントを任意のサーバーに接続できます。

## クライアント能力

1. 通知の一括削除。
2. 通知の詳細表示。
3. 通知の全文検索、および検索内容の一括削除。
4. 複数選択によるメッセージ状態の調整（既読/未読）。
5. 全プラットフォームでの通知削除/読書状態の擬似リアルタイム同期。
6. 設定保存後、更新ボタンをクリックする必要があるかもしれません（これは能力ではなく、私の怠惰さによるものです）。

## アプリスクリーンショット

<center class="half">
<img src="screenshot_1.png" width="300"/>
<img src="screenshot_2.png" width="300"/>
</center>
<center class="half">
<img src="screenshot_3.png" width="300"/>
<img src="screenshot_4.png" width="300"/>
</center>

## 以下は余談かもしれません

> Q: <font color="#4671bb">なぜこのものを作りたかったのですか？</font><br>A: ほとんどの Webhook プッシュソフトウェアには費用がかかったり、プッシュ量の制限があったり、プラットフォームの制限があったりするため、私の個人的なニーズを満たすために ChinoNotify が生まれました。<br><br>
> Q: <font color="#4671bb">技術スタック</font><br>A: サーバーは Python Flask + SQLite を使用。クライアントは Flutter を使用して全プラットフォームの迅速な開発を行います。（Mac がないため、Github Action を使用して iOS 端を何度もパッケージングとデバッグを繰り返し、一万年かかりました）

# <font color="#4671bb">デプロイチュートリアル</font>

## Webhook 呼び出し例

以下の方法でサーバーの Webhook インターフェースを呼び出して通知を送信できます：

### Curl

```bash
curl -X POST http://your-server:5000/webhook \
  -H "Authorization: Bearer your-token" \
  -H "Content-Type: application/json" \
  -d '{"title": "通知タイトル", "content": "通知内容"}'
```

### JavaScript (Node.js)

```javascript
fetch('http://your-server:5000/webhook', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer your-token',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    title: '通知タイトル',
    content: '通知内容'
  })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

### PHP

```php
<?php
$url = 'http://your-server:5000/webhook';
$data = array('title' => '通知タイトル', 'content' => '通知内容');
$options = array(
    'http' => array(
        'header'  => "Authorization: Bearer your-token\r\nContent-Type: application/json",
        'method'  => 'POST',
        'content' => json_encode($data),
    ),
);
$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);
if ($result === FALSE) {
    echo "Error";
} else {
    echo $result;
}
?>
```

### Python

```python
import requests

url = 'http://your-server:5000/webhook'
headers = {
    'Authorization': 'Bearer your-token',
    'Content-Type': 'application/json'
}
data = {
    'title': '通知タイトル',
    'content': '通知内容'
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

## サーバーデプロイ

### 前提条件

Python 3.x がインストールされていること。

### 1. 依存関係のインストール

server フォルダに入り、以下のコマンドを実行して Python 依存ライブラリをインストールします。

```bash
pip install -r requirements.txt
```

### 2. サーバーの実行

server フォルダに入り、以下のコマンドを実行します。バックエンドは <font color="#4671bb">localhost:5000</font> で実行されます。

```bash
python run.py
```

### 3. クライアントの設定

クライアントソフトウェアでサーバーアドレスをデプロイアドレスに設定します。

### これでサーバーのデプロイは終了です

## ここまで読んでくれたあなたはきっとこのプロジェクトに興味があるはずです。無料の Star を付けてください！

### Star トレンド

[![Star History Chart](https://api.star-history.com/svg?repos=Chino1116/chino_notify_public&type=date&legend=top-left)](https://www.star-history.com/#Chino1116/chino_notify_public&type=date&legend=top-left)
