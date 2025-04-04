from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

# Below is needed because by default Flask binds to local host, which prevents external access from Docker
# This allows flask to listen on all available network interfaces, including Docker
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)