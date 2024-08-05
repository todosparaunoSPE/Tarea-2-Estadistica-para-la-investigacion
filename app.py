# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:17:05 2024

@author: jperezr
"""

import streamlit as st

# Set the title
st.title("CONSAR ESTADÍSTICAS")

# CSS to inject custom styles
st.markdown("""
    <style>
    .stButton > button {
        color: white;
        background-color: #007BFF; /* Blue color */
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        font-size: 16px;
    }
    .stButton > button:hover {
        background-color: #0056b3; /* Darker blue on hover */
    }
    </style>
    """, unsafe_allow_html=True)

# Create 3 buttons that link to Google
if st.button('Tarea 2'):
    st.write('[Tarea 2](https://tarea-2-epi-fvyj9oahajx88jhxiunm9g.streamlit.app/)')

if st.button('Tarea 2.1'):
    st.write('[Tarea 2.1](https://tarea-21-hpiqhe6e3ythirwzkjakgk.streamlit.app/)')




st.sidebar.write("© 2024 Creado por: Javier Horacio Pérez Ricárdez")
