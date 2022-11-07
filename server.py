from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/hello")
def hello2():
  return "This is a test"

if __name__ == "__main__":
  app.run()
