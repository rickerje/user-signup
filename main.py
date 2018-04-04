from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/add", methods = ['POST'])
def verify_user():
    
    error = False
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify-password']
    username_error = ''
    password_error = ''
    verify_password_error = ''

#  email = request.form['email']

    if username == '' or username.strip() == '':
        error = True
        username_error = "Please enter a username"
    
    if password == '' or password.strip() == '':
        error = True
        password_error = "Please enter a password"

    if verify_password == '' or verify_password.strip() == '':
        error = True
        verify_password_error = "Please enter a password"
    
    if not password == verify_password:
        error = True
        verify_password_error = "Password does not match"

    if error:
        return render_template("signup.html", 
            username=username,
            username_error = username_error, 
            password_error = password_error, 
            verify_password_error = verify_password_error)
    else:
        return render_template('welcome.html', username = username)


@app.route("/", methods = ['POST'])
#def validate_user():
#    username_error = request.args.get("username_error")
#    password_error = request.args.get("password_error")
#    verify_password_error = request.args.get("verify_password_error")

#    return render_template('signup.html', 
#        username_error=username_error, 
#        password_error=password_error, 
#        verify_password_error=verify_password_error)

@app.route("/")
def display_signup_form():
    return render_template('signup.html')
    
    
app.run()