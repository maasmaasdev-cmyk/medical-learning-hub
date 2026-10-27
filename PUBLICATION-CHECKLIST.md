# 第1記事 公開前チェックリスト

対象: `_queue/draft-ercp-toha.md`

- [ ] `_config.yml` の `url` と `baseurl` を実際のGitHub情報へ変更
- [ ] `運営者名`を実名または公開名へ変更
- [ ] `about.md` に資格・専門領域・利益相反を追記
- [ ] `contact.md` に連絡方法を設定
- [ ] 記事の医学的内容と参考文献を本人が確認
- [ ] 施設差がある手順を断定していないか確認
- [ ] 著作権のある図表を無断掲載していないことを確認
- [ ] 医療レビュー後、`medical_review: true` に変更
- [ ] 公開する場合のみ `approved: true` に変更

## 即時公開

1. 対象記事の `medical_review` と `approved` を `true` にする。
2. GitHubへコミットする。
3. `Actions` から `Publish one approved article` を手動実行する。
4. 続く `Build and deploy Jekyll site` の成功を確認する。
