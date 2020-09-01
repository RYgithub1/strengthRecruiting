# README

## トップイメージ


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

候補者が、自らの"強み"を説明文と動画でアピールを行う事ができます。  
企業や個人事業主は、気になる人がいたらスカウトを実施できるWebアプリケーションです。

## コンセプトと思い

これからの世の中は更に、やる気と実力のある個人が世界中のコミュニティと繋がり、自らの特徴を活かして社会貢献する時代になると考えます。  
しかしながら、世の中に採用サイトは数多くあるものの、強みのみに注目する採用サイトが見当たらない状況です。  
他の事はなんら出来ないけど、ある特定の事に物凄く秀でた方が世の中に沢山おり、私にとって魅力的な存在です。  
採用の多様性を広げ、一人でも多くの人が輝ける・楽しめる社会をつくりたいと思っています。  
そこで今回、人の強みだけに集中して採用活動が行えるWebサイトの構築へ挑戦しました。  
まだまだ実装したい機能が沢山ありますが、土台部分が出来たためβ版とします。  

---

## 内容ーーー機能一覧

### トップページ

- xxx
- xxx


### 詳細ページ（未ログイン）

### スカウトページ（未ログイン）

### 詳細ページ（既ログイン）_自分の投稿

### 詳細ページ（既ログイン）_他人の投稿

### サインアップページ

### プロフィール新規作成ページ


## 工夫

- 複数ユーザー登録

  - 年齢性別国籍に関わらず、候補者は、自らの強みをアピール可能

- 動画投稿

  - 機械学習ライブラリPillowを用いて実装
  - 動画の投稿、再生、変更が可能
  - 候補者一覧ページでは、代替でサムネイル画像を表示
  
- スカウト
  - ログイン有無に関わらず、気になる候補者に向けて、そのプロフィールページからスカウトが可能
  - スカウトメッセージの内容は、本人以外には表示されない設計
  
## 今後の実装予定

1. □ 候補者と企業のマッチング
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
| name     | string | null: false |
| email    | string | null: false |
| password | string | null: false |

#### Association(Users)

- has_many :posts

### Posts Table

| Column       | Type   | Options                 |
| ------------ | ------ | ----------------------- |
| author       | string | foreign_key: true       |
| title        | string | max_length: 200         |
| text         | text   | blank: true             |
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
| post         | string | null: false, foreign_key: true |
| author       | string | max_length: 200                |
| text         | string |                                |
| created_date | string | auto_now_add=True              |

#### Association(Scouts)

- belongs_to :post

---

## 著者

- 製作者：R.O.
- [GitHub](https://github.com/RYgithub1)
