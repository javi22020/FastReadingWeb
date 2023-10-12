import gradio as gr
import time as tm
import asyncio

def iniciar_lectura(label_texto: gr.Label, texto: gr.Textbox, velocidad: gr.Slider):
    palabras = texto.split()
    for palabra in palabras:
        label_texto.update(value=palabra)
