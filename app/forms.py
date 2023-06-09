from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Length
 

class LoginForm(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired(),Length(1,20)])
    password = StringField('Password', validators=[DataRequired(),Length(1,50)])
    submit_button = SubmitField('Signin')
    