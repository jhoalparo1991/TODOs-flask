from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,EmailField,DateField
from wtforms.validators import DataRequired, Length, InputRequired,EqualTo
 

class LoginForm(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired(),Length(1,20)])
    password = StringField('Password', validators=[DataRequired(),Length(1,50)])
    submit_button = SubmitField('Signin')
    


class SignupForm(FlaskForm):

    fullname = StringField('Fullname', validators=[InputRequired('El nombre es requerido')])
    email = EmailField('email', validators=[InputRequired('el campo email es requerido')])
    password = PasswordField('password', validators=[InputRequired('El password es requerido'),
                                                     EqualTo('repet_password',
                                                             'Los password no coinciden')])
    repet_password = PasswordField('repet_password', validators=
                                   [InputRequired('Ingrese el nombre completo')])
    birthday = DateField('birthday')
    register_button = SubmitField('register_submit')
