#Libreria flask para pagina web
from flask  import Flask, render_template,request,url_for
from forms import DatosGrafo 
from config import Config

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

@app.route('/Arkthar', methods=['GET','POST']) #Se crea pagina Arkthar
def Arkthar():
    form = DatosGrafo(request.form)
    if request.method == 'POST':
        print(form.Vertices.data)
        print(form.Aristas.data)
        return render_template("grafo.html")
    return render_template('Arkthar.html')    
    



if __name__=='__main__':
    app.run(debug=True)

    #dfgsd