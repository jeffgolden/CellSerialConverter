from flask import Flask, render_template, request
from CellSerialConverter import translate_serial

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    translation = None
    if request.method == 'POST':
        serial = request.form.get('serial', '').strip()
        translation = translate_serial(serial)
    return render_template('index.html', result=translation)


if __name__ == '__main__':
    app.run(debug=True)
