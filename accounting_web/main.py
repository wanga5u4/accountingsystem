from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return "<h1>记账系统<h1>"
app.run(debug=True)