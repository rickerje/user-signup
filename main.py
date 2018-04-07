from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/add", methods = ['POST'])
def verify_user():
    
    #assume no error to start
    error = False

    #request variable values from form
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']
    
    #if we need to return input field values to form
    def_username = username
    def_email = email

    #empty strings for returning error messages if needed
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    
    len_username = len(username)
    
    #test cases for verifying email
    email_countDot = 0
    email_countAmpersand = 0

    #test username for valid entry
    if username == '' or username.strip() == '':
        error = True
        username_error = "Please enter a username"
    elif len_username <= 2:
        error = True
        username_error = "Username must be 3 or more characters"
    else:
        for char in username:
            if char == " ":
                error = True
                username_error = "Password cannot have spaces"
    
    #test password and verify_password for correctness
    if password == '' or password.strip() == '':
        error = True
        password_error = "Please enter a password"

    if verify_password == '' or verify_password.strip() == '':
        error = True
        verify_password_error = "Please enter a password"
    
    if not password == verify_password:
        error = True
        verify_password_error = "Password does not match"

    #validate email, look for one period and one ampersand
    if not email == '':              #email is optional
        for character in email:
            if character == ".":
                email_countDot += 1
            if character == "@":
                email_countAmpersand += 1
    
        if email_countDot != 1 or email_countAmpersand != 1:
            error = True
            email_error = "Password must have one @ and one ."


    if error:
        return render_template("signup.html", 
            username=username,
            username_error = username_error, 
            password_error = password_error, 
            verify_password_error = verify_password_error,
            email_error = email_error,
            def_username=def_username,
            def_email=def_email)
            
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