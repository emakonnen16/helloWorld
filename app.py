from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def about_me():  # put application's code here
    return 'Hello from Endalk! This leads to my about page.'
#app

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
