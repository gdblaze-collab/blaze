from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def json():
   marks = {
      "rohan": 65,
      "anita": 85,
      "priya": 90
   }
   return jsonify(marks)


app.run(debug=True)
