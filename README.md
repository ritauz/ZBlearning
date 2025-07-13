# ZBlearning - 学習管理アプリ

本リポジトリは、他者と学習情報を共有できる学習管理Webアプリです。  
フロントエンド（Next.js）とバックエンド（FastAPI）は Docker コンテナ上で開発され、VS Code の Dev Containers に対応しています。

---

## 🚀 開発環境のセットアップ手順

### 1. 必要なツールをインストール

- [x] [Docker Desktop](https://www.docker.com/products/docker-desktop/)
  - WSL2 統合が有効になっていること（Ubuntu 推奨）
- [x] [WSL2](https://qiita.com/SAITO_Keita/items/148f794a5b358e5cb87b)
- [x] [Visual Studio Code](https://code.visualstudio.com/)
  - 拡張機能：  
    - `Dev Containers`（ms-vscode-remote.remote-containers）
    - `Docker`（ms-azuretools.vscode-docker）

---

### 2. リポジトリをクローン

```bash
git clone https://github.com/ritauz/ZBlearning.git
cd ZBlearning
```

---

### 3. Dev Container を起動（VS Code）
1. F1（または Ctrl + Shift + P）→ Dev Containers: Reopen in Container

2. 初回ビルド完了後、ターミナルで以下を実行：

## 🔧 フロントエンド（Next.js）
```bash
npm install
npm run dev         # http://localhost:3000
npm run test        # Vitestによる自動テスト
npm run type-check  # TypeScriptの型チェック
```
## 🔧 バックエンド（FastAPI）
```bash
make run            # http://localhost:8000
make test           # pytest + coverage
make type-check     # mypyによる型チェック
```

---

# 🧪 テストフレームワーク
| 層      | 使用技術                |
| ------ | ------------------- |
| フロント   | Vitest              |
| バックエンド | pytest, httpx, mypy |

---

# ✅ コミットルール
コミットメッセージは以下のフォーマットを使用：

```bash
<絵文字> #<課題番号> <概要>
例: 🐛 #42 バリデーションが機能していなかった問題を修正
```
用途別絵文字の一覧は commit_template.txt を参照してください。

---

# 📦 その他
- docker-compose.yml でフロントエンド・バックエンドを一括起動可能です。
- .devcontainer/ に各サービスの開発環境設定が含まれています。
- PRテンプレート・コミットテンプレート完備
