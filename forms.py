from wtforms import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class DatosGrafo(Form):
    Vertices = StringField('Vertices', validators=[DataRequired()])
    Aristas = StringField('Aristas', validators=[DataRequired()])
    submit = SubmitField('Ingresar')
