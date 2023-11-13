from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__)

# Configuración de la conexión a la base de datos Access
connection = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\PC 1\Downloads\parcialpa\new\Ventas.accdb;'
)

cursor = connection.cursor()

@app.route('/')
def index():
    # Ejecutar la consulta
    cursor.execute('SELECT cliente.nombre, cliente.apellidos, cliente.contactos, consulta.cantidad, consulta.modelo, consulta.precio, consulta.fecha FROM cliente INNER JOIN consulta ON cliente.Id = consulta.Id;')
    results = cursor.fetchall()

    # Pasar resultados a la plantilla HTML
    return render_template('index.html', data=results)

if __name__ == '__main__':
    app.run(debug=True)