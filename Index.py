#Libreria flask para pagina web
from flask  import Flask, render_template
app = Flask(__name__)

@app.route('/') #Se crea pagina principal
def home():
    return render_template('home.html')

@app.route('/LosCasiCra') #Se crea pagina About
def about():
    return render_template('Casicra.html')

@app.route('/Dostoievskys') #Se crea pagina Dostoievskys
def Dostoievskys():
    return render_template('Dostoievskys.html')
    
@app.route('/Arkthar') #Se crea pagina Arkthar
def Arkthar():
    return render_template('Arkthar.html')

@app.route('/Muchopoquitonada') #Se crea pagina Muchopoquitonada
def Muchopoquitonada():
    return render_template('Muchopoquitonada.html')


if __name__=='__main__':
    app.run(debug=True)

    #dfgsd