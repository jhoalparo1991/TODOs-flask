from ..forms import LoginForm
from . import auth
from flask import render_template,session

@auth.errorhandler(404)
def page_not_found(error):
    return 'Error page',error

@auth.route('/login', methods=['GET','POST'])
def login():
    
    session['username'] = ''
    form = LoginForm()
    context = {
        'login_form' : form
    }
    
    if form.validate_on_submit():
        
        return render_template('home.html')
    
    
    return render_template('auth/index.html',**context)

