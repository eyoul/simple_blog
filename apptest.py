from flask import Flask, request
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/mydatabase' # Replace with your database connection details
db = SQLAlchemy(app)

# Define a model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# Create the database tables (you only need to do this once)
db.create_all()

# Route to query the database
@app.route('/')
def index():
    users = User.query.all()
    return str(users)

if __name__ == '__main__':
    app.run(debug=True)