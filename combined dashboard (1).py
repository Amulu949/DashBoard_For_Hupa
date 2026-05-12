import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# =========================
# CUSTOM UI THEME (CSS)
# =========================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(180deg, #F8FBFF 0%, #EEF6FF 100%);
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    width: 320px;
    min-width: 320px;
    max-width: 320px;
    background: linear-gradient(180deg,#0B1F3A 0%, #102B50 100%);
    padding-top: 10px;
}

/* SIDEBAR LABEL */
[data-testid="stSidebar"] label {
    color: white !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

/* SELECTBOX CONTAINER */
[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
    background-color: #102B4E !important;
    border: 1px solid #1F5C99 !important;
    border-radius: 10px !important;
    color: white !important;
    height: 48px !important;
    padding-left: 10px !important;
}

/* SELECTED TEXT */
[data-testid="stSidebar"] .stSelectbox span {
    color: white !important;
    font-size: 15px !important;
}

/* DROPDOWN MENU */
[data-baseweb="popover"] {
    background-color: #102B4E !important;
    border-radius: 10px !important;
}

/* DROPDOWN OPTIONS */
[data-baseweb="menu"] div {
    background-color: #102B4E !important;
    color: white !important;
    padding: 10px !important;
}

[data-baseweb="menu"] div:hover {
    background-color: #1F5C99 !important;
}

</style>
""", unsafe_allow_html=True)
