from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello BMGT407 from Endalk! This is my about page'

@app.route('/about')
def about_me():  # put application's code here
    return render_template('about.html')

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/favorite-course', methods=['GET','POST'])
def favorite_course():  # put application's code here
    if request.method == "POST":
        print('You entered your favorite course as: ' + request.form.get('department') + request.form.get('course_no'))
    return render_template('favorite-course.html')

if __name__ == '__main__':
    app.run()
