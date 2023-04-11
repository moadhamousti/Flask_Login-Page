from website import create_app
from flask import Flask, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template('base.html')

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)
