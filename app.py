import gradio as gr
from funciones import *

with gr.Blocks(
    theme=gr.themes.Default(),
    title="FastReading"
) as webapp:
    with gr.Tabs() as tabs:
        with gr.TabItem("Escribir") as tab1:
            with gr.Column():
                texto = gr.Textbox(lines=5)
        with gr.TabItem("Leer") as tab2:
            with gr.Column():
                label_texto = gr.Label(value=texto.value)
                velocidad = gr.Slider(minimum=1, maximum=100, step=1, interactive=True, label="Velocidad (palabras por minuto)")
                leer = gr.Button(value="Comenzar")
                leer.click(iniciar_lectura, inputs=[label_texto, texto, velocidad])

webapp.launch()