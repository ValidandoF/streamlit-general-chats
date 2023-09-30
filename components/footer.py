from pathlib import Path

import streamlit as st

from .constants import BUG_REPORT_URL, REPO_URL
#from .helpers import render_svg


def footer() -> None:
    st.divider()
    st.divider()
    st.markdown(f"""
        ### :page_with_curl: Validando.com @2023
    """, unsafe_allow_html=True)
    st.divider()
    st.markdown(f"project [repo on github]({REPO_URL}) waiting for your :star: | [report]({BUG_REPORT_URL}) a bug")