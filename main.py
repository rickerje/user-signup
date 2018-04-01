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
#    email = request.form['email']

    if username == '' or username.strip() == '':
        error = True
        username_error = "Please enter a username"
    
    elif password == '' or password.strip() == '':
        error = True
        password_error = "Please enter a password"

    elif verify_password == '' or verify_password.strip() == '':
        error = True
        verify_password_error = "Please enter a password"
    
    elif password and verify_password and not password == verify_password:
        error = True
        verify_password_error = "Password does not match"

    if error:
        return redirect("/", username_error = username_error, password_error = password_error, verify_password_error = verify_password_error)
    else:
        return render_template('welcome.html', username = username)


@app.route("/", methods = ['POST', 'GET'])
def index():
    username_error = request.args.get("username_error")
    password_error = request.args.get("password_error")
    return render_template('signup.html', username_error=username_error, password_error=password_error)

app.run()