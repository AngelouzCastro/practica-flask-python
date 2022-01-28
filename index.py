from flask import Flask
from flask.templating import render_template

app = Flask(__name__)
"""
@app.route('/')
def principal():
    return "Bienvenido a mi sitio web con python! soy angel"

@app.route('/contacto')
def contacto():
    return "pagina de contacto"
"""

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

@app.route('/lenguajes')
def lenguajes():
    mislenguajes = ("Php","Python","Java","C#","JavaScript","C++","Scala") 
    return  render_template('lenguajes.html',lenguajess=mislenguajes)

if __name__ == '__main__':
    app.run(debug=True, port=5017)