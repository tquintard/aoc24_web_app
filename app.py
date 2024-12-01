import streamlit as st

st.title("Welcome to my Advent of Code 2024 web app")

st.sidebar.title("Select a day")
option = st.sidebar.selectbox("", ["Homepage",
                              "Day 1: Historian Hysteria",
                                   ])

if option == "Homepage":
    # Description
    st.write(
        "This web app aims to share my python code I used to solve AoC puzzles")
    st.write("Ultimately, you can drop your inputs and run my code on it to check wether your code is correct or not ;)")
else:
    st.header(option)
    # Uploader un fichier
    uploaded_file = st.file_uploader(
        f"Upload your input file for {option}", type=["txt", "csv"])
