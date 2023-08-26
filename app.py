from flask import Flask, redirect, render_template, request, url_for
from jinja2 import TemplateNotFound

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('home/index.html')

@app.route('/index.html')
def route_home():
    return render_template('home/index.html')

@app.route('/page_sign_up.html')
def route_sign_up():
    return render_template('home/page_sign_up.html')

@app.route('/page_about_us.html')
def route_about_us():
    return render_template('home/page_about_us.html')

@app.route('/page_sign_in.html')
def route_sign_in():
    return render_template('home/page_sign_in.html')

@app.route('/page_contact_us.html')
def route_contact_us():
    return render_template('home/page_contact_us.html')


