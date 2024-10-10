import streamlit as st
if "df_spotify" not in st.session_state:
    st.warning("Ih! deu pau")
else:
    st.session_state["df_spotify"]