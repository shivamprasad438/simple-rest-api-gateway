from flask import Flask

app = Flask(__name__)

@app.route('/')
def service1():
    return "Response from Service 4"

if __name__ == '__main__':
    app.run(port=5001)
