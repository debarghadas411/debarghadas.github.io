from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/blog')
def blog():
    return render_template('blog.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/service')
def service():
    return render_template('service.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
