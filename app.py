from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def about_world():  # put application's code here
    return 'Hello BMGT407 from Endalk! This is my about page'
#helloo

@app.route('/about')
def about_me():  # put application's code here
    return render_template('about.html')

@app.route('/2')
def hello_world():  # put application's code here
    return 'Hello World from Endalk! This is my first page'
#helloo

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()
