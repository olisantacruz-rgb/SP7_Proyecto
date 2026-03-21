import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis de Vehículos en Venta 🚗')

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)
    # BOTÓN 2: GRÁFICO DE DISPERSIÓN
# =========================
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Relación entre el odómetro y el precio de los vehículos')

    # Crear gráfico de dispersión
    fig_scatter = go.Figure(
        data=[
            go.Scatter(
                x=car_data['odometer'],
                y=car_data['price'],
                mode='markers'
            )
        ]
    )

    # Título del gráfico
    fig_scatter.update_layout(
        title='Relación entre Odómetro y Precio',
        xaxis_title='Odómetro',
        yaxis_title='Precio'
    )

    # Mostrar gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)