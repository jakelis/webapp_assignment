from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index1.html")

@app.route("/select", methods=["POST"])
def select():
  if request.form.get("diet") == "vegetarian" and request.form.get("staple_food") == "rice":
    return render_template("combi_1.html")
    
  elif request.form.get("diet") == "non-vegetarian" and request.form.get("staple_food") == "rice":
    return render_template("combi_2.html")

  elif request.form.get("diet") == "vegetarian" and request.form.get("staple_food") == "noodles":
    return render_template("combi_3.html")

  elif request.form.get("diet") == "non-vegetarian" and request.form.get("staple_food") == "noodles":
    return render_template("combi_4.html")

app.run(host='0.0.0.0', port=81)
