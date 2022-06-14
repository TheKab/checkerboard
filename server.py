from flask import Flask, render_template

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def check_zero():
    return render_template("index.html", num1=8, num2=8)

@app.route('/<int:num1>/<int:num2>')          # The "@" decorator associates this route with the function immediately following
def check_one(num1, num2):
    return render_template("index.html", num1=num1, num2=num2)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.