from flask import Flask, render_template , app , request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mj.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Contacts(db.Model):
    # sno = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(20), nullable=False, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    Phone = db.Column(db.String(120), nullable=False)
    msg = db.Column(db.String(200), nullable=False)
    # date = db.Column(db.String(20), nullable=True)

    
@app.route('/')
def hello_world():
    return render_template("index.html")

# @app.route('/about')
# def about():
#     return render_template("about.html")

@app.route('/contact', methods = ['GET' , 'POST'])
def contact():
    if (request.method=='POST'):
        # sno = request.form.get('sno')
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        msg = request.form.get('msg')

        entry = Contacts( name = name , email = email, Phone = phone , msg = msg)
        # entry = Contacts(name = name , email = email, phone_num = phone , msg = msg, date = datetime.now())
        db.session.add(entry)
        db.session.commit()    
    return render_template('contact.html')
app.run(debug=True)