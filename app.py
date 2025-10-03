from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/usage")
def usage():
    data = {
        "device": "printer 001",
        "pages_printed": 120,
        "ink_level": 65,
        "energy_used_kwh": 3.4
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)