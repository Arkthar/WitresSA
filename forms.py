from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class DatosGrafo(Form):
    Vertices = StringField('Vertices', validators=[DataRequired()])
    Aristas = StringField('Aristas', validators=[DataRequired()])