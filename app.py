import streamlit as st
import pandas as pd
import requests
import random
import datetime

# --- 1. 頁面基礎配置 ---
st.set_page_config(
    page_title="AI Growth Hub - 策略中心",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. API 設定 (請確保在 Streamlit Cloud Secrets 設定 GEMINI_API_KEY) ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except:
    API_KEY = "" # 本地測試可暫時填寫於此

API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# --- 3. 自定義 CSS (修正字體過擠與手機版顯示) ---
st.markdown("""
    <style>
    .stApp { background-color: #F8FAF8; }
    /* 解決文字擠在一塊的問題 */
    .stMarkdown p { line-height: 1.8 !important; margin-bottom: 1.2rem !important; }
    .stMarkdown h3 { margin-top: 1.5rem; color: #2D3A3A; border-bottom: 2px solid #E2E8F0; padding-bottom: 5px; }
    /* 對話框樣式優化 */
    .stChatMessage { border-radius: 15px; border: 1px solid #E2E8F0; background: white !important; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
    /* 移除 Streamlit 頂部預設工具列 */
    div[data-testid="stToolbar"] { display: none; }
    /* 標籤頁字體加粗 */
    .stTabs [data-baseweb="tab"] { font-weight: 700; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. 初始化 Session 狀態 ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "brand_bio" not in st.session_state:
    st.session_state.brand_bio = ""

# --- 5. 核心 AI 函數 ---
def call_gemini(user_query, data_attachment=None):
    if not API_KEY:
        return "❌ 尚未設定 API Key。請至 Streamlit Cloud 設定 Secrets。"

    # 系統指令：嚴格執行敘述式風格，禁絕表格
    system_prompt = f"""你現在是專業的 AI Growth Hub 成長顧問。
    【品牌背景】：{st.session_state.brand_bio or "尚未提供"}
    
    【文字輸出排版規範】：
    1. **絕對禁止產出表格**：無論如何都不要使用表格，這在手機上體驗很差。
    2. **敘述式風格**：請使用「### 標題」搭配「深入的敘述段落」。每一點建議都必須有完整的邏輯說明與數據洞察感。
    3. **視覺間距**：段落與段落之間請保持空行。
    4. **固定結尾**：回覆最後必須詢問：「你想主推什麼樣的商品？它有什麼特色呢？歡迎提供給我，讓我幫您產生 AI 中英文版的圖片咒語」。
    """
    
    # 構造對話歷史，維持 User -> Model 順序
    history_payload = []
    for msg in st.session_state.chat_history[-10:]: # 取最近 10 筆
        history_payload.append({"role": msg["role"], "parts": [{"text": msg["content"]}]})
    
    # 加入當前訊息與附件數據
    current_input = user_query
    if data_attachment:
        current_input = f"[參考數據資料]:\n{data_attachment}\n\n[需求]:\n{user_query}"
        
    history_payload.append({"role": "user", "parts": [{"text": current_input}]})

    payload = {
        "systemInstruction": {"parts": [{"text": system_prompt}]},
        "contents": history_payload,
        "safetySettings": [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"}
        ]
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=30)
        data = response.json()
        if 'error' in data:
            return f"❌ API 報錯：{data['error']['message']}"
        return data['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"⚠️ 系統連線異常：{str(e)}"

# --- 6. 介面佈局 ---
st.title("🌿 AI Growth Hub")

# 使用標籤頁區分功能，解決標頭重複問題
tab1, tab2, tab3 = st.tabs(["🧬 品牌基因設定", "💬 策略中心", "📊 數據連線"])

# --- Tab 1: 品牌設定 ---
with tab1:
    st.markdown("### STEP 1. 建立品牌大腦")
    st.caption("設定一次，確保所有企劃建議皆符合品牌調性與市場定位。")
    
    # 提供複製提示詞的代碼塊
    copy_text = "我現在要將我的品牌資訊導入 AI Growth Hub 策略系統。請幫我分析品牌名稱+品牌官網網址+品牌社群網址，並按格式整理：品牌名稱、核心價值與語氣、目標客群特徵、三大核心產品及其賣點、主要競爭對手與差異化、目前行銷重點。請以純文字格式呈現。"
    st.code(copy_text, language=None)
    st.caption("☝️ 點擊代碼框右上角按鈕即可複製分析指令")

    brand_input = st.text_area(
        "請貼入 AI 分析後的品牌基因內容：",
        value=st.session_state.brand_bio,
        placeholder="品牌名稱、核心價值、主力產品賣點...",
        height=300
    )
    
    if st.button("儲存並更新品牌基因", type="primary", use_container_width=True):
        st.session_state.brand_bio = brand_input
        st.success("✅ 品牌基因已同步！AI 顧問現在已完全了解您的品牌。")

# --- Tab 2: 策略中心 ---
with tab2:
    # 顯示對話歷史
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 靈感引擎按鈕區 (隨機組合邏輯)
    st.write("---")
    st.write("💡 **靈感引擎 3.0** (每次點擊組合都不同)")
    c1, c2, c3 = st.columns(3)

    def run_inspiration(platform):
        # 靈感引擎隨機資料庫
        weather = f"{random.choice(['微涼清爽的', '和煦溫暖的', '陽光普照的', '細雨靜謐的'])} {random.randint(16, 28)}度"
        festival = random.choice(["情人節浪漫商機", "週末質感提案", "春季美學生活", "開工回饋企劃", "母親節溫暖話題"])
        trend = random.choice(["AI 科技美學", "極簡靜奢風 (Quiet Luxury)", "永續生活話題", "高效數位賦能", "情緒價值共鳴"])
        
        prompt = f"【靈感引擎 3.0 智慧啟動】交叉計算結果：環境感({weather})、當前熱點({festival})、核心趨勢({trend})。請以此為核心為我產出一份具備實質深度的 {platform} 結構化企劃建議。內容請用流暢敘述呈現，嚴禁表格。"
        
        with st.chat_message("user"): st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("AI 顧問正在進行深度運算與撰寫..."):
                reply = call_gemini(prompt)
                st.markdown(reply)
                st.session_state.chat_history.append({"role": "user", "content": prompt})
                st.session_state.chat_history.append({"role": "model", "content": reply})

    if c1.button("📱 FB / IG", use_container_width=True): run_inspiration("FB / IG")
    if c2.button("💬 LINE 群組", use_container_width=True): run_inspiration("LINE 群組")
    if c3.button("🧵 Threads", use_container_width=True): run_inspiration("Threads")

    # 文字輸入框
    if user_text := st.chat_input("輸入您的行銷需求..."):
        st.session_state.chat_history.append({"role": "user", "content": user_text})
        with st.chat_message("user"):
            st.markdown(user_text)
        
        with st.chat_message("assistant"):
            with st.spinner("顧問撰寫中..."):
                reply = call_gemini(user_text)
                st.markdown(reply)
                st.session_state.chat_history.append({"role": "model", "content": reply})

    if st.button("🗑️ 清空對話歷史", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

# --- Tab 3: 數據連線 ---
with tab3:
    st.markdown("### STEP 3. 銷售報表數據分析")
    uploaded_file = st.file_uploader("上傳 CSV 或 Excel 銷售報表", type=["csv", "xlsx"])
    
    if uploaded_file:
        st.success(f"檔案 {uploaded_file.name} 已載入！")
        if st.button("開始進行數據透視分析", type="primary", use_container_width=True):
            try:
                df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('csv') else pd.read_excel(uploaded_file)
                # 傳送摘要數據給 AI
                data_summary = df.head(100).to_string()
                
                with st.spinner("正在解析數據中的增長機會..."):
                    reply = call_gemini("請分析此份數據，指出增長亮點與潛在風險，並提供具體的行動建議。請使用詳盡敘述，絕對嚴禁表格。", data_attachment=data_summary)
                    st.session_state.chat_history.append({"role": "user", "content": "分析銷售數據報表"})
                    st.session_state.chat_history.append({"role": "model", "content": reply})
                    st.info("分析已完成！請前往「策略中心」查看詳細報告。")
            except Exception as e:
                st.error(f"數據讀取失敗: {str(e)}")
