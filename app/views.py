from flask import Blueprint, redirect, render_template, url_for, session

app_route = Blueprint('app',__name__)

@app_route.errorhandler(404)
def page_not_found(error):
    return 'Page not found'

@app_route.route('/')
def login():
    return redirect(url_for('auth.login'))


@app_route.route('/home', methods=['GET','POST'])
def home_page():
        
    return render_template('home.html')