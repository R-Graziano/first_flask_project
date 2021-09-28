from wtforms import Form
from wtforms import StringField, TextField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import HiddenField
from wtforms import validators
from models import User

def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio.')


class CommentForm(Form):
    comment = TextField('Comentario',
                        [
                            validators.length(min=1,max=200, message='El comentario no puede estar vacío y no debe superar los 200 caracteres.')
                        ])
    honeypot = HiddenField('',
                [length_honeypot])

class LoginForm(Form):
    username = StringField('Username',
                [
                    validators.Required(message = 'El username es requerido!'),
                    validators.length(min=4, max=25, message='Ingrese un username valido!')
                ])
    password = PasswordField('Password', [validators.Required(message='El password es requerido!')])
    honeypot = HiddenField('',
                [length_honeypot])

class CreateForm(Form):
    username = TextField('Username',
                [
                    validators.Required(message = 'El username es requerido!'),
                    validators.length(min=4, max=50, message='Ingrese un username valido!')
                ])
    email = EmailField('Correo Electronico',
                [ validators.Required(message = 'El email es requerido!'),
                  validators.Email(message = 'Ingrese un email valido!'),
                  validators.length(min=4, max=50, message= 'Ingrese un email valido.')
                ])
    password = PasswordField('Password', [validators.Required(message='El password es requerido!')])

    def validate_username(form, field):
        username = field.data 
        user = User.query.filter_by(username = username).first()
        if user is not None:
            raise validators.ValidationError('El username ya se encuentra registrado.')