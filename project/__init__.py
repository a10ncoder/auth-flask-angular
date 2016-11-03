
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy  import SQLAlchemy
from project.config import BaseConfig


# config

app = Flask(__name__)
app.config.from_object(BaseConfig)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


@app.route('/')
def index():
    return app.send_static_file('index.html')
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    pass


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    pass

