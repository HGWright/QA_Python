from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, DecimalField, SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = ''

class BasicForm(FlaskForm):
    first_name = StringField('First Name:')
    last_name = StringField('Last Name:')
    submit = SubmitField('Add Details:')
    age = IntegerField('Age:')
    dob = DateField('Date of Birth:', format = '%d-%m-%y')
    weight = DecimalField('Weight:')
    hobby = SelectField('Hobby:', choices= [('sport', 'Sports'), ('gaming', 'Video Games'), ('music', 'Music'), ('none', 'None')])

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supple both a first and last name"
        else:
            return f"Thank you {first_name} {last_name} for registering with us!"
    return render_template('home.html', form = form, message = error)

if __name__ == '__main__':
    app.run(debug = True)