import streamlit as st

st.title("Welcome to my Advent of Code 2024 web app")

st.sidebar.title("Menu")
option = st.sidebar.selectbox("", ["Homepage",
                              "Day 1: Historian Hysteria",
                                   ])

if option == "Homepage":
    # Description

    st.write('-----------------------------------------------')
    st.write(
        "This web app aims to share my python code I used to solve AoC puzzles")
    st.write("Ultimately, you can drop your inputs and run my code on it to check wether your code is correct or not ;)")
    st.write('-----------------------------------------------')
# else:
#     script_name = st.text_input(
#         "Entrez le nom du script à exécuter", "example.py")
#     if st.button("Exécuter"):
#         with st.spinner("Exécution en cours..."):
#             try:
#                 exec(open(script_name).read())
#                 st.success("Script exécuté avec succès.")
#             except Exception as e:
#                 st.error(f"Erreur : {e}")
# elif option == "Analyser des données":
#     uploaded_file = st.file_uploader("Chargez un fichier CSV")
#     if uploaded_file is not None:
#         data = pd.read_csv(uploaded_file)
#         st.write(data.head())
#         st.write("Histogramme des colonnes numériques :")
#         data.hist(bins=20)
#         st.pyplot(plt)
