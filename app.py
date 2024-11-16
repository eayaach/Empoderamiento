from flask import Flask, render_template, request
import psycopg2
from credentials import CREDENTIALS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    connection = None
    cur = None
    try:
        # Conectar a la base de datos
        connection = psycopg2.connect(**CREDENTIALS)
        cur = connection.cursor()

        results = cur.fetchall()
        print(results)
        headers = [description[0] for description in cur.description]

        if not results:
            print("No se encontraron resultados en la tabla 'suscripciones'.")
        return render_template('search.html', data=results, search_term=search_query, query_number = query_number, headers=headers)

    except psycopg2.Error as e:
        print(f"Error al interactuar con la base de datos: {e}")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    finally:
        # Cerrar el cursor y la conexión
        if cur:
            cur.close()
        if connection:
            connection.close()



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)