from flask import Flask,render_template,request
app=Flask(__name__)
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
        money=request.form["money"]
        note=request.form["note"]
        print(money)
        print(note)
        return render_template("add.html")

@app.route("/show")
def show():
    return render_template("show.html")

@app.route("/sort")
def sort():
    return render_template("sort.html")
  

app.run(debug=True)