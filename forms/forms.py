from wtforms import Form, validators
from wtforms.fields import StringField, IntegerField, EmailField, DateField


class Login(Form):
    email = EmailField(validators=[
        validators.data_required(message='El correo es obligatorio'),
        validators.email(message='Escribe un correo válido')
    ])
    password = StringField(validators=[
        validators.data_required(message='La contraseña es obligatoria'),
        validators.length(min=8, message='Agrega al menos 8 caracteres en la contraseña')
    ])

class Singup(Login):
    fullname = StringField(validators=[
        validators.data_required(message='El nombre es obligatorio'),
        validators.length(min=2, max=120, message='Agrega tu nombre completo')
    ])
    address = StringField(validators=[
        validators.data_required(message='La direccíon es obligatorio'),
        validators.length(min=2, max=120, message='Agrega una dirección válida')
    ])
    phone_number = IntegerField(validators=[
        validators.data_required(message='El número de teléfono es obligatorio'),
        validators.number_range(min=10, message='El número de teléfono debe tener 10 digitos')
    ])
    birth_date = DateField(format='%Y-%m-%d', validators=[
        validators.data_required(message='Escribe tu fecha de nacimiento')
    ])