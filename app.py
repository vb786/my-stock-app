import streamlit as st
import datetime
import akshare as ak
import pandas as pd

st.set_page_config(page_title="乾坤五行量化系统", layout="centered")

st.title("☯️ 乾坤五行量化择时模型")
st.markdown("---")

# 1. 输入区域
st.sidebar.header("实时参数输入")
open_p = st.sidebar.number_input("请输入今日上证指数开盘价", value=3900.0, step=0.01)
analyze_btn = st.sidebar.button("开始推演行情")

# 2. 核心逻辑（以 2026-03-30 癸卯日为例）
def run_model(op):
    with st.spinner('正在调取实时阴阳能量...'):
        try:
            df = ak.stock_zh_a_spot_em()
            total = len(df)
            up = len(df[df['涨跌幅'] > 0])
            yang_ratio = (up / total) * 100
        except:
            yang_ratio = 50.0
            
    # 简单的五行推演展示
    st.subheader("📊 今日行情推演报告")
    col1, col2 = st.columns(2)
    col1.metric("市场阳性率", f"{yang_ratio:.1f}%")
    col2.metric("建议仓位", "70%" if yang_ratio > 55 else "30%")

    st.info("【梅花卦象】：当日卦位偏向 [震雷]，震荡特征明显。")
    
    st.success("【优选板块】：医药生物（木）、计算机（水）")
    st.warning("【规避板块】：房地产、建筑（土）")
    
    st.write("### 💡 具体操作建议")
    if yang_ratio > 55:
        st.write("✅ **多头占优**：行情生发力强，建议持股待涨。")
    else:
        st.write("⚠️ **空头占优**：流动性收缩，建议逢高减仓。")

if analyze_btn:
    run_model(open_p)
else:
    st.write("请在左侧输入开盘价并点击开始。")
