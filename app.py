from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello BMGT407 from Endalk! This is my about page'

@app.route('/about')
def about_me():  # put application's code here
    return render_template('about.html')

@app.route('/favorite_course')
def favorite_course():  # put application's code here
    return render_template('favCourse.html')

@app.route('/favorite_courses')
def favorite_courses():  # put application's code here
    return render_template('favorite_course.html')

if __name__ == '__main__':
    app.run()
