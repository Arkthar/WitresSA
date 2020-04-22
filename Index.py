#Libreria flask para pagina web
#render_templates, es para plantillas en html
#request, es para parametros por Url
#las llaves {} para llamar algo desde python
#url_for
#send_file
#forms es para formularios
#este es el formulario donde se reciben los datos del grafo 
#field es para el dato que se esta recibiendo
#vertices y aristas son string
from flask  import Flask, render_template

app = Flask(__name__)

@app.route('/') #Se crea pagina principal
def home():
    return render_template('home.html')

@app.route('/About') #Se crea pagina About
def about():
    return render_template('About.html')

@app.route('/Dostoievskys') #Se crea pagina Dostoievskys
def Dostoievskys():
    return render_template('Dostoievskys.html')
    
@app.route('/Arkthar') #Se crea pagina Arkthar
def Arkthar():
    return render_template('Arkthar.html')


if __name__=='__main__':
    app.run(debug=True)

    #dfgsd