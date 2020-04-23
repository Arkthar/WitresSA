from wtforms import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class DatosGrafo(Form):
    vertices = StringField('Vertices', validators=[DataRequired()])
    aristas = StringField('Aristas', validators=[DataRequired()])
    submit = SubmitField('Ingresar')
