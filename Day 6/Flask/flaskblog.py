from flask import Flask, render_template, url_for,flash, redirect
from flask_sqlalchemy import SQLAlchemy
# sqllite database will be file in our filesystem
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '6baf93b1470f88bd1a1b31ac7834cc91'
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///site.db'
# for sqllite we can specify a relative path as ///


db = SQLAlchemy(app)  # sqlalchemy db instance # wecan represent db structures as classes

class User(db.Model):
    id = db.Column(db.Integer, primary)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) #home is the name of the function
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
    


if __name__ == '__main__':
    app.run(debug=True)