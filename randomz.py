from flask import Flask, render_template
import random
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("sitio.html", nome = random.randint(1, 100))
if __name__ == "__main__":
    app.run(debug=True)
