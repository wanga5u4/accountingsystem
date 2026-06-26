from flask import Flask,render_template,request,redirect,url_for
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
        type_=request.form["type_"]
        note=request.form["note"]
        records.append({
            "金额":money,
            "类型":type_,
            "备注":note
            })
        save_data()
        return redirect("/add")


@app.route("/show")
def show():
    search_result=[]
    keyword = request.args.get("keyword")
    if not keyword:
        return render_template(
        "show.html",
        records=records)
    else:
        for record in records:
            if keyword in record["备注"]:
               search_result.append(record)
        return render_template(
            "show.html",
            records=search_result) 

@app.route("/sort")
def sort():
    total_income=0
    total_expense=0
    for record in records:
        if record["类型"] == "收入":
            total_income += record["金额"]
        elif record["类型"] == "支出":
            total_expense += record["金额"]
    balance = total_income - total_expense    
    return render_template(
        "sort.html",
        total_income=total_income,
        total_expense=total_expense,
        balance=balance)

@app.route("/delete/<int:index>")
def delete(index):
    records.pop(index)
    save_data()
    return redirect("/show")

@app.route("/edit/<int:index>",methods=["GET","POST"])
def edit(index):
    if request.method=="GET":
        record=records[index]
        return render_template(
        "edit.html",
        record=record,
        index=index)
        
    else:
        money=int(request.form["money"])
        note=request.form["note"]
        type_=request.form["type_"]
        records[index]={
            "金额":money,
            "备注":note,
            "类型":type_
            }
        save_data()
        return redirect("/show")


app.run(debug=True)