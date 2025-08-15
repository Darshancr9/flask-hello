from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
 return "Hello from Flask on EC2 via Jenkins + Docker! ✅"
# gunicorn will import "app:app", so no __main__ needed.
