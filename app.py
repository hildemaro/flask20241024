from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola, Azure 2024, Soy hildemaro cardenas! Esta App es vulnerable"

# Conexión a la base de datos SQLite
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Página de inicio vulnerable a XSS
@app.route('/')
def index():
    name = request.args.get("name", "")
    template = f"<h1>Hola {name}</h1>"  # El valor de 'name' se inserta sin sanitización, lo que permite XSS
    return render_template_string(template)

# Página vulnerable a inyección SQL
@app.route('/search')
def search():
    query = request.args.get("query", "")
    conn = get_db_connection()
    # Vulnerabilidad: consulta SQL directa, sin parametrización
    posts = conn.execute(f"SELECT * FROM posts WHERE title LIKE '%{query}%'").fetchall()
    conn.close()

    result = "<h2>Resultados de la búsqueda:</h2><ul>"
    for post in posts:
        result += f"<li>{post['title']}: {post['content']}</li>"
    result += "</ul>"
    return render_template_string(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
