import streamlit as st
import pandas as pd
import random
from PIL import Image
from datetime import datetime
import time

now = datetime.utcnow().strftime('%Y-%m-%d')

with st.sidebar:
    #image = Image.open('Cropped.png')
    #st.image(image, caption='BET223', width=100)
    st.sidebar.title("VOUS ÊTES PASSIONNÉ PAR LE SPORT ET PAR LE JEU ? AVEC BET223, FAITES DE VOTRE PASSION UN GAIN !")
    st.sidebar.write('\n')
    st.sidebar.write('\n')
    st.sidebar.write('\n')
    st.sidebar.write('\n')
    st.sidebar.write('\n')
    st.sidebar.write("BET223 est une société Malienne, dirigée par des Maliens pour les Maliens. La société BET223 fait partie du groupe BET2AFRICA, elle intervient, en partenariat avec le PMU-Mali, dans le secteur des jeux et loisirs. BET223 s’est très rapidement positionné comme un acteur incontournable dans son domaine, pour la République du Mali. Notre plus grande force, c’est le travail et l’engagement de nos équipes, et nous travaillons chaque jour en étroite collaboration avec nos fournisseurs et partenaires locaux pour participer activement au développement de notre environnement et de la communauté Malienne.")

with st.container():
    def random_value(Content):
        # Randomly choose one value
        value_choiced = random.choice(Content)
        return value_choiced
    
    def timer(duration):
        timer_text = st.empty()  # Create an empty slot to later update the timer tex
        for remaining in range(duration, 0, -1):
            #timer_text.text(f"Décompte: {remaining} secondes")
            timer_text.markdown(f"<p style='font-size:50px; font-weight:bold; background-color: #02044b;color: #fff; text-align: center;border: 2px solid #f20683; border-radius: 10px; padding: 10px;box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);'>{remaining}</p>", unsafe_allow_html=True)
            time.sleep(1)
        timer_text.empty()

    def main():
        st.title(f"Bienvenue au Tirage au sort aléatoire d'un millionnaire pour la date du {now}.")
        # File upload widget
        uploaded_file = st.file_uploader("Charger le fichier", type=["xlsx", "xls"])

        if uploaded_file is not None:
            # Read the uploaded Excel file
            sheet_name = "Feuil1" #set the sheet name
            column_name = "ID" #set the column name
            df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
            
            col1, col2 = st.columns(2)
            with col1:
                # Extract the values from the specified column
                data = df[column_name].tolist()
                st.subheader("Liste des tickets participants :")
                styled_df = df.style.set_table_styles([
                        {'selector': 'th', 'props': [('font-weight', 'bold')]},
                        {'selector': 'td', 'props': [('font-weight', 'bold')]},
                        {'selector': 'td:hover', 'props': [('background-color', 'green')]}
                    ])
                # Display the values from the specified column
                st.write(styled_df)
            # Button to trigger the random value selection
            if st.button("Lancer le Tirage"):
                # Set the time to 10 seconds to wait before the random value selection
                #time.sleep(10)
                with col2:
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    
                    timer(10)
                
                try:
                    result = random_value(data)
                    st.markdown("<p style='font-size:20px; font-weight:bold;'>Le ticket gagnant est le ticket avec l'ID :</p>", unsafe_allow_html=True)
                    st.markdown(f"<p style='font-size:100px; font-weight:bold; background-color: #f20683;color: #fff; text-align: center;border: 2px solid #02044b; border-radius: 10px; padding: 10px;box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);'>{result}</p>", unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"An error occurred: {e}")




if __name__ == "__main__":
    main()


