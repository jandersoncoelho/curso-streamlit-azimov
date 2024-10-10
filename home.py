import streamlit as st
import pandas as pd
import time

st.set_page_config(
    layout="wide",
    page_title="Análise de Dados do Spotify",
)
st.header("Músicas do Spotify")


@st.cache_data
def load_data() -> object:
    df_loaded = pd.read_csv("spotfy.csv")
    time.sleep(5)
    return df_loaded


df = load_data()
st.session_state["df_spotify"] = df
df.set_index("Track", inplace=True)

artists = df["Artist"].value_counts().index
artist = st.sidebar.selectbox("Escolha seu artista:", artists)
df_filtered = df[df["Artist"] == artist]

albums = df_filtered["Album"].value_counts().index
album = st.selectbox("Selecione o álbum do artista:", albums)
df_filtered_album = df[df["Album"] == album]

col1, col2 = st.columns([0.7, 0.4])

with col1:
    st.write("#### Stream")
    st.bar_chart(df_filtered_album["Stream"])

with col2:
    st.write("#### Danceability")
    st.line_chart(df_filtered_album["Danceability"])

st.subheader(f"Músicas de {artist}")
df_filtered

st.subheader(f"Músicas do Álbum {album}")
df_filtered_album
