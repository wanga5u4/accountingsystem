from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return """ <h1>我的记账系统</h1>
    <p>欢迎使用Boyan的记账系统</p>"""
app.run(debug=True)