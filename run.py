from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def login():
    return render_template('login.html')


def hello_world():
	if request.method == 'POST':
        #Fetch the form data
        userDetails = request.form
        userDetails['email']
        userDetails['password']
    return render_template('index.html')

if __name__ == '__main__':
	app.run(debug = True);
