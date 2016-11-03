from flask import Flask

app = Flask(__name__)


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


if __name__ == '__main__':
	app.run(debug=True)