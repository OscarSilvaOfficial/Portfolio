from flask import *

app = Flask(__name__, template_folder='../frontend/template', static_folder='../frontend/static')

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)