import gradio as gr
import time as tm
import asyncio

def iniciar_lectura(label_texto: gr.Label, texto: gr.Textbox, velocidad: gr.Slider):
    palabras = texto.split()
    for palabra in palabras:
        yield palabra

async def lectura(label_texto):
    tm.sleep(1)
    yield label_texto
