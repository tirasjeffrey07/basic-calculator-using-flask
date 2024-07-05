from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return "", 404


@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/calculate', methods = ["POST"])
def calculate():
    expression = request.form.get("input_text")
    
    regexPattern =  r'^[\d\s.\-+*/()]+$'
    
    if re.match(regexPattern, expression):
        # expression is valid
        try:
            # eval evaluates expression which comes as a string 
            result = eval(expression)  
            
            return jsonify({"status": "success", "message": str(result)})
        
        except Exception as e:
            
            return jsonify({"status": "error", "message": "Error evaluating expression"}), 400
    else:
        # expression is invalid
        return jsonify({"status": "error", "message": "Invalid expression"}), 400

if __name__ == "main":
    app.run(debug = True)
