# RR & 期待値 カルキュレーター

`rr_calculator.py` は、Streamlit を用いて「利確（リターン）」「損切（リスク）」の比率から **RR（Risk-Reward）**、**トントン勝率（p₀）**、および**期待値（E）** をインタラクティブに計算・可視化するウェブアプリです。モバイルにも対応しており、生徒さんやトレーダーの方がスマホで直感的に操作できます。

---

## 📋 特長

- **RR** を「リスク 1 に対して利確 何 」の比率（例: `6.0 : 1`）で表示
- **トントン勝率 (p₀)** を「〇％ ≈ △回に1回勝てばトントン」とわかりやすく解説
- **想定勝率** の入力欄（小数点以下1位）で、**期待値 E** をリアルタイム計算
- **期待値 E** を「長期的にプラス/マイナス」コメント付きで表示
- スマホ・PC 両対応のシンプル UI

---

## 🚀 インストール & 実行

1. **リポジトリをクローン** (既にクローン済みの場合はスキップ)
   ```bash
   git clone https://github.com/<ユーザー名>/akami_lab.git
   cd akami_lab/app/rr_calculator
   ```

2. **仮想環境の準備** (Mac の例)
   ```bash
   python3 -m venv ~/myenv_rr
   source ~/myenv_rr/bin/activate
   ```

3. **依存パッケージをインストール**
   ```bash
   pip install -r ../../requirements.txt
   ```

4. **アプリを起動**
   ```bash
   streamlit run rr_calculator.py
   ```

5. ブラウザで開く（自動で開かない場合は `http://localhost:8501`）

---

## 🛠️ 主要コード解説

- **利確 / 損切 スライダー**: `st.slider` で `%` 値を取得
- **RR 計算**: `rr = take_profit / stop_loss` → `f"{rr:.1f} : 1"`
- **p₀ 計算**: `p0 = 1 / (rr + 1)` → `%` 表示 & 回数換算
- **想定勝率入力**: `st.number_input(format="%.1f")`
- **期待値 E**: `E = p × G - (1-p) × R` → プラス/マイナスを色分け

---

## ⚙️ カスタマイズ

- CSS は `st.markdown(...unsafe_allow_html=True)` 部分を編集
- レイアウト変更は `st.columns` の数や `st.set_page_config(layout="wide")` を調整
- テーマカラーは Streamlit の [Theme 設定](https://docs.streamlit.io/library/advanced-features/theming) で変更可能

---

## 📜 ライセンス

このプロジェクトは MIT License のもとで公開されています。詳細は [LICENSE](../../LICENSE) をご覧ください。

