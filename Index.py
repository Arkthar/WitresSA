from flask import Flask, render_template, request, url_for, redirect, send_file
from forms import DatosGrafo 
from config import Config

app = Flask(__name__)

@app.route('/') #Se crea pagina principal
def home():
    return render_template('home.html')

@app.route('/About') #Se crea pagina About
def about():
    return render_template('About.html')

@app.route('/Dostoievskys', methods=['GET','POST']) #Se crea pagina Dostoievskys
def Dostoievskys():
    form = DatosGrafo(request.form)
    if request.method == 'POST':
        print(form.Vertices.data)
        print(form.Aristas.data)
        return render_template("grafo.html")

    return render_template('Dostoievskys.html')

@app.route('/Arkthar') #Se crea pagina Arkthar
def Arkthar():
    return render_template('Arkthar.html')


if __name__=='__main__':
    app.run(debug=True)