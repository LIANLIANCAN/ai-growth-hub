import streamlit as st
import pandas as pd
import requests
import random
import datetime
import json
from streamlit_extras.add_vertical_space import add_vertical_space

# --- 頁面基本配置 ---
st.set_page_config(
    page_title="AI Growth Hub - 專業策略中心",
    page_icon="🌿",
    layout="wide"
)

# --- 自定義 CSS 樣式 (模擬原有的質感) ---
st.markdown("""
    <style>
    .main {
        background-color: #F1F4F1;
    }
    .stButton>button {
        border-radius: 12px;
        font-weight: 700;
        transition: all 0.3s;
    }
    .hero-box {
        background: linear-gradient(120deg, #94A696 0%, #7A8D7C 100%);
        padding: 2rem;
        border-radius: 25px;
        color: white;
        margin-bottom: 2rem;
    }
    .brand-bio-section {
        background-color: white;
        padding: 2rem;
        border-radius: 25px;
        border-left: 5px solid #FFBF00;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 初始化 Session State (跨頁面存儲) ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "brand_bio" not in st.session_state:
    st.session_state.brand_bio = ""
if "current_tab" not in st.session_state:
    st.session_state.current_tab = "工作台"

# --- 常數與 API 配置 ---
API_KEY = "" # 請在此填入您的 Gemini API Key
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key={API_KEY}"

# --- 工具函數 ---

def get_taipei_weather():
    """模擬原有的氣象獲取功能"""
    try:
        r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=25.03&longitude=121.56&current_weather=true')
        data = r.json()
        return f"{data['current_weather']['temperature']}度"
    except:
        return "氣候宜人"

def call_gemini(user_prompt, attachments=None):
    """呼叫 Gemini API 並維持 User/Model 交替"""
    system_prompt = """你現在是專業的成長顧問 AI。
    【文字輸出排版規範】
    1. **嚴禁使用表格 (Strictly No Tables)**：絕對禁止使用 Markdown 或 HTML 表格呈現資訊。
    2. **述敘式風格**：請改用「標題 (###)」配合「述敘性段落」來呈現所有分析。確保每一點分析都有完整的句子描述。
    3. **段落間距**：每個章節或重點之間請空出一行。
    4. **結構化模板 (僅限文字描述)**：
       媒體名稱、主題、目的、說明、視覺建議、文案。

    【結尾規範】
    必須加上這段問句：「你想主推什麼樣的商品？它有什麼特色呢？歡迎提供給我，讓我幫您產生 AI 中英文版的圖片咒語」
    """
    
    brand_context = f"\n\n【當前品牌基因】：\n{st.session_state.brand_bio or '未設定'}"
    
    # 構造歷史紀錄 (Gemini 要求必須是 User/Model 交替)
    contents = []
    for msg in st.session_state.chat_history[-10:]:
        contents.append({"role": msg["role"], "parts": [{"text": msg["content"]}]})
    
    # 加入當前訊息
    current_parts = [{"text": user_prompt}]
    if attachments:
        current_parts.insert(0, {"text": f"[資料參考]: {attachments}"})
        
    contents.append({"role": "user", "parts": current_parts})

    payload = {
        "systemInstruction": {"parts": [{"text": system_prompt + brand_context}]},
        "contents": contents,
        "tools": [{"google_search": {}}]
    }

    try:
        response = requests.post(API_URL, json=payload)
        result = response.json()
        text_out = result['candidates'][0]['content']['parts'][0]['text']
        return text_out
    except Exception as e:
        return f"⚠️ 系統連線繁忙或 API Key 無效。錯誤: {str(e)}"

# --- 側邊欄導覽 ---
st.sidebar.title("🌿 AI Growth Hub")
st.session_state.current_tab = st.sidebar.radio("切換視圖", ["工作台", "策略中心"])
if st.sidebar.button("🗑️ 清除對話歷史"):
    st.session_state.chat_history = []
    st.rerun()

# --- 主畫面邏輯 ---

if st.session_state.current_tab == "工作台":
    # Hero Section
    st.markdown("""
        <div class="hero-box">
            <h1>AI Growth Hub 策略增長系統</h1>
            <p>請設定品牌背景與數據，讓 AI 為您精準導航，提供具備市場洞察的商業建議。</p>
        </div>
        """, unsafe_allow_html=True)

    # STEP 1. 品牌基因設定
    st.markdown('<div class="brand-bio-section">', unsafe_allow_html=True)
    st.subheader("🧬 STEP 1. 品牌基因設定")
    st.caption("建立您的品牌大腦，確保所有企劃建議皆符合品牌調性與市場定位。")
    
    bio_input = st.text_area(
        "品牌基因輸入框",
        value=st.session_state.brand_bio,
        placeholder="品牌名稱、主力商品特徵、目標客群定位、核心競爭力...",
        height=150,
        label_visibility="collapsed"
    )
    
    col1, col2 = st.columns([1, 1])
    with col1:
        copy_prompt = "我現在要將我的品牌資訊導入 AI Growth Hub 策略系統。請幫我分析品牌名稱+品牌官網網址+品牌社群網址，並整理一份『品牌基因簡報』：品牌名稱、核心價值與語氣、目標客群特徵、三大核心產品及其賣點、主要競爭對手與差異化、目前行銷重點。請以純文字格式呈現。"
        st.code(copy_prompt, language=None)
        st.caption("☝️ 點擊代碼框右上角可複製分析指令")
        
    with col2:
        if st.button("儲存並更新基因", use_container_width=True, type="primary"):
            st.session_state.brand_bio = bio_input
            with st.spinner("AI 正在深度學習品牌 DNA..."):
                reply = call_gemini(f"(系統提示：載入品牌基因：\n{bio_input}\n\n請用熱情語氣回覆並總結特色。結尾詢問：今天我們從哪裡開始？)")
                st.session_state.chat_history.append({"role": "user", "content": f"更新品牌基因: {bio_input}"})
                st.session_state.chat_history.append({"role": "model", "content": reply})
                st.success("基因同步成功！已為您切換至策略中心。")
                # 跳轉
                # st.session_state.current_tab = "策略中心"
                # st.rerun()

    # STEP 2. 創意內容產出 (靈感引擎 3.0)
    st.divider()
    st.subheader("🎨 STEP 2. 創意內容產出 (靈感引擎 3.0)")
    c1, c2, c3 = st.columns(3)
    
    platforms = {"daily_social": "FB / IG", "line_private": "LINE 群組", "threads": "Threads"}
    
    def trigger_engine(p_key):
        weather = get_taipei_weather()
        month = datetime.datetime.now().month
        festivals = {1: "新年氣象", 2: "情人節氛圍", 5: "母親節商機", 12: "耶誕跨年熱點"}
        trend = random.choice(["AI 科技美學", "極簡質感生活", "永續消費觀念", "數位游牧高效生活"])
        
        prompt = f"【靈感引擎 3.0】計算結果：氣象({weather})、節慶({festivals.get(month, '本月市場熱點')})、趨勢({trend})。請以此為核心產出 {platforms[p_key]} 的深度述敘性企劃。"
        
        with st.spinner("靈感引擎運算中..."):
            res = call_gemini(prompt)
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            st.session_state.chat_history.append({"role": "model", "content": res})
            st.toast("企劃已生成，請前往策略中心查看！")

    if c1.button("📱 FB / IG", use_container_width=True): trigger_engine("daily_social")
    if c2.button("💬 LINE 群組", use_container_width=True): trigger_engine("line_private")
    if c3.button("🧵 Threads", use_container_width=True): trigger_engine("threads")

    # STEP 3. 數據分析
    st.divider()
    st.subheader("📊 STEP 3. 數據與檔案分析")
    uploaded_file = st.file_uploader("上傳銷售報表 (CSV 或 XLSX)", type=["csv", "xlsx"])
    if uploaded_file:
        if st.button("分析上傳數據"):
            df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('csv') else pd.read_excel(uploaded_file)
            data_summary = df.head(50).to_string() # 傳送部分數據給 AI
            with st.spinner("正在透視數據..."):
                reply = call_gemini("📈 請分析我上傳的銷售數據，指出增長亮點與建議。請用詳盡文字敘述，嚴禁表格。", attachments=data_summary)
                st.session_state.chat_history.append({"role": "user", "content": "分析銷售數據報表"})
                st.session_state.chat_history.append({"role": "model", "content": reply})
                st.success("分析完成！")

elif st.session_state.current_tab == "策略中心":
    st.title("🤖 策略顧問模式")
    st.caption("AI 已加載您的品牌基因，隨時準備進行深度企劃。")

    # 顯示歷史訊息
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 對話輸入
    if prompt := st.chat_input("請輸入您的需求..."):
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("model"):
            with st.spinner("顧問撰寫中..."):
                response = call_gemini(prompt)
                st.markdown(response)
                # 存入紀錄
                st.session_state.chat_history.append({"role": "user", "content": prompt})
                st.session_state.chat_history.append({"role": "model", "content": response})
