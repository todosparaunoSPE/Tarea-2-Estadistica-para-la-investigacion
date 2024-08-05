import streamlit as st

# Configurar la página
st.title("Redirección con Botones")

# Definir los enlaces a los que se redirigirá
enlace_1 = "https://tarea-2-epi-fvyj9oahajx88jhxiunm9g.streamlit.app/"
enlace_2 = "https://www.example2.com"

# Función para redirigir al usuario
def redirigir(url):
    st.markdown(f'<meta http-equiv="refresh" content="0; url={url}">', unsafe_allow_html=True)

# Crear botones y redirigir al pulsarlos
if st.button("Ir a Enlace 1"):
    redirigir(enlace_1)

if st.button("Ir a Enlace 2"):
    redirigir(enlace_2)
