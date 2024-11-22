import openai
import os
from dotenv import load_dotenv


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    # Realizar una prueba de conexión llamando a la API de modelos
    response = openai.Model.list()
    print("Conexión exitosa. Modelos disponibles:")
    for model in response['data']:
        print(model['id'])
except Exception as e:
    print(f"Error al conectar con OpenAI: {e}")