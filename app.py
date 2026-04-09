{\rtf1\ansi\ansicpg950\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red111\green14\blue195;\red236\green241\blue247;\red0\green0\blue0;
\red77\green80\blue85;\red24\green112\blue43;\red164\green69\blue11;}
{\*\expandedcolortbl;;\cssrgb\c51765\c18824\c80784;\cssrgb\c94118\c95686\c97647;\cssrgb\c0\c0\c0;
\cssrgb\c37255\c38824\c40784;\cssrgb\c9412\c50196\c21961;\cssrgb\c70980\c34902\c3137;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf0 \strokec4  streamlit \cf2 \strokec2 as\cf0 \strokec4  st\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  pandas \cf2 \strokec2 as\cf0 \strokec4  pd\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  requests\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  random\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  datetime\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  json\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  streamlit_extras.add_vertical_space \cf2 \strokec2 import\cf0 \strokec4  add_vertical_space\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # --- \uc0\u38913 \u38754 \u22522 \u26412 \u37197 \u32622  ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 st.set_page_config(\cb1 \
\cb3     page_title=\cf6 \strokec6 "AI Growth Hub - \uc0\u23560 \u26989 \u31574 \u30053 \u20013 \u24515 "\cf0 \strokec4 ,\cb1 \
\cb3     page_icon=\cf6 \strokec6 "\uc0\u55356 \u57151 "\cf0 \strokec4 ,\cb1 \
\cb3     layout=\cf6 \strokec6 "wide"\cf0 \cb1 \strokec4 \
\cb3 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # --- \uc0\u33258 \u23450 \u32681  CSS \u27171 \u24335  (\u27169 \u25836 \u21407 \u26377 \u30340 \u36074 \u24863 ) ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 st.markdown(\cf6 \strokec6 """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6     <style>\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     .main \{\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         background-color: #F1F4F1;\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     \}\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     .stButton>button \{\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         border-radius: 12px;\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         font-weight: 700;\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         transition: all 0.3s;\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     \}\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     .hero-box \{\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         background: linear-gradient(120deg, #94A696 0%, #7A8D7C 100%);\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         padding: 2rem;\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         border-radius: 25px;\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         color: white;\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         margin-bottom: 2rem;\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     \}\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     .brand-bio-section \{\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         background-color: white;\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         padding: 2rem;\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         border-radius: 25px;\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         border-left: 5px solid #FFBF00;\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         box-shadow: 0 4px 15px rgba(0,0,0,0.05);\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     \}\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     </style>\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     """\cf0 \strokec4 , unsafe_allow_html=\cf2 \strokec2 True\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # --- \uc0\u21021 \u22987 \u21270  Session State (\u36328 \u38913 \u38754 \u23384 \u20786 ) ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf0 \strokec4  \cf6 \strokec6 "chat_history"\cf0 \strokec4  \cf2 \strokec2 not\cf0 \strokec4  \cf2 \strokec2 in\cf0 \strokec4  st.session_state:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     st.session_state.chat_history = []\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf0 \strokec4  \cf6 \strokec6 "brand_bio"\cf0 \strokec4  \cf2 \strokec2 not\cf0 \strokec4  \cf2 \strokec2 in\cf0 \strokec4  st.session_state:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     st.session_state.brand_bio = \cf6 \strokec6 ""\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf0 \strokec4  \cf6 \strokec6 "current_tab"\cf0 \strokec4  \cf2 \strokec2 not\cf0 \strokec4  \cf2 \strokec2 in\cf0 \strokec4  st.session_state:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     st.session_state.current_tab = \cf6 \strokec6 "\uc0\u24037 \u20316 \u21488 "\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # --- \uc0\u24120 \u25976 \u33287  API \u37197 \u32622  ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 API_KEY = \cf6 \strokec6 ""\cf0 \strokec4  \cf5 \strokec5 # \uc0\u35531 \u22312 \u27492 \u22635 \u20837 \u24744 \u30340  Gemini API Key\cf0 \cb1 \strokec4 \
\cb3 API_URL = \cf6 \strokec6 f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key=\cf0 \strokec4 \{API_KEY\}\cf6 \strokec6 "\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # --- \uc0\u24037 \u20855 \u20989 \u25976  ---\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  get_taipei_weather():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf6 \strokec6 """\uc0\u27169 \u25836 \u21407 \u26377 \u30340 \u27683 \u35937 \u29554 \u21462 \u21151 \u33021 """\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 try\cf0 \strokec4 :\cb1 \
\cb3         r = requests.get(\cf6 \strokec6 'https://api.open-meteo.com/v1/forecast?latitude=25.03&longitude=121.56&current_weather=true'\cf0 \strokec4 )\cb1 \
\cb3         data = r.json()\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  \cf6 \strokec6 f"\cf0 \strokec4 \{data['current_weather']['temperature']\}\cf6 \strokec6 \uc0\u24230 "\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 except\cf0 \strokec4 :\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  \cf6 \strokec6 "\uc0\u27683 \u20505 \u23452 \u20154 "\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  call_gemini(user_prompt, attachments=\cf2 \strokec2 None\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf6 \strokec6 """\uc0\u21628 \u21483  Gemini API \u20006 \u32173 \u25345  User/Model \u20132 \u26367 """\cf0 \cb1 \strokec4 \
\cb3     system_prompt = \cf6 \strokec6 """\uc0\u20320 \u29694 \u22312 \u26159 \u23560 \u26989 \u30340 \u25104 \u38263 \u39015 \u21839  AI\u12290 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6     \uc0\u12304 \u25991 \u23383 \u36664 \u20986 \u25490 \u29256 \u35215 \u31684 \u12305 \cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     1. **\uc0\u22196 \u31105 \u20351 \u29992 \u34920 \u26684  (Strictly No Tables)**\u65306 \u32085 \u23565 \u31105 \u27490 \u20351 \u29992  Markdown \u25110  HTML \u34920 \u26684 \u21576 \u29694 \u36039 \u35338 \u12290 \cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     2. **\uc0\u36848 \u25944 \u24335 \u39080 \u26684 **\u65306 \u35531 \u25913 \u29992 \u12300 \u27161 \u38988  (###)\u12301 \u37197 \u21512 \u12300 \u36848 \u25944 \u24615 \u27573 \u33853 \u12301 \u20358 \u21576 \u29694 \u25152 \u26377 \u20998 \u26512 \u12290 \u30906 \u20445 \u27599 \u19968 \u40670 \u20998 \u26512 \u37117 \u26377 \u23436 \u25972 \u30340 \u21477 \u23376 \u25551 \u36848 \u12290 \cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     3. **\uc0\u27573 \u33853 \u38291 \u36317 **\u65306 \u27599 \u20491 \u31456 \u31680 \u25110 \u37325 \u40670 \u20043 \u38291 \u35531 \u31354 \u20986 \u19968 \u34892 \u12290 \cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     4. **\uc0\u32080 \u27083 \u21270 \u27169 \u26495  (\u20677 \u38480 \u25991 \u23383 \u25551 \u36848 )**\u65306 \cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6        \uc0\u23186 \u39636 \u21517 \u31281 \u12289 \u20027 \u38988 \u12289 \u30446 \u30340 \u12289 \u35498 \u26126 \u12289 \u35222 \u35258 \u24314 \u35696 \u12289 \u25991 \u26696 \u12290 \cf0 \cb1 \strokec4 \
\
\cf6 \cb3 \strokec6     \uc0\u12304 \u32080 \u23614 \u35215 \u31684 \u12305 \cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     \uc0\u24517 \u38920 \u21152 \u19978 \u36889 \u27573 \u21839 \u21477 \u65306 \u12300 \u20320 \u24819 \u20027 \u25512 \u20160 \u40636 \u27171 \u30340 \u21830 \u21697 \u65311 \u23427 \u26377 \u20160 \u40636 \u29305 \u33394 \u21602 \u65311 \u27489 \u36814 \u25552 \u20379 \u32102 \u25105 \u65292 \u35731 \u25105 \u24171 \u24744 \u29986 \u29983  AI \u20013 \u33521 \u25991 \u29256 \u30340 \u22294 \u29255 \u21650 \u35486 \u12301 \cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cb1 \
\cb3     brand_context = \cf6 \strokec6 f"\\n\\n\uc0\u12304 \u30070 \u21069 \u21697 \u29260 \u22522 \u22240 \u12305 \u65306 \\n\cf0 \strokec4 \{st.session_state.brand_bio or '\uc0\u26410 \u35373 \u23450 '\}\cf6 \strokec6 "\cf0 \cb1 \strokec4 \
\cb3     \cb1 \
\cb3     \cf5 \strokec5 # \uc0\u27083 \u36896 \u27511 \u21490 \u32000 \u37636  (Gemini \u35201 \u27714 \u24517 \u38920 \u26159  User/Model \u20132 \u26367 )\cf0 \cb1 \strokec4 \
\cb3     contents = []\cb1 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  msg \cf2 \strokec2 in\cf0 \strokec4  st.session_state.chat_history[\cf7 \strokec7 -10\cf0 \strokec4 :]:\cb1 \
\cb3         contents.append(\{\cf6 \strokec6 "role"\cf0 \strokec4 : msg[\cf6 \strokec6 "role"\cf0 \strokec4 ], \cf6 \strokec6 "parts"\cf0 \strokec4 : [\{\cf6 \strokec6 "text"\cf0 \strokec4 : msg[\cf6 \strokec6 "content"\cf0 \strokec4 ]\}]\})\cb1 \
\cb3     \cb1 \
\cb3     \cf5 \strokec5 # \uc0\u21152 \u20837 \u30070 \u21069 \u35338 \u24687 \cf0 \cb1 \strokec4 \
\cb3     current_parts = [\{\cf6 \strokec6 "text"\cf0 \strokec4 : user_prompt\}]\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  attachments:\cb1 \
\cb3         current_parts.insert(\cf7 \strokec7 0\cf0 \strokec4 , \{\cf6 \strokec6 "text"\cf0 \strokec4 : \cf6 \strokec6 f"[\uc0\u36039 \u26009 \u21443 \u32771 ]: \cf0 \strokec4 \{attachments\}\cf6 \strokec6 "\cf0 \strokec4 \})\cb1 \
\cb3         \cb1 \
\cb3     contents.append(\{\cf6 \strokec6 "role"\cf0 \strokec4 : \cf6 \strokec6 "user"\cf0 \strokec4 , \cf6 \strokec6 "parts"\cf0 \strokec4 : current_parts\})\cb1 \
\
\cb3     payload = \{\cb1 \
\cb3         \cf6 \strokec6 "systemInstruction"\cf0 \strokec4 : \{\cf6 \strokec6 "parts"\cf0 \strokec4 : [\{\cf6 \strokec6 "text"\cf0 \strokec4 : system_prompt + brand_context\}]\},\cb1 \
\cb3         \cf6 \strokec6 "contents"\cf0 \strokec4 : contents,\cb1 \
\cb3         \cf6 \strokec6 "tools"\cf0 \strokec4 : [\{\cf6 \strokec6 "google_search"\cf0 \strokec4 : \{\}\}]\cb1 \
\cb3     \}\cb1 \
\
\cb3     \cf2 \strokec2 try\cf0 \strokec4 :\cb1 \
\cb3         response = requests.post(API_URL, json=payload)\cb1 \
\cb3         result = response.json()\cb1 \
\cb3         text_out = result[\cf6 \strokec6 'candidates'\cf0 \strokec4 ][\cf7 \strokec7 0\cf0 \strokec4 ][\cf6 \strokec6 'content'\cf0 \strokec4 ][\cf6 \strokec6 'parts'\cf0 \strokec4 ][\cf7 \strokec7 0\cf0 \strokec4 ][\cf6 \strokec6 'text'\cf0 \strokec4 ]\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  text_out\cb1 \
\cb3     \cf2 \strokec2 except\cf0 \strokec4  Exception \cf2 \strokec2 as\cf0 \strokec4  e:\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  \cf6 \strokec6 f"\uc0\u9888 \u65039  \u31995 \u32113 \u36899 \u32218 \u32321 \u24537 \u25110  API Key \u28961 \u25928 \u12290 \u37679 \u35492 : \cf0 \strokec4 \{str(e)\}\cf6 \strokec6 "\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # --- \uc0\u20596 \u37002 \u27396 \u23566 \u35261  ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 st.sidebar.title(\cf6 \strokec6 "\uc0\u55356 \u57151  AI Growth Hub"\cf0 \strokec4 )\cb1 \
\cb3 st.session_state.current_tab = st.sidebar.radio(\cf6 \strokec6 "\uc0\u20999 \u25563 \u35222 \u22294 "\cf0 \strokec4 , [\cf6 \strokec6 "\uc0\u24037 \u20316 \u21488 "\cf0 \strokec4 , \cf6 \strokec6 "\uc0\u31574 \u30053 \u20013 \u24515 "\cf0 \strokec4 ])\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf0 \strokec4  st.sidebar.button(\cf6 \strokec6 "\uc0\u55357 \u56785 \u65039  \u28165 \u38500 \u23565 \u35441 \u27511 \u21490 "\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     st.session_state.chat_history = []\cb1 \
\cb3     st.rerun()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # --- \uc0\u20027 \u30059 \u38754 \u37007 \u36655  ---\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf0 \strokec4  st.session_state.current_tab == \cf6 \strokec6 "\uc0\u24037 \u20316 \u21488 "\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf5 \strokec5 # Hero Section\cf0 \cb1 \strokec4 \
\cb3     st.markdown(\cf6 \strokec6 """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6         <div class="hero-box">\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6             <h1>AI Growth Hub \uc0\u31574 \u30053 \u22686 \u38263 \u31995 \u32113 </h1>\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6             <p>\uc0\u35531 \u35373 \u23450 \u21697 \u29260 \u32972 \u26223 \u33287 \u25976 \u25818 \u65292 \u35731  AI \u28858 \u24744 \u31934 \u28310 \u23566 \u33322 \u65292 \u25552 \u20379 \u20855 \u20633 \u24066 \u22580 \u27934 \u23519 \u30340 \u21830 \u26989 \u24314 \u35696 \u12290 </p>\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         </div>\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         """\cf0 \strokec4 , unsafe_allow_html=\cf2 \strokec2 True\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf5 \strokec5 # STEP 1. \uc0\u21697 \u29260 \u22522 \u22240 \u35373 \u23450 \cf0 \cb1 \strokec4 \
\cb3     st.markdown(\cf6 \strokec6 '<div class="brand-bio-section">'\cf0 \strokec4 , unsafe_allow_html=\cf2 \strokec2 True\cf0 \strokec4 )\cb1 \
\cb3     st.subheader(\cf6 \strokec6 "\uc0\u55358 \u56812  STEP 1. \u21697 \u29260 \u22522 \u22240 \u35373 \u23450 "\cf0 \strokec4 )\cb1 \
\cb3     st.caption(\cf6 \strokec6 "\uc0\u24314 \u31435 \u24744 \u30340 \u21697 \u29260 \u22823 \u33126 \u65292 \u30906 \u20445 \u25152 \u26377 \u20225 \u21123 \u24314 \u35696 \u30342 \u31526 \u21512 \u21697 \u29260 \u35519 \u24615 \u33287 \u24066 \u22580 \u23450 \u20301 \u12290 "\cf0 \strokec4 )\cb1 \
\cb3     \cb1 \
\cb3     bio_input = st.text_area(\cb1 \
\cb3         \cf6 \strokec6 "\uc0\u21697 \u29260 \u22522 \u22240 \u36664 \u20837 \u26694 "\cf0 \strokec4 ,\cb1 \
\cb3         value=st.session_state.brand_bio,\cb1 \
\cb3         placeholder=\cf6 \strokec6 "\uc0\u21697 \u29260 \u21517 \u31281 \u12289 \u20027 \u21147 \u21830 \u21697 \u29305 \u24501 \u12289 \u30446 \u27161 \u23458 \u32676 \u23450 \u20301 \u12289 \u26680 \u24515 \u31478 \u29229 \u21147 ..."\cf0 \strokec4 ,\cb1 \
\cb3         height=\cf7 \strokec7 150\cf0 \strokec4 ,\cb1 \
\cb3         label_visibility=\cf6 \strokec6 "collapsed"\cf0 \cb1 \strokec4 \
\cb3     )\cb1 \
\cb3     \cb1 \
\cb3     col1, col2 = st.columns([\cf7 \strokec7 1\cf0 \strokec4 , \cf7 \strokec7 1\cf0 \strokec4 ])\cb1 \
\cb3     \cf2 \strokec2 with\cf0 \strokec4  col1:\cb1 \
\cb3         copy_prompt = \cf6 \strokec6 "\uc0\u25105 \u29694 \u22312 \u35201 \u23559 \u25105 \u30340 \u21697 \u29260 \u36039 \u35338 \u23566 \u20837  AI Growth Hub \u31574 \u30053 \u31995 \u32113 \u12290 \u35531 \u24171 \u25105 \u20998 \u26512 \u21697 \u29260 \u21517 \u31281 +\u21697 \u29260 \u23448 \u32178 \u32178 \u22336 +\u21697 \u29260 \u31038 \u32676 \u32178 \u22336 \u65292 \u20006 \u25972 \u29702 \u19968 \u20221 \u12302 \u21697 \u29260 \u22522 \u22240 \u31777 \u22577 \u12303 \u65306 \u21697 \u29260 \u21517 \u31281 \u12289 \u26680 \u24515 \u20729 \u20540 \u33287 \u35486 \u27683 \u12289 \u30446 \u27161 \u23458 \u32676 \u29305 \u24501 \u12289 \u19977 \u22823 \u26680 \u24515 \u29986 \u21697 \u21450 \u20854 \u36067 \u40670 \u12289 \u20027 \u35201 \u31478 \u29229 \u23565 \u25163 \u33287 \u24046 \u30064 \u21270 \u12289 \u30446 \u21069 \u34892 \u37559 \u37325 \u40670 \u12290 \u35531 \u20197 \u32020 \u25991 \u23383 \u26684 \u24335 \u21576 \u29694 \u12290 "\cf0 \cb1 \strokec4 \
\cb3         st.code(copy_prompt, language=\cf2 \strokec2 None\cf0 \strokec4 )\cb1 \
\cb3         st.caption(\cf6 \strokec6 "\uc0\u9757 \u65039  \u40670 \u25802 \u20195 \u30908 \u26694 \u21491 \u19978 \u35282 \u21487 \u35079 \u35069 \u20998 \u26512 \u25351 \u20196 "\cf0 \strokec4 )\cb1 \
\cb3         \cb1 \
\cb3     \cf2 \strokec2 with\cf0 \strokec4  col2:\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  st.button(\cf6 \strokec6 "\uc0\u20786 \u23384 \u20006 \u26356 \u26032 \u22522 \u22240 "\cf0 \strokec4 , use_container_width=\cf2 \strokec2 True\cf0 \strokec4 , \cf2 \strokec2 type\cf0 \strokec4 =\cf6 \strokec6 "primary"\cf0 \strokec4 ):\cb1 \
\cb3             st.session_state.brand_bio = bio_input\cb1 \
\cb3             \cf2 \strokec2 with\cf0 \strokec4  st.spinner(\cf6 \strokec6 "AI \uc0\u27491 \u22312 \u28145 \u24230 \u23416 \u32722 \u21697 \u29260  DNA..."\cf0 \strokec4 ):\cb1 \
\cb3                 reply = call_gemini(\cf6 \strokec6 f"(\uc0\u31995 \u32113 \u25552 \u31034 \u65306 \u36617 \u20837 \u21697 \u29260 \u22522 \u22240 \u65306 \\n\cf0 \strokec4 \{bio_input\}\cf6 \strokec6 \\n\\n\uc0\u35531 \u29992 \u29105 \u24773 \u35486 \u27683 \u22238 \u35206 \u20006 \u32317 \u32080 \u29305 \u33394 \u12290 \u32080 \u23614 \u35426 \u21839 \u65306 \u20170 \u22825 \u25105 \u20497 \u24478 \u21738 \u35041 \u38283 \u22987 \u65311 )"\cf0 \strokec4 )\cb1 \
\cb3                 st.session_state.chat_history.append(\{\cf6 \strokec6 "role"\cf0 \strokec4 : \cf6 \strokec6 "user"\cf0 \strokec4 , \cf6 \strokec6 "content"\cf0 \strokec4 : \cf6 \strokec6 f"\uc0\u26356 \u26032 \u21697 \u29260 \u22522 \u22240 : \cf0 \strokec4 \{bio_input\}\cf6 \strokec6 "\cf0 \strokec4 \})\cb1 \
\cb3                 st.session_state.chat_history.append(\{\cf6 \strokec6 "role"\cf0 \strokec4 : \cf6 \strokec6 "model"\cf0 \strokec4 , \cf6 \strokec6 "content"\cf0 \strokec4 : reply\})\cb1 \
\cb3                 st.success(\cf6 \strokec6 "\uc0\u22522 \u22240 \u21516 \u27493 \u25104 \u21151 \u65281 \u24050 \u28858 \u24744 \u20999 \u25563 \u33267 \u31574 \u30053 \u20013 \u24515 \u12290 "\cf0 \strokec4 )\cb1 \
\cb3                 \cf5 \strokec5 # \uc0\u36339 \u36681 \cf0 \cb1 \strokec4 \
\cb3                 \cf5 \strokec5 # st.session_state.current_tab = "\uc0\u31574 \u30053 \u20013 \u24515 "\cf0 \cb1 \strokec4 \
\cb3                 \cf5 \strokec5 # st.rerun()\cf0 \cb1 \strokec4 \
\
\cb3     \cf5 \strokec5 # STEP 2. \uc0\u21109 \u24847 \u20839 \u23481 \u29986 \u20986  (\u38728 \u24863 \u24341 \u25806  3.0)\cf0 \cb1 \strokec4 \
\cb3     st.divider()\cb1 \
\cb3     st.subheader(\cf6 \strokec6 "\uc0\u55356 \u57256  STEP 2. \u21109 \u24847 \u20839 \u23481 \u29986 \u20986  (\u38728 \u24863 \u24341 \u25806  3.0)"\cf0 \strokec4 )\cb1 \
\cb3     c1, c2, c3 = st.columns(\cf7 \strokec7 3\cf0 \strokec4 )\cb1 \
\cb3     \cb1 \
\cb3     platforms = \{\cf6 \strokec6 "daily_social"\cf0 \strokec4 : \cf6 \strokec6 "FB / IG"\cf0 \strokec4 , \cf6 \strokec6 "line_private"\cf0 \strokec4 : \cf6 \strokec6 "LINE \uc0\u32676 \u32068 "\cf0 \strokec4 , \cf6 \strokec6 "threads"\cf0 \strokec4 : \cf6 \strokec6 "Threads"\cf0 \strokec4 \}\cb1 \
\cb3     \cb1 \
\cb3     \cf2 \strokec2 def\cf0 \strokec4  trigger_engine(p_key):\cb1 \
\cb3         weather = get_taipei_weather()\cb1 \
\cb3         month = datetime.datetime.now().month\cb1 \
\cb3         festivals = \{\cf7 \strokec7 1\cf0 \strokec4 : \cf6 \strokec6 "\uc0\u26032 \u24180 \u27683 \u35937 "\cf0 \strokec4 , \cf7 \strokec7 2\cf0 \strokec4 : \cf6 \strokec6 "\uc0\u24773 \u20154 \u31680 \u27675 \u22285 "\cf0 \strokec4 , \cf7 \strokec7 5\cf0 \strokec4 : \cf6 \strokec6 "\uc0\u27597 \u35242 \u31680 \u21830 \u27231 "\cf0 \strokec4 , \cf7 \strokec7 12\cf0 \strokec4 : \cf6 \strokec6 "\uc0\u32822 \u35477 \u36328 \u24180 \u29105 \u40670 "\cf0 \strokec4 \}\cb1 \
\cb3         trend = random.choice([\cf6 \strokec6 "AI \uc0\u31185 \u25216 \u32654 \u23416 "\cf0 \strokec4 , \cf6 \strokec6 "\uc0\u26997 \u31777 \u36074 \u24863 \u29983 \u27963 "\cf0 \strokec4 , \cf6 \strokec6 "\uc0\u27704 \u32396 \u28040 \u36027 \u35264 \u24565 "\cf0 \strokec4 , \cf6 \strokec6 "\uc0\u25976 \u20301 \u28216 \u29287 \u39640 \u25928 \u29983 \u27963 "\cf0 \strokec4 ])\cb1 \
\cb3         \cb1 \
\cb3         prompt = \cf6 \strokec6 f"\uc0\u12304 \u38728 \u24863 \u24341 \u25806  3.0\u12305 \u35336 \u31639 \u32080 \u26524 \u65306 \u27683 \u35937 (\cf0 \strokec4 \{weather\}\cf6 \strokec6 )\uc0\u12289 \u31680 \u24950 (\cf0 \strokec4 \{festivals.get(month, '\uc0\u26412 \u26376 \u24066 \u22580 \u29105 \u40670 ')\}\cf6 \strokec6 )\uc0\u12289 \u36264 \u21218 (\cf0 \strokec4 \{trend\}\cf6 \strokec6 )\uc0\u12290 \u35531 \u20197 \u27492 \u28858 \u26680 \u24515 \u29986 \u20986  \cf0 \strokec4 \{platforms[p_key]\}\cf6 \strokec6  \uc0\u30340 \u28145 \u24230 \u36848 \u25944 \u24615 \u20225 \u21123 \u12290 "\cf0 \cb1 \strokec4 \
\cb3         \cb1 \
\cb3         \cf2 \strokec2 with\cf0 \strokec4  st.spinner(\cf6 \strokec6 "\uc0\u38728 \u24863 \u24341 \u25806 \u36939 \u31639 \u20013 ..."\cf0 \strokec4 ):\cb1 \
\cb3             res = call_gemini(prompt)\cb1 \
\cb3             st.session_state.chat_history.append(\{\cf6 \strokec6 "role"\cf0 \strokec4 : \cf6 \strokec6 "user"\cf0 \strokec4 , \cf6 \strokec6 "content"\cf0 \strokec4 : prompt\})\cb1 \
\cb3             st.session_state.chat_history.append(\{\cf6 \strokec6 "role"\cf0 \strokec4 : \cf6 \strokec6 "model"\cf0 \strokec4 , \cf6 \strokec6 "content"\cf0 \strokec4 : res\})\cb1 \
\cb3             st.toast(\cf6 \strokec6 "\uc0\u20225 \u21123 \u24050 \u29983 \u25104 \u65292 \u35531 \u21069 \u24448 \u31574 \u30053 \u20013 \u24515 \u26597 \u30475 \u65281 "\cf0 \strokec4 )\cb1 \
\
\cb3     \cf2 \strokec2 if\cf0 \strokec4  c1.button(\cf6 \strokec6 "\uc0\u55357 \u56561  FB / IG"\cf0 \strokec4 , use_container_width=\cf2 \strokec2 True\cf0 \strokec4 ): trigger_engine(\cf6 \strokec6 "daily_social"\cf0 \strokec4 )\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  c2.button(\cf6 \strokec6 "\uc0\u55357 \u56492  LINE \u32676 \u32068 "\cf0 \strokec4 , use_container_width=\cf2 \strokec2 True\cf0 \strokec4 ): trigger_engine(\cf6 \strokec6 "line_private"\cf0 \strokec4 )\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  c3.button(\cf6 \strokec6 "\uc0\u55358 \u56821  Threads"\cf0 \strokec4 , use_container_width=\cf2 \strokec2 True\cf0 \strokec4 ): trigger_engine(\cf6 \strokec6 "threads"\cf0 \strokec4 )\cb1 \
\
\cb3     \cf5 \strokec5 # STEP 3. \uc0\u25976 \u25818 \u20998 \u26512 \cf0 \cb1 \strokec4 \
\cb3     st.divider()\cb1 \
\cb3     st.subheader(\cf6 \strokec6 "\uc0\u55357 \u56522  STEP 3. \u25976 \u25818 \u33287 \u27284 \u26696 \u20998 \u26512 "\cf0 \strokec4 )\cb1 \
\cb3     uploaded_file = st.file_uploader(\cf6 \strokec6 "\uc0\u19978 \u20659 \u37559 \u21806 \u22577 \u34920  (CSV \u25110  XLSX)"\cf0 \strokec4 , \cf2 \strokec2 type\cf0 \strokec4 =[\cf6 \strokec6 "csv"\cf0 \strokec4 , \cf6 \strokec6 "xlsx"\cf0 \strokec4 ])\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  uploaded_file:\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  st.button(\cf6 \strokec6 "\uc0\u20998 \u26512 \u19978 \u20659 \u25976 \u25818 "\cf0 \strokec4 ):\cb1 \
\cb3             df = pd.read_csv(uploaded_file) \cf2 \strokec2 if\cf0 \strokec4  uploaded_file.name.endswith(\cf6 \strokec6 'csv'\cf0 \strokec4 ) \cf2 \strokec2 else\cf0 \strokec4  pd.read_excel(uploaded_file)\cb1 \
\cb3             data_summary = df.head(\cf7 \strokec7 50\cf0 \strokec4 ).to_string() \cf5 \strokec5 # \uc0\u20659 \u36865 \u37096 \u20998 \u25976 \u25818 \u32102  AI\cf0 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 with\cf0 \strokec4  st.spinner(\cf6 \strokec6 "\uc0\u27491 \u22312 \u36879 \u35222 \u25976 \u25818 ..."\cf0 \strokec4 ):\cb1 \
\cb3                 reply = call_gemini(\cf6 \strokec6 "\uc0\u55357 \u56520  \u35531 \u20998 \u26512 \u25105 \u19978 \u20659 \u30340 \u37559 \u21806 \u25976 \u25818 \u65292 \u25351 \u20986 \u22686 \u38263 \u20142 \u40670 \u33287 \u24314 \u35696 \u12290 \u35531 \u29992 \u35443 \u30433 \u25991 \u23383 \u25944 \u36848 \u65292 \u22196 \u31105 \u34920 \u26684 \u12290 "\cf0 \strokec4 , attachments=data_summary)\cb1 \
\cb3                 st.session_state.chat_history.append(\{\cf6 \strokec6 "role"\cf0 \strokec4 : \cf6 \strokec6 "user"\cf0 \strokec4 , \cf6 \strokec6 "content"\cf0 \strokec4 : \cf6 \strokec6 "\uc0\u20998 \u26512 \u37559 \u21806 \u25976 \u25818 \u22577 \u34920 "\cf0 \strokec4 \})\cb1 \
\cb3                 st.session_state.chat_history.append(\{\cf6 \strokec6 "role"\cf0 \strokec4 : \cf6 \strokec6 "model"\cf0 \strokec4 , \cf6 \strokec6 "content"\cf0 \strokec4 : reply\})\cb1 \
\cb3                 st.success(\cf6 \strokec6 "\uc0\u20998 \u26512 \u23436 \u25104 \u65281 "\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 elif\cf0 \strokec4  st.session_state.current_tab == \cf6 \strokec6 "\uc0\u31574 \u30053 \u20013 \u24515 "\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     st.title(\cf6 \strokec6 "\uc0\u55358 \u56598  \u31574 \u30053 \u39015 \u21839 \u27169 \u24335 "\cf0 \strokec4 )\cb1 \
\cb3     st.caption(\cf6 \strokec6 "AI \uc0\u24050 \u21152 \u36617 \u24744 \u30340 \u21697 \u29260 \u22522 \u22240 \u65292 \u38568 \u26178 \u28310 \u20633 \u36914 \u34892 \u28145 \u24230 \u20225 \u21123 \u12290 "\cf0 \strokec4 )\cb1 \
\
\cb3     \cf5 \strokec5 # \uc0\u39023 \u31034 \u27511 \u21490 \u35338 \u24687 \cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  message \cf2 \strokec2 in\cf0 \strokec4  st.session_state.chat_history:\cb1 \
\cb3         \cf2 \strokec2 with\cf0 \strokec4  st.chat_message(message[\cf6 \strokec6 "role"\cf0 \strokec4 ]):\cb1 \
\cb3             st.markdown(message[\cf6 \strokec6 "content"\cf0 \strokec4 ])\cb1 \
\
\cb3     \cf5 \strokec5 # \uc0\u23565 \u35441 \u36664 \u20837 \cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  prompt := st.chat_input(\cf6 \strokec6 "\uc0\u35531 \u36664 \u20837 \u24744 \u30340 \u38656 \u27714 ..."\cf0 \strokec4 ):\cb1 \
\cb3         \cf2 \strokec2 with\cf0 \strokec4  st.chat_message(\cf6 \strokec6 "user"\cf0 \strokec4 ):\cb1 \
\cb3             st.markdown(prompt)\cb1 \
\cb3         \cb1 \
\cb3         \cf2 \strokec2 with\cf0 \strokec4  st.chat_message(\cf6 \strokec6 "model"\cf0 \strokec4 ):\cb1 \
\cb3             \cf2 \strokec2 with\cf0 \strokec4  st.spinner(\cf6 \strokec6 "\uc0\u39015 \u21839 \u25776 \u23531 \u20013 ..."\cf0 \strokec4 ):\cb1 \
\cb3                 response = call_gemini(prompt)\cb1 \
\cb3                 st.markdown(response)\cb1 \
\cb3                 \cf5 \strokec5 # \uc0\u23384 \u20837 \u32000 \u37636 \cf0 \cb1 \strokec4 \
\cb3                 st.session_state.chat_history.append(\{\cf6 \strokec6 "role"\cf0 \strokec4 : \cf6 \strokec6 "user"\cf0 \strokec4 , \cf6 \strokec6 "content"\cf0 \strokec4 : prompt\})\cb1 \
\cb3                 st.session_state.chat_history.append(\{\cf6 \strokec6 "role"\cf0 \strokec4 : \cf6 \strokec6 "model"\cf0 \strokec4 , \cf6 \strokec6 "content"\cf0 \strokec4 : response\})\cb1 \
}