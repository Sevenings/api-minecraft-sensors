from . import main
from flask import render_template



""" WEB PAGE 
------------------------------------------""" 

@main.route('/')
def home_route():
    return render_template('index.html')



