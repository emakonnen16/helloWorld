from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello BMGT407 from Endalk! This is my about page (Updated to Module 8)'

@app.route('/about')
def about_me():  # put application's code here
    return render_template('about.html')

@app.route('/favorite_course')
def favorite_course():
    fun_courses = [str(request.args.get('department') + request.args.get('course_no'))]
    return render_template('favorite_course.html', courses=fun_courses)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run()
