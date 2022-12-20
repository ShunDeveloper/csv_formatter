import streamlit as st
import pandas as pd
import re
import os

### set global variable

PAGE_PATH = "pages/"
PAGE_NAMES = []
tmp = os.listdir(PAGE_PATH) # get file name
assert 0 < len(tmp) # confirm
for i in range(len(tmp)):
    file_name = tmp[i]
    file_name = re.sub(r'[0-9]+_', '', file_name)
    file_name = re.sub(r'.py', '', file_name)
    PAGE_NAMES.append(file_name)
del tmp

### set config

st.set_page_config(
    page_title="CSV FORMATTER",
    page_icon="🗃️",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://twitter.com/ShunDeveloper',
        'Report a bug': "https://twitter.com/ShunDeveloper",
        'About': "csv fomatter make your csv file more cool!"
    }
)

### application

st.title("CSV FORMATTER")
st.write("csv fomatter make your csv file more cool!")
st.subheader("Menu")
for name in PAGE_NAMES:
    st.write('- ' + name)