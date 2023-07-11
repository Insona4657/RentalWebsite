from flask import Blueprint
from flask import render_template, request, Blueprint, url_for
#from flaskrental.models import Product

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    image_file = url_for('static', filename='pictures/Neoleehospitalbed1.jpg')
    return render_template('home.html', image_file=image_file)

@main.route("/contact")
def contact():
    return render_template('contact.html')


@main.route("/sample")
def sample():
    return render_template('sample.html')