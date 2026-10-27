# 胆膵メディカルラーニング 完成版テンプレート

GitHub Pages + Jekyll + GitHub Actionsで動く、維持費0円から始められる医療教育サイトです。AI APIや有料サービスには依存しません。

## 公開前に必ず変更する項目

1. `_config.yml` の `url` を `https://GitHubユーザー名.github.io` に変更
2. `_config.yml` の `baseurl` を `/リポジトリ名` に変更（`ユーザー名.github.io`リポジトリなら空文字）
3. `運営者名`、資格、専門、問い合わせ先を実情報へ変更
4. `privacy.md` を、実際に使う広告・解析サービスに合わせて修正
5. サンプル記事と下書きの医学的内容・一次資料を人が確認
6. `_queue` 内で公開してよい記事だけ `approved: true` に変更

## GitHubで公開する手順

1. GitHubでパブリックリポジトリを作る（例 `medical-learning-hub`）。
2. このフォルダの中身をリポジトリ直下へアップロードして `main` ブランチへコミット。
3. `Settings` → `Pages` → `Build and deployment` → `Source` で `GitHub Actions` を選択。
4. `Actions` タブで `Build and deploy Jekyll site` が成功したことを確認。
5. `Settings` → `Actions` → `General` → `Workflow permissions` で、定期公開を使う場合は `Read and write permissions` を許可。
6. サイトURL、ナビゲーション、404、sitemap.xml、robots.txtを確認。

## 記事作成と自動公開

1. `_queue/draft-template.md` を複製し、ファイル名を `draft-english-slug.md` にする。
2. 執筆、引用確認、医療レビューを行う。
3. レビュー済みなら `medical_review: true`、公開予約するなら `approved: true` に変更。
4. 毎週のワークフローが、ファイル名順で最初の承認済み記事を1本だけ `_posts` へ移動。
5. 手動実行は `Actions` → `Publish one approved article` → `Run workflow`。

重要: AIで未確認の医学記事を自動生成・公開しない設計です。完全自動生成ではなく「レビュー済み原稿の自動公開」に限定しています。

## ローカル確認（任意）

```bash
bundle install
bundle exec jekyll serve
```

## AdSense

審査合格後に `_config.yml` の `adsense_client` を設定し、`_includes/ad-slot.html` に管理画面で発行された広告ユニットを貼ります。審査前は空欄のままにしてください。

## Search Console

所有権確認用メタタグの値を `_config.yml` の `google_site_verification` に設定します。サイトマップは `/sitemap.xml` です。

## ライセンス

コードはMIT License。記事本文・ブランド素材は利用者が権利を管理してください。
