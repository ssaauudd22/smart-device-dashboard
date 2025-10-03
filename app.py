from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/usage")
def usage():
    data = [
        {"device": "printer 001", "pages_printed": 147, "ink_level": 35},
        {"device": "printer 002", "pages_printed": 60, "ink_level": 83},
        {"device": "Scanner 001", "scans": 25, "energy_used": 1.9}
    ]
    return jsonify({"data": data})

if __name__ == "__main__":
    app.run(debug=True)