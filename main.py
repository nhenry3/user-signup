from flask import Flask, request, redirect, render_template
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['POST'])
def verify_signup():


    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verifypassword']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''
    
        
    if username =='' or ' ' in username or len(username) < 3 or len(username) > 20:
        username_error = 'Enter a valid user name'
        


    if password =='' or len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = 'Enter a valid password'
        
    
  
    if verify_password == '' or verify_password != password:
        verify_password_error ='Password does not match original'

    if email != "":
        if "@" not in email or "." not in email or ' ' in email or len(email) < 3 or len(email) > 20:
            email_error = 'Enter a valid email'

    if username_error == "" and password_error == "" and verify_password_error == "" and email_error == "":
        return render_template('welcome.html', username = username)

    else:
        return render_template('signup.html', username_error = username_error, password_error = password_error, 
    verify_password_error = verify_password_error, email_error = email_error, username=username, email=email)
    


@app.route("/")
def index():
    return render_template('signup.html')






app.run()