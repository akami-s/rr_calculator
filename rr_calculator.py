# rr_calculator.py – Streamlit app for Risk‑Reward & Expected Value
# Author: ChatGPT (OpenAI o3)
# Usage: streamlit run rr_calculator.py

import streamlit as st
import math

# ----- Page configuration -----
st.set_page_config(
    page_title="RR Calculator",
    page_icon="📈",
    layout="centered",  # mobile‑friendly
)

# ----- Custom CSS for nicer mobile look -----
st.markdown(
    """
    <style>
    div[data-testid="stMetric"] > div > div {
        font-size: 1.6rem;            /* bigger numbers on phones */
    }
    h2 {
        margin-top: 0.2em;
        margin-bottom: 0.2em;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----- UI -----
st.title("📈 RR & 期待値 カルキュレーター")

col1, col2 = st.columns(2)
with col1:
    tp_pct: float = st.slider("利確 (%)", min_value=5.0, max_value=200.0, value=20.0, step=1.0)
with col2:
    sl_pct: float = st.slider("損切 (%)", min_value=1.0, max_value=50.0, value=10.0, step=1.0)

# ----- Core calculations -----
rr: float = tp_pct / sl_pct  # Risk‑Reward Ratio (decimal)
# Display as “リスク 1 に対して利確 側” format, return side one decimal
rr_ratio: str = f"{rr:.1f} : 1"  # e.g. “6.0 : 1”

p0: float = 1 / (rr + 1)  # Breakeven win‑rate (decimal)
p0_percent: float = p0 * 100
p0_ratio: str = f"{round(1/p0)}回に1回"  # e.g. “3回に1回”

# ----- Display RR & p0 -----
st.subheader("RR と トントン勝率 (p₀)")
met_rr, met_p0 = st.columns(2)
met_rr.metric("RR (利確 : 損切)", rr_ratio)
met_p0.metric("トントン勝率", f"{p0_percent:.1f}%  ≈  {p0_ratio}")
# Full explanation below metric (wrapping allowed)
st.markdown(f"<small>→ {p0_ratio}勝てば<strong>トントン</strong>です</small>", unsafe_allow_html=True)

# ----- User win‑rate input & expected value -----
win_rate_input: float = st.number_input(
    "想定勝率 (%)（過去実績やバックテスト値）",
    min_value=0.0, max_value=100.0, value=50.0, step=0.1,
    format="%.1f"
)
win_rate: float = win_rate_input / 100

E: float = win_rate * tp_pct - (1 - win_rate) * sl_pct
color = "green" if E >= 0 else "red"
comment = "長期的にプラス ✅" if E >= 0 else "長期的にマイナス ❌"

# ----- Expected value -----
st.subheader("期待値 (E)")
st.markdown(
    f"<h2 style='color:{color}'>E = {E:.1f}%（{comment}）</h2>",
    unsafe_allow_html=True,
)

# ----- Footnote -----
st.caption("RR = 利確 ÷ 損切 | p₀ = 1／(RR + 1) | E = 勝率×利確 − (1−勝率)×損切")