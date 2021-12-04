import flask
import calclib

app = flask.Flask(__name__)
calc = calclib.VecCalc()

error_msg = '500 Internal Server Error\n'

@app.route('/suma/', methods=['POST'])
def suma():
    data = flask.request.json

    try:
        result = calc.addition(data["v1"], data["v2"])
    except:
        return error_msg

    return f'{result}\n'

@app.route('/resta/', methods=['POST'])
def resta():
    data = flask.request.json
    
    try:
        result = calc.subtraction(data["v1"], data["v2"])
    except:
        return error_msg
    
    return f'{result}\n'

@app.route('/mult/', methods=['POST'])
def multi():
    data = flask.request.json
    
    try:
        result = calc.multiplication(data["v1"], data["v2"])
    except:
        return error_msg

    return f'{result}\n'

@app.route('/divis/', methods=['POST'])
def divis():
    data = flask.request.json

    try:
        result = calc.division(data["v1"], data["v2"])
    except:
        return error_msg

    return f'{result}\n'

@app.route('/')
def main():
    return 'This is a REST API.\n'