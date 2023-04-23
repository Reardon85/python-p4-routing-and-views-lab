#!/usr/bin/env python3

from flask import Flask




app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    value= ''
    for i in range(parameter):
        value += f'{i}' + '\n'
    return value

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    value = 0
    if (operation == '+'):
        value = num1 + num2
    elif(operation == '-'):
        value = num1 - num2
    elif(operation == '*'):
        value = num1 * num2
    elif(operation == 'div'):
        value = num1 / num2 
    elif(operation == '%'):
        value = num1 % num2
    return str(value)




if __name__ == '__main__':
    app.run(port=5555, debug=True)
