import streamlit as st

# Configurar la página
st.title("Tarea 2: Estadística para la investigación")

# Definir los enlaces a los que se redirigirá
Tarea_2 = "https://tarea-2-epi-fvyj9oahajx88jhxiunm9g.streamlit.app/"
Tarea_2_1 = "https://www.example2.com"

# Función para redirigir al usuario
def redirigir(url):
    st.markdown(f'<meta http-equiv="refresh" content="0; url={url}">', unsafe_allow_html=True)

# Crear botones y redirigir al pulsarlos
if st.button("Ir a Tarea 2"):
    redirigir("Tarea_2")

if st.button("Ir a Tarea 2.1"):
    redirigir("Tarea_2_1")
