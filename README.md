# README

## トップイメージ

<img width="797" alt="django_headerImage" src="https://user-images.githubusercontent.com/62828568/91919964-a314fa80-ed02-11ea-8578-ded1fc27147e.png">

![python](https://img.shields.io/badge/-Python-yellow)
![django](https://img.shields.io/badge/-Django-darkgreen)
![sqlite](https://img.shields.io/badge/-SQLite-blue)
![html](https://img.shields.io/badge/-HTML-orange)
![css](https://img.shields.io/badge/-CSS-lightblue)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/RYgithub1/strengthRecruiting)

## アプリケーション名

_Strength Recruiting!_  
（ストレングス リクルーティング！： 強み採用のプラットフォームアプリ）

## 概要

候補者が、自らの"強み"を説明文と動画でアピールできます。  
（企業や個人事業主は、）気になる人がいたらスカウトを実施できます。

## コンセプトと思い

これからの世の中は更に、やる気と実力のある個人が世界中のコミュニティと繋がり、自らの特徴を活かして社会貢献する時代になると考えます。  
しかしながら、世の中に採用サイトは数多くあるものの、強みのみに注目する採用サイトが見当たらない状況です。  
他の事はなんら出来ないけど、ある特定の事に物凄く秀でた方が世の中に沢山おり、私にとって魅力的な存在です。  
採用の多様性を広げ、一人でも多くの人が輝ける・楽しめる社会をつくりたいと思っています。  
そこで今回、人の強みだけに集中して採用活動が行えるWebサイトの構築へ挑戦しています。  
まだまだ実装したい機能が沢山ありますが、土台部分を実装したためβ版とします。  

---

## 内容

### トップページ（未ログイン）

<img width="783" alt="django_toppage" src="https://user-images.githubusercontent.com/62828568/91917489-0733c080-ecfb-11ea-8e94-736081012a8d.png">

- トップページにて、全候補者のプロフィールを一覧できます。
- ヘッダーの、人型アイコンからサインアップ、矢印四角アイコンからログイン可能です。
- 表示項目は、「作成日時・氏名・スカウト数・強み説明文・強みサムネイル」です。
- 氏名ないしサムネイル画像をクリックすると、詳細ページに遷移します。

### 詳細ページ（未ログイン）

<img width="790" alt="django_detail_withoutLogin" src="https://user-images.githubusercontent.com/62828568/91917529-25012580-ecfb-11ea-8c3a-c2df659d56e1.png">

- 強み動画の再生が可能です。
- プロフィール投稿者本人でない場合、動画の下方に、スカウティングボタンとスカウト数のみが表示されます。

### スカウトページ（未ログイン）

<img width="786" alt="django_scout_withoutLogin" src="https://user-images.githubusercontent.com/62828568/91917559-38ac8c00-ecfb-11ea-8943-294ab4342637.png">

- スカウティングボタンを押下すると、「New Scout」作成ページに遷移します。
- 個人名や社名、連絡先やスカウト内容を記載して、「Send」ボタンを押すと、スカウトメッセージを届けられます。

### 詳細ページ（既ログイン）_自分の投稿

<img width="782" alt="django_detail_afterLogin_v1" src="https://user-images.githubusercontent.com/62828568/91917570-48c46b80-ecfb-11ea-95d4-6d22d04faca2.png">

- （サインアップとプロフィール新規投稿については、後ほど記載します。）
- ヘッダーよりログインを行うと、ユーザー名がヘッダーに表示されます（Hi there. 'User Name'）。
- ログイン後に自分の投稿をクリックすると、編集ボタン(鉛筆マーク)や削除ボタン(バツマーク)が表示されます。ここからプロフィールのアップデートを行います。

<img width="782" alt="django_detail_afterLogin_v2" src="https://user-images.githubusercontent.com/62828568/91917593-5974e180-ecfb-11ea-8c14-ff95632ddef1.png">

- また、投稿者本人が自らのプロフィールページを訪れている場合、スカウティングボタンが消え、各組織からのスカウト内容が表示されます。
- スカウト内容を確認して、積極的に連絡を行いましょう！

### 詳細ページ（既ログイン）_他人の投稿

<img width="790" alt="django_detail_afterLogin_anotherProfile" src="https://user-images.githubusercontent.com/62828568/91917618-685b9400-ecfb-11ea-8c08-1a79cb3b06ce.png">

- 例えログイン済みだとしても、ログインユーザー自身が投稿したプロフィールではない場合、編集・削除ボタンやスカウト内容は表示されません（他社には見られません）。

### サインアップページ

<img width="783" alt="django_signup" src="https://user-images.githubusercontent.com/62828568/91917635-77424680-ecfb-11ea-94d6-08c30ee071fc.png">

- ヘッダーの人型アイコンをクリックすると、サインアップページに遷移します。
- ユーザー名・メールアドレス・パスワードが、サインアップに際して必要です。
- ログインする際は、ユーザー名とパスワードだけで可能です。

### 新規プロフィール作成ページ

<img width="784" alt="django_makeProfile_v1" src="https://user-images.githubusercontent.com/62828568/91917646-80cbae80-ecfb-11ea-81e7-a70ff56e818c.png">

- ログイン後に、ヘッダーに表示される家アイコンを押下すると、新規プロフィール作成ページに遷移します。
- 自らの強みを入力してSaveボタンを押すと、次の画像のように一覧ページの最下方へ情報が追加されます。

<img width="783" alt="django_mekeProfile_v2" src="https://user-images.githubusercontent.com/62828568/91917651-86c18f80-ecfb-11ea-9822-6eff33913381.png">

- 因みに、1ユーザーアカウントにつき、複数のプロフィール作成が可能な設計としています。


## 工夫

- 複数ユーザー登録

  - サインアップからユーザーアカウントを作成し、プロフィールの登録が可能です。

- 動画投稿

  - 機械学習ライブラリのPillowを用いて実装しています。
  - 動画の投稿、再生、変更が可能です。
  - 候補者一覧ページでは、代替でサムネイル画像を表示しています。

- スカウト

  - ログイン有無に関わらず、気になる候補者に向けて、そのプロフィールページからスカウトが可能です。
  - スカウトメッセージの内容は、本人以外には表示されない設計にしています。

## 今後の実装予定

1. □ 候補者と企業の志向性マッチング
2. □ メッセージ交換
3. □ フォロー・フォロワー（お気に入り）

---

## 開発環境

- Python（3.8.5）
- Django（2.2.15）
- HTML5（5.1.2）
- CSS3
- SQLite（3.28.0）
- Git（2.26.0）

## DB 設計

### Users Table

| Column   | Type   | Options     |
| -------- | ------ | ----------- |
| name     | string | null: False |
| email    | string | null: False |
| password | string | null: False |

#### Association(Users)

- has_many :posts

### Posts Table

| Column       | Type   | Options                 |
| ------------ | ------ | ----------------------- |
| author       | string | ForeignKey: True       |
| title        | string | max_length: 200         |
| text         | text   | blank: True             |
| thumbnail    | image  | null: True, blank: True |
| upload       | file   | null: True              |
| created_date | date   | auto_now_add: True      |
| updated_date | date   | auto_now: True          |

#### Association(Posts)

- belongs_to :user
- has_many :scouts

### Scouts Table

| Column       | Type   | Options                        |
| ------------ | ------ | ------------------------------ |
| post         | string | null: False, ForeignKey: True |
| author       | string | max_length: 200                |
| text         | string |                                |
| created_date | string | auto_now_add=True              |

#### Association(Scouts)

- belongs_to :post

---

## 著者

- 製作者：R.O.
- [GitHub](https://github.com/RYgithub1)
