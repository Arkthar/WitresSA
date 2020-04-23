from wtforms import Form #llama a wtforms
from wtforms import StringField , SubmitField #tipos de datos que almacena la clase
from wtforms.validators import DataRequired #validador

class DatosGrafo(Form): 
    Vertices = StringField('Vertices', validators=[DataRequired()]) #tipo strings
    Aristas = StringField('Aristas', validators=[DataRequired()]) #el validador acusa al usuario
    submit = SubmitField('Ingresar')