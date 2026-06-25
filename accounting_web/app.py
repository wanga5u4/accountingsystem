from flask import Flask,render_template,request
import pandas as pd
app=Flask(__name__)
records=[]

def load_data():
    global records
    try:
        df=pd.read_csv("money.csv")
        records=df.to_dict("records")
        print("加载成功")
    except FileNotFoundError:
        records = []
        print("没有找到历史记录")

load_data()

def save_data():
    df=pd.DataFrame(records)
    df.to_csv("money.csv",index=False)

@app.route("/")
def home():
    username="boyan"
    return render_template(
        "home.html",
        username=username)


@app.route("/add",methods=["GET","POST"])
def add():
    if request.method=="GET":
        return render_template("add.html")
    else:
        money=int(request.form["money"])
        note=request.form["note"]
        records.append({
            "金额":money,
            "备注":note
            })
        save_data()
        return render_template("add.html")

@app.route("/show")
def show():
    return render_template(
    "show.html",
    records=records)

@app.route("/sort")
def sort():
    return render_template("sort.html")
  

app.run(debug=True)