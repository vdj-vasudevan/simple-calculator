from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        data = request.get_json()
        expression = data.get("expression", "")

        # Safely evaluate the expression
        result = eval(expression)  # ⚠️ Avoid using `eval` in production without sanitization

        return jsonify({"result": f"Result - {result}"}),200
    except Exception:
        return jsonify({"result": "Error"}), 400

if __name__ == "__main__":
    app.run(debug=True)
