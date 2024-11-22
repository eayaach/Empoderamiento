from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv
import base64
import openai

load_dotenv()

app = Flask(__name__)
cors = CORS(app)

# Configurar la clave de API
openai.api_key = os.getenv("OPENAI_API_KEY")

system_message = {
    "role": "system",
    "content": (
        "Eres un experto en reciclaje de plasticos!"
    )
}

# Inicializar la lista de mensajes
messages = [system_message]


# para procesar la imagen
def process_image_with_query(image, query):
    try:
        # Combinamos el query con la imagen (debería ser un texto procesado)
        messages.append({"role": "user", "content": query})

        response = openai.ChatCompletion.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                        "role": "user",
                        "content": [
                            {
                            "type": "text",
                            "text": "Dime si la siguiente imagen es reciclable o no, siguiendo el formato (solo espacio entre las cosas): SI/NO nombre del tipo de plastico completo",
                            },
                            {
                            "type": "image_url",
                            "image_url": {
                                "url":  f"{image}"
                            },
                            },
                        ],
                        }
                    ],
                    )
        # Obtener el mensaje del asistente
        assistant_message = response['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": assistant_message})

        # Imprimir y retornar el resultado
        print(assistant_message)
        return assistant_message

    except Exception as e:
        # Manejo de errores con más información
        print(f"Error al procesar la imagen y la consulta: {e}")
        return f"Error: {str(e)}"

@app.route("/api/generate/output", methods=['POST'])
def response():
    """Manejar solicitudes POST para generar texto."""
    print("Estoy aquí")
    data = request.get_json()
    base64_image = data['image']
    print(base64_image[0:20])

    # Procesar la imagen
    response = process_image_with_query(base64_image, "").split(' ')

    # Extraer información de la respuesta
    reciclable = response[0].strip()  # "SI" o "NO"
    tipo_plastico = response[1].strip()  # Por ejemplo, "PET"

    # Redirigir a la vista confirmación
    return redirect(url_for('confirmacion', reciclable=reciclable, tipo=tipo_plastico))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/subir')
def subir():
    return render_template('subir.html')

@app.route('/confirmacion/<reciclable>/<tipo>')
def confirmacion(reciclable, tipo):
    """Renderizar la vista de confirmación con los valores reciclable y tipo."""
    return render_template(
        'confirmacion.html',
        reciclable=reciclable,
        tipo_plastico=tipo
    )
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
