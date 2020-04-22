#Rama Jen
from flask  import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/About')
def about():
    return render_template('About.html')

@app.route('/Dostoievskys')
def Dostoievskys():
    return render_template('Dostoievskys.html')
    
@app.route('/Arkthar')
def Arkthar():
    return render_template('Arkthar.html')


if __name__=='__main__':
    app.run(debug=True)

    #dfgsd