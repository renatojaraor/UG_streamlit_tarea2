import streamlit as st

st.title('Mi Primera Aplicación en Streamlit')

st.title('Renato Jara')

# Barra Lateral (st.sidebar)
st.sidebar.header("Configuración")

# Input Box para Edad (rango 0 a 100)
edad = st.sidebar.slider("Edad", min_value=0, max_value=100, value=25)
st.sidebar.write(f"Edad seleccionada: {edad} años")

# Text Input para Nombres y Apellidos
nombres = st.sidebar.text_input("Nombres y Apellidos")
st.sidebar.write(f"Nombre ingresado: {nombres}")

# Slider para Seleccionar Mes
mes = st.sidebar.slider("Seleccionar Mes", min_value=1, max_value=12, value=1)
st.sidebar.write(f"Mes seleccionado: {mes}")

# Checkbox para Aceptar Términos
aceptar_terminos = st.sidebar.checkbox("Acepto los Términos y Condiciones")
if aceptar_terminos:
    st.sidebar.write("Términos y condiciones aceptados.")
else:
    st.sidebar.write("Aún no ha aceptado los términos.")

# Radio Buttons para Género
genero = st.sidebar.radio("Género", ("Masculino", "Femenino", "Otro"))
st.sidebar.write(f"Género seleccionado: {genero}")

# Selectbox para Seleccionar País
pais = st.sidebar.selectbox("Selecciona tu País", ["México", "Ecuador", "Argentina", "Colombia", "Chile"])
st.sidebar.write(f"País seleccionado: {pais}")

# Button para Enviar Información
if st.sidebar.button("Enviar Información"):
    st.sidebar.write("Información enviada correctamente!")

# File Uploader para Cargar Archivo
archivo = st.sidebar.file_uploader("Cargar un archivo", type=["csv", "txt", "jpg", "png"])
if archivo is not None:
    st.sidebar.write(f"Archivo cargado: {archivo.name}")

# Date Input para Seleccionar una Fecha
fecha = st.sidebar.date_input("Selecciona una Fecha")
st.sidebar.write(f"Fecha seleccionada: {fecha}")

# Time Input para Seleccionar una Hora
hora = st.sidebar.time_input("Selecciona una Hora", value=None)
st.sidebar.write(f"Hora seleccionada: {hora}")

# Mostrar los datos en la aplicación principal
st.write("### Datos Ingresados:")
st.write(f"Edad: {edad} años")
st.write(f"Nombre: {nombres}")
st.write(f"Mes: {mes}")
st.write(f"Género: {genero}")
st.write(f"País: {pais}")
st.write(f"Aceptó los términos: {aceptar_terminos}")
st.write(f"Fecha seleccionada: {fecha}")
st.write(f"Hora seleccionada: {hora}")

# Si se cargó un archivo, mostrar información del archivo
if archivo is not None:
    st.write(f"Se cargó el archivo: {archivo.name}")