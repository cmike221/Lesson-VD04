from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index_t():
    current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index_t.html', current_date_time=current_date_time)

if __name__ == '__main__':
    app.run(debug=True)
