#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index ():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def test_print_route(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    output = ""
    for i in range (parameter):
        output += f"{i}\n"
    return output

@app.route('/math/<int:num1>/<operator>/<int:num2>')
def math(num1, operator, num2):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "div":
        result = num1 / num2 if num2 != 0 else "Error"
    elif operator == "%":
        result = num1 % num2 if num2 != 0 else "Error" 
    else: 
        return "Invalid operator"
    
    return str(result)
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
